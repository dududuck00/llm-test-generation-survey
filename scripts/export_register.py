"""Export the curated Markdown register without inferring new study attributes."""
from pathlib import Path
import csv
import re

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
    if len(records)!=60 or len(ids)!=len(records) or ids!=bib_ids:
        raise ValueError('Register size, duplicate IDs, or bibliography IDs need review.')
    output=ROOT/'data/papers.csv'
    with output.open('w',encoding='utf-8',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(records[0]))
        writer.writeheader();writer.writerows(records)
    print(f'Exported {len(records)} records with bibliography-matched IDs.')

if __name__=='__main__':main()
