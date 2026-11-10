"""Read FDA source workbook; retain full source rows and a transparent first-pass screen."""
from pathlib import Path
from datetime import datetime
from collections import Counter
import json,re,html
import openpyxl
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data/independent'; OUT.mkdir(parents=True,exist_ok=True)
w=openpyxl.load_workbook(ROOT/'sources/regulatory/fda_cder_1985_2025.xlsx',read_only=True,data_only=True)
s=w.worksheets[0]; rows=list(s.values); headers=[str(x).strip() for x in rows[0]]
onc=re.compile(r'cancer|carcinoma|lymphoma|leukemia|leukaemia|myeloma|sarcoma|melanoma|neuroblastoma|glioblastoma|glioma|myelodysplastic|myelofibrosis|myeloproliferative|polycythemia vera|gastrointestinal stromal|mesothelioma|neoplasm|tumou?r',re.I)
records=[]
for i,row in enumerate(rows[1:],2):
 if not row[0]: continue
 d={k:(v.isoformat()[:10] if isinstance(v,datetime) else v) for k,v in zip(headers,row)}
 d['frame_id']=f'CDER-{i}'; d['source_locator']=f'2025 Compilation!A{i}:AA{i}'
 year=d['Approval Year']; indication=d.get('Abbreviated Indication(s)') or d.get('Approved Use(s)') or ''
 d['indication_at_approval']=indication
 if not isinstance(year,(int,float)) or year<2000 or year>2025: reason='outside_primary_period'
 elif not str(d['Orphan Drug Designation']).lower().startswith('yes'): reason='not_orphan_designated_at_original_approval'
 elif onc.search(indication): reason='oncology_or_tumor_candidate_review'
 else: reason='nononcology_orphan_review'
 d['initial_screen']=reason; records.append(d)
(OUT/'cder_full_frame.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Frame',len(records),'Screen counts',dict(Counter(x['initial_screen'] for x in records)))
for d in records:
 if d['initial_screen']=='nononcology_orphan_review':
  print(d['frame_id'],d['FDA Approval Date'],d['Proprietary  Name'], '|',d['indication_at_approval'])
raw=(ROOT/'sources/regulatory/fda_cell_gene_2026-11-09.html').read_text()
tables=re.findall(r'<table\b.*?</table>',raw,re.S|re.I)
print('CBER tables',len(tables))
for t in tables:
 print(re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]*>',' ',t))))
