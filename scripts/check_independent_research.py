"""Meaningful provenance, arithmetic and eligibility checks for the research artifact."""
from pathlib import Path
from collections import Counter
from datetime import date
from html.parser import HTMLParser
import hashlib,json,math,re,csv
R=Path(__file__).resolve().parents[1];D=R/'data/independent'
e=json.loads((D/'evidence.json').read_text());f=json.loads((D/'approval_screen.json').read_text());c=json.loads((D/'candidate_universe.json').read_text())
checks=[]
def check(name,ok):
 assert ok,name
 checks.append(name)
check('all retrieved frame IDs unique',len(f)==len({x['id'] for x in f})==1442)
check('CDER and CBER counts',sum(x['id'].startswith('CDER') for x in f)==1387 and sum(x['id'].startswith('CBER') for x in f)==55)
check('all rows retain reason and status; no unexplained pending rows',all(x.get('reason') and x.get('classification_status') and x['classification'] not in ['unresolved_screen','cber_review_pending'] for x in f))
check('extended candidate counts reconcile',len(c)==99 and len([x for x in c if x['classification'] not in ['historical_extension','outside_primary_period_2026']])==82)
primary=[x for x in f if x['id'].startswith('CDER') and '2000-01-01'<=x['us_approval_date']<='2025-12-31']
check('primary original approval counts',len(primary)==924 and sum(str(x['orphan_status']).startswith('Yes') for x in primary)==380)
check('scope category counts reconcile',dict(Counter(x['classification'] for x in f))==e['frame_counts'])
check('twenty unique case dossiers',len(e['cases'])==len({x['product'] for x in e['cases']})==20)
check('all case source IDs exist',all(s in e['sources'] for x in e['cases'] for s in x['sources']))
for filename,n in [('forecast_actuals.csv',5),('analogue_matrix.csv',20),('approval_screen.csv',1442)]:
 with (D/filename).open(newline='') as fh: rows=list(csv.DictReader(fh))
 check(filename+' export row count',len(rows)==n)
check('five new comparisons, three original-publication rows',len(e['new_target_year_comparisons'])==5 and sum(x['forecast_source']=='werber04' for x in e['new_target_year_comparisons'])==3)
for p in e['new_target_year_comparisons']:
 check(p['product']+' arithmetic',math.isclose(p['raw_actual_over_forecast_minus_1'],p['actual_usdm']/p['forecast_usdm']-1,abs_tol=1e-12))
 check(p['product']+' preapproval vintage',p['forecast_date']<p['approval_date'])
 check(p['product']+' unknown PoS not imputed',p['pos'] is None and p['conditional_sales_usdm'] is None)
 check(p['product']+' strict eligibility excluded',not p['strict_36m_eligible'] and not p['strict_60m_eligible'] and len(p['exclusion_reasons'])>=4)
 check(p['product']+' target after approval',p['target_year']>=int(p['approval_date'][:4]))
 if p['break_even_scalar_pos'] is not None:check(p['product']+' PoS threshold recomputed',math.isclose(p['break_even_scalar_pos'],p['forecast_usdm']/p['actual_usdm']))
check('all original source-table rows preserved',len(e['complete_werber_table'])==8 and sum(x['preapproval_at_publication'] for x in e['complete_werber_table'])==3)
check('no pooled or cumulative result invented',e['strict_36m_N']==e['strict_60m_N']==0 and e['pooled_bias_estimate'] is None and e['pooled_beat_rate'] is None)
for name,h in e['protocol_sha256'].items():check('protocol hash '+name,hashlib.sha256((R/'protocol'/name).read_bytes()).hexdigest()==h)
manifest=json.loads((R/'sources/regulatory/manifest.json').read_text())
for x in manifest:check('regulatory source hash '+x['file'],hashlib.sha256((R/x['file']).read_bytes()).hexdigest()==x['sha256'])
check('failed OOPD retrieval not used',manifest[1]['used_for_universe'] is False and manifest[1]['access_status'].startswith('FAILED'))
check('source originals exist',all(not x['local_file'] or (R/x['local_file']).exists() for x in e['sources'].values()))
class Links(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.hrefs=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
  if t=='a':self.hrefs.append(d.get('href',''))
p=Links();p.feed((R/'reports/independent_research.html').read_text())
check('report internal anchors resolve',all(x[1:] in p.ids for x in p.hrefs if x.startswith('#')))
check('report has no duplicate IDs',len(p.ids)==len(set(p.ids)))
check('all repository report links resolve except generated validation',all((R/x.split('/blob/main/',1)[1]).exists() or x.endswith('data/independent/validation.json') for x in p.hrefs if '/blob/main/' in x))
v=dict(as_of=e['as_of'],checks_passed=len(checks),checks=checks,frame_counts=e['frame_counts'],candidate_N=len(c),primary_candidate_control_N=82,new_comparisons=[{k:x[k] for k in ['product','forecast_usdm','actual_usdm','raw_actual_over_forecast_minus_1','break_even_scalar_pos']} for x in e['new_target_year_comparisons']],strict_36m_N=0,strict_60m_N=0,limitations='Internal arithmetic/provenance consistency, not independent validation of forecast scope or causal mechanisms.')
(D/'validation.json').write_text(json.dumps(v,indent=2)+'\n');print(f'{len(checks)} checks passed; no normalized pooled result claimed.')
