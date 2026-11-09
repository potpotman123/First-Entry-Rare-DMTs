"""Build the audit and integrated evidence from the supplied 16-page deck.

All deck-derived entries are transcriptions, not authenticated underlying models.
The original first-pass dataset is retained unchanged in data/archive/.
"""
from pathlib import Path
import json
from datetime import date

ROOT=Path(__file__).resolve().parents[1]
deck='sources/user-provided/prior-analysis/1st Entry Rare Tx - Historical Analyst Estimates.pdf'
sources={
 'prior_deck':{'title':'Prior first-entry rare-disease analyst-estimate analysis','repo_path':deck,'pages':16,'type':'user-supplied synthesis with reproduced source excerpts','date':None,'accessed':'2026-11-09','access_note':'Read all substantive pages, including image-based appendix. Underlying AlphaSense links are not clickable in the PDF. Most appendix material is a synthesis; p.8 reproduces a Credit Suisse model-assumption table.'},
 'alexion2020':{'title':'Alexion 2020 Form 10-K, p.92 / Note 18 F-66','url':'https://www.sec.gov/Archives/edgar/data/899866/000089986621000014/alxn-20201231.htm','type':'primary audited filing','accessed':'2026-11-09'},
 'novartis2024':{'title':'Novartis FY2024 results, top-20 brands table','url':'https://www.novartis.com/news/media-releases/novartis-continues-strong-momentum-sales-growth-margin-expansion-reaches-key-innovation-milestones-2024','type':'primary company results','accessed':'2026-11-09'},
 'strensiq_original_label':{'title':'FDA original Strensiq orphan approval record','url':'https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=266608','type':'primary regulatory record','accessed':'2026-11-09'},
 'zolgensma_original':{'title':'FDA Purple Book Zolgensma record','url':'https://www.accessdata.fda.gov/scripts/purplebooksearch/index.cfm?blaNo=125694&event=productdetails','type':'primary regulatory record','accessed':'2026-11-09'},
 'evrysdi_original':{'title':'FDA Evrysdi approval, August 7, 2020','url':'https://www.fda.gov/news-events/press-announcements/fda-approves-oral-treatment-spinal-muscular-atrophy','type':'primary regulatory record','accessed':'2026-11-09'},
 'omav_safety':{'title':'Safety Monitoring of Omaveloxolone in Friedreich Ataxia: Results from One Year of Clinical Treatment','url':'https://pmc.ncbi.nlm.nih.gov/articles/PMC12089633/','type':'original observational clinical research','accessed':'2026-11-09','access_note':'Indexed Table 2 and dosing text recovered; direct PMC/Europe PMC page access challenged. No population-wide persistence inference.'},
 'novartis2025':{'title':'Novartis FY2025 financial report, p.8','url':'https://www.novartis.com/sites/novartis_com/files/q4-2025-interim-financial-report-en.pdf','type':'primary company results','accessed':'2026-11-09','access_note':'Reports Zolgensma Group and discusses intrathecal Itvisma. Do not assume 2025 group revenue is pure original IV-product sales.'}
}

summary=[]
for drug,indication,launch,old,years,actual,new,peak,signal,note in [
 ('Strensiq','HPP',2015,[500,1000],'2012–2014',1700,[2000,2000],2027,'realized sales above displayed range','P.7 also lists BofA $1.6bn dated September 30, 2014; displayed initial range is incomplete or uses unstated selection rules.'),
 ('Crysvita','XLH',2018,[1200,1800],'2016–2018',1600,[2000,3000],2032,'upward revision, not realized out-of-range beat','Later TIO indication admitted; 2025 actual lies inside old range. Worldwide product economics require partner reconciliation.'),
 ('Vyjuvek','DEB',2023,[750,1000],'2023',400,[1700,2000],2033,'upward revision, not realized peak beat','Territorial scope and exact preapproval note dates unknown; within-disease age expansion also flagged.'),
 ('Daybue','Rett',2023,[400,800],'2022–2023',400,[500,900],2032,'within displayed range','Rounded 2025 product sales; future peaks not observed. No appendix of underlying Daybue forecasts.'),
 ('Givlaari','AHP',2019,[500,1500],'2017–2019',300,[600,600],2033,'downward revision relative to high estimates','New $600m estimate is still inside old range. P.11 gives later mechanism commentary, not original sales forecasts.'),
 ('Skyclarys','Friedreich ataxia',2023,[1400,2200],'2022',500,[1000,1500],2033,'downward revision with overlapping ranges','Future peak not observed; alarming persistence anecdotes require cohort/denominator checks.'),
 ('Spinraza','SMA',2016,[1600,3000],'2016 as labeled on p.5',1500,[2100,2100],2019,'observed historical maximum inside displayed range','Lower $1.6bn entry shown in appendix is September 2017, after approval; 2019 value is actual, not current forecast.'),
 ('Zolgensma','SMA',2019,[1400,2800],'2019 as labeled on p.5',1200,[1600,1600],2033,'future revision, fast-follower comparator','Upper $2.8bn appendix entry is August 2019 after approval. IV/IT combined forecasts and excluded $5bn entry complicate scope.'),
 ('Evrysdi','SMA',2020,[2200,3800],'2020',2100,[3200,3200],2032,'within displayed range, fast-follower comparator','Appendix mentions 90% approval probability, mixed currencies and postapproval entries; original models required.')
]:
 summary.append({'product':drug,'indication':indication,'launch_year_as_deck':launch,'prelaunch_peak_range_usdm_as_deck':old,'vintage_as_deck':years,'sales_2025_usdm_as_deck_rounded':actual,'current_peak_range_usdm_as_deck':new,'current_peak_year_as_deck':peak,'page':4 if drug not in ['Spinraza','Zolgensma','Evrysdi'] else 5,'source':'prior_deck','compiler_risk_statement':'not probability adjusted','risk_statement_verified_in_originals':False,'audited_interpretation':signal,'qualification':note,'strict_eligible':False})

est=[]
approval={'Strensiq':'2015-10-23','Spinraza':'2016-12-23','Zolgensma':'2019-05-24','Evrysdi':'2020-08-07'}
def row(drug,broker,dt,value,year,page,notes='',source_date=None,currency='USD',risk='compiler declares unadjusted; original not checked'):
 if dt and len(dt)==10:
  delta=(date.fromisoformat(approval[drug])-date.fromisoformat(dt)).days
  timing='preapproval' if delta>0 else 'postapproval' if delta<0 else 'approval day; timing unresolved'
 else: delta=None;timing='date precision insufficient; see notes'
 est.append({'id':'PD'+str(len(est)+1),'product':drug,'institution':broker,'date_as_deck':dt,'citation_date_as_deck':source_date or dt,'sales_usdm_as_deck':value,'currency_of_displayed_value':currency,'target_year_as_deck':year,'page':page,'approval_date':approval[drug],'days_before_approval':delta,'timing_audit':timing,'risk_treatment':risk,'conditional_sales_usdm':None,'source':'prior_deck','source_quality':'reproduced model table' if page==8 else 'compiler/AlphaSense synthesis; underlying report not supplied','strict_eligible':False,'notes':notes})
row('Strensiq','JPMorgan','2012-04-16',625,None,7,'Assumed pediatric filing in 2014; scope needs original model.')
row('Strensiq','Credit Suisse','2014-09-02',500,2020,7,'Forecast assumes 2015 launch; worldwide scope inferred from main deck table, not authenticated in underlying note.')
row('Strensiq','BofA','2014-09-30',1600,None,7,'P.7 places under a 2015–2016 heading despite 2014 citation; outside p.4 displayed initial range.')
row('Strensiq','Morgan Stanley','2013-10-25',750,None,7)
row('Strensiq','Morgan Stanley','2015-04-23',1200,None,7)
row('Strensiq','Credit Suisse','2016-01-19',1200,2025,8,'Reproduced assumption table; pediatric-only modeled population despite broader label; $500m US/$700m ex-US. Postapproval.')
row('Strensiq','Credit Suisse','2018-01-17',1300,2028,7,'Postapproval revision.')
row('Spinraza','Credit Suisse','2016-01-19',3000,None,14,'A promising primary-vintage original-report retrieval lead; no annual curve reproduced.')
row('Spinraza','JPMorgan','2016-12-27',3000,None,14,'Four days after FDA approval.')
row('Spinraza','Credit Suisse','2017-02-03',2500,None,14,'Postapproval; summary compares peak with a different-year consensus value.')
row('Spinraza','RBC','2017-09-14',1600,None,14,'Postapproval entry appears to supply the lower end of the p.5 pre-launch range.')
row('Spinraza','BofA','2017-10-05',1900,None,14)
row('Spinraza','JPMorgan','2017-11-09',3000,None,14)
row('Spinraza','Credit Suisse','2017-12-20',3200,2025,14)
row('Zolgensma','BofA','2018-04',5000,None,15,'Marked outlier without an explicit inclusion rule; no original source chip visible.',risk='explicitly described as unrisk-adjusted in deck')
row('Zolgensma','Jefferies','2019-04-24',2600,2024,15,'Worldwide peak by 2024 per deck; original route/label coverage needs checking.')
row('Zolgensma','Morgan Stanley','2019-04-10',1400,None,15)
row('Zolgensma','Jefferies','2019-08-30',2800,None,15,'Postapproval upward revision.')
row('Zolgensma','BofA','2019-09-13',2500,2024,15,'Combines $900m IV and $1.6bn IT; not pure original IV product.')
row('Zolgensma','BofA','2020-03-24',2100,None,15,'Combined IV/IT formulation forecast; postapproval.')
row('Zolgensma','Deutsche Bank','2021-01-14',1700,2025,15)
row('Evrysdi','BofA','2020-01-21',2800,2027,16,'35% prevalent-patient penetration per deck.')
row('Evrysdi','BofA','2020-03',2900,2027,16,'Estimate date and source chip conflict.',source_date='2019-09-13')
row('Evrysdi','Bernstein','2020-07-22',2170,None,16,'Described as CHF2bn at 90% probability; transformation and FX date absent. Do not divide by 0.9 without original.',risk='ambiguous: 90% PoS mentioned in appendix despite global unadjusted statement')
row('Evrysdi','Credit Suisse','2020-07-20',3800,2034,16,'Displayed estimate ~$3.8bn; prose says $3.5bn before royalty monetization. Unit/revenue-owner reconciliation required.')
row('Evrysdi','Credit Suisse','2020-08-10',2800,None,16,'After August 7 approval; annual net price $280k mentioned.')
row('Evrysdi','TD Cowen','2021-02',3200,None,16,'Postapproval; day not visible.')

issues=[
 ('A01','high','Forecast versus forecast is not forecast versus actual',[4,5],'Crysvita, Vyjuvek, Givlaari and Skyclarys directions are primarily old-versus-current peak comparisons.','Split realized error, forecast revisions and operational lessons; do not pool them into one beat rate.'),
 ('A02','high','Preapproval ranges contain postapproval estimates',[5,14,15,16],'Spinraza $1.6bn is dated September 2017; Zolgensma $2.8bn is August 2019; Evrysdi includes August 10, 2020.','Rebuild from dated originals before respective approval dates.'),
 ('A03','high','PoS handling is not fully established',[4,5,16],'Deck says unadjusted, but Bernstein Evrysdi row mentions 90% probability.','Retain compiler declaration as evidence; recover exact location of probability in model; do not automatically divide.'),
 ('A04','high','Strensiq initial range omits a cited larger forecast',[4,7],'P.4 gives $0.5–1bn for 2012–2014; p.7 cites BofA September 30, 2014 at $1.6bn.','Document vintage and selection rules; preserve all eligible estimates before aggregation.'),
 ('A05','high','Later disease indication retained',[2,4,9],'Crysvita TIO is included and described as marginal without a numerical allocation.','Exclude mixed XLH/TIO sales from strict sample until separated or bounded; label age expansion separately.'),
 ('A06','high','Geography shifts may change the opportunity rather than reveal error',[4,9,10],'LATAM/EU expansion is called upside without the original geographic scope.','US-only forecasts must be compared with US actuals; add territories only in a separately defined analysis.'),
 ('A07','medium','Population denominators change',[9],'Crysvita table compares 9,000 US adults with 36,000 global adults.','Do not interpret this as a fourfold epidemiology revision.'),
 ('A08','high','SMA route and product scope are mixed',[5,15],'2019 Zolgensma is labeled IT, but approval was IV; some estimates explicitly combine IV/IT.','Separate original Zolgensma from intrathecal franchise expectations; retain fast followers outside first-DMT cohort.'),
 ('A09','medium','SMA revenue-owner reconciliation needed',[13],'Evaluate table has Roche and Chugai Evrysdi rows; 2025 total appears to include both.','Verify end-market conventions before summing. Also distinguish 2025 Zolgensma Group from original IV sales.'),
 ('A10','high','Skyclarys persistence anecdotes lack a generalizable denominator',[12],'48% at six months and up to 75% discontinuation in some practices are cited from surveys/expert summaries.','Recover population, follow-up, dose-reduction definitions and pharmacy coverage; compare with original observational cohorts.'),
 ('A11','medium','Market-size accuracy is not demonstrated by summing product peaks',[5,13],'Forecasts were made in different years with different competitor knowledge.','Use contemporaneous, same-horizon total-SMA forecasts before making a market-accuracy claim.'),
 ('A12','medium','Strensiq age-at-treatment and age-at-onset differ',[7,8],'Adults with pediatric-onset HPP are not equivalent to adult-onset disease; the reproduced model is January 2016.','Use the table as postapproval mechanism evidence, not a preapproval forecast or proof of adult efficacy for CMP-002.'),
 ('A13','medium','Date, currency and value inconsistencies',[16],'March 2020 row cites September 2019; $3.8bn row describes $3.5bn; CHF-to-USD translation is not specified.','Preserve raw entries, quarantine transformations and obtain originals.'),
 ('A14','medium','Universal price-conservatism conclusion is unsupported',[3,4,9],'Daybue and Crysvita descriptions include material pricing surprises; price and adult mix interact.','Decompose net price, body weight, utilization and patient mix within each case.'),
 ('A15','medium','No complete cohort or annual curves',[2,4,5],'Selected products and peak ranges cannot identify a systematic signed three-year error.','Keep the original strict endpoint; add a labeled exploratory single-year comparison track.'),
 ('A16','medium','Causal attribution exceeds the reproduced evidence',[7,9,10,11,12],'Many mechanisms are later syntheses/expert reports, with no quantitative patient-price-revenue bridge.','Treat as hypotheses; seek contemporaneous forecasts and independent patient, access and utilization records.')
]
issues=[dict(id=i,severity=s,title=t,pages=p,observation=o,treatment=a) for i,s,t,p,o,a in issues]

checks=[
 {'id':'C1','product':'Strensiq','forecast_record':'PD2','target_year':2020,'forecast_usdm':500,'actual_usdm':731.8,'error_fraction':731.8/500-1,'actual_source':'alexion2020','status':'exploratory secondary-source single-year comparison','caveats':['Forecast reported by deck, not authenticated original','Worldwide scope inferred from deck heading','Compiler declares unadjusted; original model risk treatment unverified','Not first 36-month cumulative outcome']},
 {'id':'C2','product':'Zolgensma','forecast_record':'PD16','target_year':2024,'forecast_usdm':2600,'actual_usdm':1214,'error_fraction':1214/2600-1,'actual_source':'novartis2024','status':'exploratory fast-follower single-year comparison','caveats':['Underlying Jefferies report not supplied','IV versus future IT scope needs reconciliation','Not first DMT','Not first 36-month cumulative outcome']}
]
audit={'as_of':'2026-11-09','source':'prior_deck','deck_publication_date':None,'review_scope':'16 pages; text plus visual review of all substantive appendix tables','deck_summary':summary,'recovered_estimate_leads':est,'quality_issues':issues,'exploratory_matched_year_checks':checks,'sources':sources,'strict_cumulative_36m_n':0,'strict_cumulative_60m_n':0,'interpretation':'Additional records materially improve the retrieval roadmap and mechanism evidence, but do not establish systematic underforecasting. Conditional status is declared by the compiler, not uniformly authenticated.'}
(ROOT/'data/prior_deck_audit.json').write_text(json.dumps(audit,indent=2))

base=json.loads((ROOT/'data/archive/research_evidence.json').read_text())
base['sources'].update(sources)
manifest=json.loads((ROOT/'sources/source_manifest.json').read_text())
for k,s in base['sources'].items():
 if 'path' in s:
  found=next((r for r in manifest if r['original_path']==s['path']),None)
  if found:s['repo_path']=found['repo_path']
base['prior_deck_audit_file']='data/prior_deck_audit.json'
for pair,year,value,source_key in [('Strensiq / HPP',2020,731.8,'alexion2020'),('Zolgensma / SMA',2024,1214,'novartis2024')]:
 base['actual_sales'].append({'pair':pair,'year':year,'sales_usdm':value,'geography':'worldwide','currency':'USD','revenue_basis':'recognized net product sales','period_convention':'calendar year','scope':'reported product sales; forecast scope must still be checked','source':source_key,'locator':'product sales table','status':'observed'})
base['study_status']='Integrated prior internal deck and eight current CAMP reports. No systematic commercial forecast bias established; strict cumulative sample remains empty. Exploratory point outcomes and forecast revisions are separate.'
base['update_log']=[{'date':'2026-11-09','change':'Integrated prior 16-page deck; added five previously unscreened products; extracted 27 individual estimate leads and 16 audit issues; added two exploratory target-year checks. Original first-pass records retained unchanged in data/archive.'}]
for pair,year,decision,reason in [('Crysvita / XLH',2018,'Mechanism comparator; strict first-DMT status unresolved','Prior conventional treatment and later TIO indication require adjudication/separation.'),('Vyjuvek / DEB',2023,'DMT candidate; early launch and scope flags','Original-label/territory and annual curve needed; higher current peak is a revision.'),('Givlaari / AHP',2019,'Mechanism comparator; first-DMT status unresolved','Earlier disease-directed care; no original preapproval annual model in deck.'),('Zolgensma / SMA',2019,'Fast-follower comparator only','Spinraza precedes it; distinguish original IV from IT expectations.'),('Evrysdi / SMA',2020,'Fast-follower comparator only','Existing SMA DMTs; PoS/currency ambiguities in reproduced estimates.')]:
 base['screened_candidates'].append({'pair':pair,'us_approval_year':year,'group':'added from user prior-analysis deck','decision':decision,'reason':reason,'source':'prior_deck','verification':'deck screened; individual primary adjudication incomplete except regulatory timing checks noted in audit','strict_quantitative_inclusion':False})
base['data_dictionary']['prior_deck_audit']='Compiler-reported estimates and issues are separate from authenticated original broker records. Do not silently merge peak revisions into historical forecast-error results.'
(ROOT/'data/research_evidence.json').write_text(json.dumps(base,indent=2))
assert len(summary)==9 and len(est)==27 and len(base['screened_candidates'])==53
assert all(not r['strict_eligible'] for r in est)
assert len({r['id'] for r in est})==len(est)
print('Integrated 9 deck cases, 27 estimate leads, 16 audit issues; strict cumulative N remains 0.')
