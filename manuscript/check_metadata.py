"""Read primary bibliographic metadata for the sources cited in this draft."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json, re, requests
from html.parser import HTMLParser
from make_bibliography import FORMAL

ROOT=Path(__file__).resolve().parent
class Meta(HTMLParser):
    def __init__(self): super().__init__(); self.values={}
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='meta' and a.get('name','').startswith('citation_'):
            self.values.setdefault(a['name'],[]).append(a.get('content',''))
def fetch(row):
    key,url=row
    try:
        if key in FORMAL and FORMAL[key][3]:
            endpoint='https://api.crossref.org/works/'+FORMAL[key][3]
            r=requests.get(endpoint,timeout=25); r.raise_for_status()
            d=r.json()['message']
            return key,dict(source=endpoint,title=d.get('title'),authors=d.get('author'),year=d.get('published'),container=d.get('container-title'),volume=d.get('volume'),issue=d.get('issue'),pages=d.get('page'),article_number=d.get('article-number'),publisher=d.get('publisher'))
        if 'arxiv.org/abs/' in url:
            r=requests.get(url,timeout=25); r.raise_for_status()
            p=Meta(); p.feed(r.text)
            p.values.pop('citation_abstract',None)
            return key,dict(source=url,metadata=p.values)
        return key,dict(source=url,status='official page previously inspected')
    except Exception as e:
        return key,dict(source=url,error=str(e)[:180])
rows=[]
for line in (ROOT.parent/'papers.md').read_text(encoding='utf-8').splitlines():
    m=re.match(r'\| ([A-Z]\d\d) \| \[.*?\]\((.*?)\)',line)
    if m: rows.append(m.groups())
with ThreadPoolExecutor(max_workers=4) as pool: result=dict(pool.map(fetch,rows))
(ROOT/'source-metadata.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'records':len(result),'errors':{k:v['error'] for k,v in result.items() if 'error' in v}},ensure_ascii=False))
