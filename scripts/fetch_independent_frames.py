"""Download three public regulatory frames once; not a crawler."""
from pathlib import Path
import urllib.request, urllib.parse, json, hashlib, datetime

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'sources/regulatory'
DEST.mkdir(parents=True, exist_ok=True)
params = {'Product_name':'','sponsor_name':'','Designation':'',
 'Designation_Start_Date':'01/01/1983','Designation_End_Date':'11/09/2026',
 'Search_param':'EXCSTART','Output_Format':'Detailed','Sort_order':'Date_Order',
 'RecordsPerPage':'2000','newSearch':'Run Search'}
items = [
 ('fda_cder_1985_2025.xlsx','https://www.fda.gov/media/177921/download?attachment=',None),
 ('fda_orphan_approved_2026-11-09.html','https://www.accessdata.fda.gov/scripts/opdlisting/oopd/OOPD_Results.cfm',urllib.parse.urlencode(params).encode()),
 ('fda_cell_gene_2026-11-09.html','https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/approved-cellular-and-gene-therapy-products',None)]
manifest=[]
for name,url,data in items:
 try:
  p=DEST/name
  if not p.exists():
   req=urllib.request.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0'})
   with urllib.request.urlopen(req,timeout=45) as r:
    blob=r.read(); content_type=r.headers.get('Content-Type'); p.write_bytes(blob)
  else: blob=p.read_bytes(); content_type='cached'
  item={'file':str(p.relative_to(ROOT)),'url':url,'post_parameters':params if data else None,'retrieved':'2026-11-09','bytes':len(blob),'sha256':hashlib.sha256(blob).hexdigest(),'content_type':content_type}
  if data is not None:
   # This request was not a successful result export. Do not silently promote
   # a new server response to a validated census on a later rerun.
   item['used_for_universe']=False
   item['access_status']='FAILED: server returned search form, not approval result export' if b'Run Search' in blob else 'UNVALIDATED: manual result-format verification required'
  else:item['used_for_universe']=True
  manifest.append(item); print(name,len(blob),content_type)
 except Exception as e:
  manifest.append({'file':name,'url':url,'error':str(e),'retrieved':'2026-11-09'}); print(name,type(e).__name__,str(e))
(DEST/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
