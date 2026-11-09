"""Check source integrity, evidence links, dates and arithmetic. No network."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from datetime import date
import hashlib,json

root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'sources/source_manifest.json').read_text())
for r in manifest:
    p=root/r['repo_path']
    assert p.is_file(), p
    assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],p
assert sum(r['repo_path'].endswith('.pdf') for r in manifest)==9

d=json.loads((root/'data/research_evidence.json').read_text())
a=json.loads((root/'data/prior_deck_audit.json').read_text())
c=json.loads((root/'data/calculation_results.json').read_text())
assert len(d['screened_candidates'])==53
assert len(a['deck_summary'])==9
assert len(a['recovered_estimate_leads'])==27
assert len(a['quality_issues'])==16
assert c['strict_primary_drug_indication_n']==0
assert c['strict_36_month_bias'] is None and c['strict_60_month_bias'] is None
assert all(not x['strict_eligible'] for x in a['recovered_estimate_leads'])
for r in a['recovered_estimate_leads']:
    if r['date_as_deck'] and len(r['date_as_deck'])==10:
        delta=(date.fromisoformat(r['approval_date'])-date.fromisoformat(r['date_as_deck'])).days
        assert delta==r['days_before_approval']
        if delta<0:assert r['timing_audit']=='postapproval'
for r in d['actual_sales']+d['historical_forecasts']+d['screened_candidates']:
    assert r['source'] in d['sources']
for r in a['exploratory_matched_year_checks']:
    lead=next(x for x in a['recovered_estimate_leads'] if x['id']==r['forecast_record'])
    assert lead['sales_usdm_as_deck']==r['forecast_usdm']
    assert lead['target_year_as_deck']==r['target_year']
    assert abs(r['actual_usdm']/r['forecast_usdm']-1-r['error_fraction'])<1e-12

class Links(HTMLParser):
    def __init__(self):super().__init__();self.hrefs=[];self.ids=set()
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='a':self.hrefs.append(attrs.get('href',''))
        if 'id' in attrs:self.ids.add(attrs['id'])

for p in [root/'reports/current_assessment.html',root/'reports/archive/initial_research_brief.html']:
    parser=Links();s=p.read_text();parser.feed(s)
    assert s.count('<table>')==s.count('</table>')
    for href in parser.hrefs:
        u=urlsplit(href)
        if u.scheme:continue
        if not u.path:
            if u.fragment:assert u.fragment in parser.ids
            continue
        target=p.parent/unquote(u.path)
        assert target.is_file(),(p,href)
assert hashlib.sha256((root/'protocol/study_protocol_v1.txt').read_bytes()).hexdigest()==d['protocol_sha256']
print('Verified: 11 unchanged source documents, 9 PDFs, 53 screened entries, 27 estimate leads, source/date integrity, arithmetic, local report links and unchanged frozen protocol.')
