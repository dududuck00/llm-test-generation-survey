"""Export the curated Markdown register without inferring new study attributes."""
from pathlib import Path
import csv
import re
import json

ROOT=Path(__file__).resolve().parents[1]

def main():
    records=[];category=''
    for line in (ROOT/'papers.md').read_text(encoding='utf-8').splitlines():
        if line.startswith('## '):category=line[3:]
        if not re.match(r'\| [SUROAFTBEG]\d\d \|',line):continue
        cells=[cell.strip() for cell in line.strip().strip('|').split('|')]
        title=re.fullmatch(r'\[(.*?)\]\((https?://.*?)\)',cells[1])
        if title is None:raise ValueError(f'Invalid linked title: {cells[0]}')
        tail=cells[4:]
        mechanism,analysis,depth=('',tail[0],tail[1]) if len(tail)==2 else tuple(tail)
        records.append(dict(id=cells[0],category=category,title=title[1],source_url=title[2],
                            year_status=cells[2],study_type=cells[3],mechanism=mechanism,
                            analysis_note=analysis,inspection_depth=depth))
    ids={row['id'] for row in records}
    bib_ids=set(re.findall(r'@\w+\{([A-Z]\d{2}),',(ROOT/'manuscript/references.bib').read_text(encoding='utf-8')))
    supplement=json.loads((ROOT/'supplemental-search.json').read_text(encoding='utf-8'))['records']
    supplemental_ids={row['id'] for row in supplement}
    extra_bib_ids=set(re.findall(r'@\w+\{([A-Z]\d{2}),',(ROOT/'supplemental-references.bib').read_text(encoding='utf-8')))
    if (len(ids)!=len(records) or len(supplemental_ids)!=len(supplement)
            or bib_ids & extra_bib_ids or ids!=bib_ids|extra_bib_ids
            or supplemental_ids!=extra_bib_ids):
        raise ValueError('Duplicate IDs or register/bibliography/provenance IDs need review.')
    titles=[re.sub(r'[^a-z0-9]','',row['title'].lower()) for row in records]
    if len(set(titles))!=len(titles):
        raise ValueError('Duplicate normalized titles need study-family review.')
    output=ROOT/'data/papers.csv'
    output.parent.mkdir(exist_ok=True)
    with output.open('w',encoding='utf-8',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(records[0]))
        writer.writeheader();writer.writerows(records)
    print(f'Exported {len(records)} unique records: {len(bib_ids)} manuscript bibliography IDs and {len(extra_bib_ids)} supplemental candidates.')

if __name__=='__main__':main()
