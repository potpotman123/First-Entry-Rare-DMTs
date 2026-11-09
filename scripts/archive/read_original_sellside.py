from pathlib import Path
import json
import pdfplumber
from pypdf import PdfReader
root=Path('/Users/kwu/Downloads')
out=Path('work/sellside'); out.mkdir(exist_ok=True)
manifest=[]
for f in sorted(root.glob('*CAMP.OQ*.pdf')):
    reader=PdfReader(f)
    plumber=pdfplumber.open(f)
    pages=[]
    for i,p in enumerate(reader.pages):
        try: pages.append(p.extract_text(extraction_mode='layout') or '')
        except (TypeError, ValueError): pages.append(plumber.pages[i].extract_text(layout=True) or '')
    plumber.close()
    dest=out/(f.stem+'.txt')
    dest.write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+p for i,p in enumerate(pages)))
    manifest.append({'file':str(f),'pages':len(pages),'text_file':str(dest)})
    print(f.name, len(pages), 'pages',sum(map(len,pages)), 'characters')
(out/'manifest.json').write_text(json.dumps(manifest,indent=2))
