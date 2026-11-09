from pathlib import Path
import json, html, re, hashlib

ROOT=Path('/Users/kwu/Documents/Codex/2026-11-09/two-separate-projects-1-build-an')
OUT=ROOT/'outputs'
OUT.mkdir(exist_ok=True)
S={}
def source(key,title,url,kind='primary',note=''):
    S[key]={'title':title,'url':url,'type':kind,'access_note':note,'accessed':'2026-11-09'}
source('camp_update','CAMP4 Q3 2026 update, November 5, 2026','https://investors.camp4tx.com/news-releases/news-release-details/camp4-reports-third-quarter-2026-financial-results-and-corporate')
source('camp_8k','CAMP4 September 28, 2026 Form 8-K, Item 8.01','https://www.sec.gov/Archives/edgar/data/1736730/000162828026063740/camp-20260928.htm')
source('camp_10q','CAMP4 September 30, 2026 Form 10-Q, equity statement and Notes 7 and 11','https://investors.camp4tx.com/node/8336/html')
source('syngap_census','Original SYNGAP1 patient-census and incidence research','https://pmc.ncbi.nlm.nih.gov/articles/PMC11726535/','original research','Census cutoff March 31, 2024; not a current 2026 patient count.')
source('chop','CHOP: SYNGAP1-related disorders','https://www.chop.edu/conditions-diseases/syngap1-related-disorders','clinical institution')
source('stoke','Stoke Q2 2026 update, August 3, 2026','https://stoketherapeutics.gcs-web.com/news-releases/news-release-details/stoke-therapeutics-announces-second-quarter-2026-financial')
source('fda_arc','FDA rare-disease drug approval index','https://www.fda.gov/about-fda/accelerating-rare-disease-cures-arc-program/rare-disease-drug-approvals','regulator','Selected approvals, not a complete orphan-drug census.')
source('fda_orphan','FDA orphan designations and approvals database','https://www.accessdata.fda.gov/scripts/opdlisting/oopd/index.cfm','regulator','Access route identified; no full database export reconciled in this study.')
source('ert_fda','FDA-authored clinical-pharmacology paper on ERT development','https://pmc.ncbi.nlm.nih.gov/articles/PMC11998121/','original regulatory research','Indexed table used as screening source; direct page returned a browser challenge.')
source('ert_review','Lysosomal enzyme-replacement approval review table','https://pmc.ncbi.nlm.nih.gov/articles/PMC12743805/','secondary scientific review','Screening seed only; US and EU approval dates must not be conflated.')
source('spin_approval','Biogen: FDA approval of Spinraza, December 23, 2016','https://investors.biogen.com/node/16026')
source('spin_label','Spinraza prescribing information','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=dd70cd5f-b0fc-4ba4-a5ea-89a34778bd94','regulatory label','Current label used for delivery context, not to backdate later dosing changes.')
source('spin_forecast','Needham forecast quoted August 1, 2016 by StreetInsider','https://www.streetinsider.com/Analyst%2BPT%2BChange/Ionis%2BPharmaceuticals%2B%28IONS%29%2BPT%2BRaised%2Bto%2B%2464%2Bat%2BNeedham%2B%26%2BCompany%2Bas%2BENDEAR%2BStudy%2BHalted%2BEarly%2Bfor%2BEfficacy/11885526.html','contemporaneous analyst quotation','Indexed quotation retrieved; direct page unavailable. Original broker model not obtained.')
source('biogen22','Biogen 2022 Form 10-K, Spinraza revenues','https://www.sec.gov/Archives/edgar/data/875045/000087504523000009/biib-20221231.htm')
source('spin_quarter','BioWorld: Biogen second-quarter 2017 earnings','https://www.bioworld.com/articles/392405-biogen-sails-to-strong-2nd-quarter-on-winds-of-sma-drug-sales','financial reporting','Postapproval quarterly consensus; excluded from preapproval comparisons.')
source('spin_claims','Prime Therapeutics AMCP 2019 Spinraza claims poster','https://pharmacy.primetherapeutics.com/content/dam/corporate/Documents/Newsroom/Pressreleases/2019/amcp-posters/news-amcp-2019-spinraza.pdf','original payer research','Small commercially insured sample; poster approval-date error is not adopted.')
source('brin17','BioMarin 2017 Form 10-K','https://www.sec.gov/Archives/edgar/data/1048477/000156459018003114/bmrn-10k_20171231.htm')
source('brin19','BioMarin 2019 Form 10-K, product revenues','https://www.sec.gov/Archives/edgar/data/1048477/000104847720000009/bmrn-20191231.htm')
source('brin21','BioMarin 2021 Form 10-K, product revenues','https://www.sec.gov/Archives/edgar/data/1048477/000104847722000012/bmrn-20211231.htm')
source('brin_label','Brineura FDA label, 2024','https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/761052s016lbl.pdf','regulatory label','Delivery context; launch-age restrictions taken from 2017 filing, not this expanded label.')
source('day_fda','FDA: first treatment for Rett syndrome','https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-treatment-rett-syndrome','regulator')
source('day_label','Daybue original FDA label, 2023','https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/217026s000lbl.pdf','regulatory label')
source('day_forecast','Reuters March 10, 2023 report quoting preapproval SMBC and RBC notes','https://mix929.com/2023/03/10/u-s-fda-approves-acadias-genetic-rett-syndrome-drug/','contemporaneous analyst quotation','Syndicated indexed text; exact dates of underlying notes and PoS not recovered.')
source('day25','Acadia full-year 2025 results','https://acadia.com/en-us/media/news-releases/acadia-pharmaceuticals-reports-fourth-quarter-and-full-year-2025-financial-results-and-operating-overview')
source('day24','Acadia full-year 2024 results','https://acadia.com/en-us/media/news-releases/acadia-pharmaceuticals-reports-fourth-quarter-and-full-year-2024')
source('kaly_label','FDA orphan approval history for ivacaftor','https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=228306','regulator')
source('kaly_forecast','AP, May 15, 2012: JPMorgan Kalydeco forecast','https://www.drugdiscoverytrends.com/vertex-forecast-promising/','contemporaneous analyst quotation','Postapproval; not eligible preapproval evidence.')
source('vrtx15','Vertex 2015 Form 10-K','https://www.sec.gov/Archives/edgar/data/875320/000087532016000067/a201510k-main.htm')
source('vrtx16','Vertex 2016 Form 10-K','https://www.sec.gov/Archives/edgar/data/875320/000087532017000017/a201610k-main.htm')
source('str_label','Strensiq prescribing information','https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=3387574f-5eaa-4501-a71d-4cbfbd563031','regulatory label')
source('str_forecast','FirstWord September 2, 2015, citing Bloomberg analyst estimates','https://firstwordpharma.com/story/3014546','contemporaneous secondary forecast','Geography, consensus composition and PoS unresolved. Article also misattributes acquisition history; original Bloomberg source not recovered.')
source('alxn18','Alexion 2018 Form 10-K geographic product-sales table','https://www.sec.gov/Archives/edgar/data/899866/000089986619000010/R26.htm')
source('alxn_peak','JPMorgan July 27, 2015 peak forecasts quoted by Benzinga','https://www.benzinga.com/analyst-ratings/analyst-color/15/07/5705028/jp-morgan-moves-alexion-pharma-to-overweight-says-strens','contemporaneous analyst quotation','Peak year undisclosed; not annual forecast evidence.')
source('on_forecast','Clarivate Drugs to Watch 2018, methodology p.7 and patisiran p.23','https://kinampark.com/DDS/files/Drugs%20to%20Watch%202018.pdf','original forecast publication hosted by third party','Cortellis forecast; not established as pure sell-side consensus. Text retrieved; web screenshot failed.')
source('alny18','Alnylam 2018 Form 10-K','https://www.sec.gov/Archives/edgar/data/1178670/000156459019003022/alny-10k_20181231.htm')
source('alny22','Alnylam 2022 Form 10-K','https://www.sec.gov/Archives/edgar/data/1178670/000117867023000005/alny-20221231.htm')
source('sky_fda','FDA Skysona 2022 regulatory review','https://www.fda.gov/media/162098/download','regulator','Documents prior allogeneic transplantation; first gene therapy is not first available DMT.')
source('blue24','Bluebird 2024 annual report, financial statements F-20','https://www.publicnow.com/view/674D88DD30443E461D8CA9ABE94FE585420CBB37','primary issuer document mirror','Product revenues and recognition at infusion; not cell-collection guidance.')
source('lux_fda','FDA Luxturna approval record','https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/luxturna','regulator')
source('zok_fda','FDA November 20, 2020 Zokinvy approval bulletin','https://content.govdelivery.com/accounts/USFDA/bulletins/2ada181/','regulator')
source('nul_fda','FDA 2021 new-drug approval report','https://www.fda.gov/media/155227/download?attachment=','regulator')
source('ox_label','Oxlumo label','https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=16985a31-f5e4-4557-9266-fc78d4bc5055','regulatory label')
source('mep_approval','Ultragenyx first MPS VII approval announcement, November 15, 2017','https://www.sec.gov/Archives/edgar/data/1515673/000156459017023875/rare-ex991_6.htm')
source('deloitte','Deloitte 2020 launch-performance study','https://www.deloitte.com/us/en/insights/industry/life-sciences/successful-drug-launch-strategy.html','original commercial research')
source('ispor','Deloitte ISPOR 2024 launch-performance abstract','https://www.ispor.org/heor-resources/presentations-database/presentation/intl2024-3896/136368','original research abstract')
source('mck','McKinsey 2024 first-time-launcher analysis','https://www.mckinsey.com/industries/life-sciences/our-insights/small-but-mighty-priming-biotech-first-time-launchers-to-compete-with-established-players','original commercial research')
source('illicki','Ilicki and Spicer 2026 abstract on rare-disease launch beliefs','https://www.sciencedirect.com/science/article/pii/S1359644626001972','original research abstract','Full text inaccessible; survey of expectations is not a broker-forecast error panel.')
source('zs','ZS emerging-biopharma first-launch analysis','https://www.zs.com/insights/us-emerging-pharma-biotech-first-launch-analysis','original commercial research')

manifest=json.loads((ROOT/'work/sellside/manifest.json').read_text())
keys=['leerink_sep','piper','leerink_oct','needham','oppenheimer','jpmorgan','blair','wedbush']
for k,m in zip(keys,manifest):
    S[k]={'title':Path(m['file']).stem,'path':m['file'],'type':'user-supplied original sell-side report','pages':m['pages'],'sha256':hashlib.sha256(Path(m['file']).read_bytes()).hexdigest(),'accessed':'2026-11-09','access_note':'Text extracted; critical Needham pp.26–29, Piper p.2 and Blair p.4 tables visually checked.'}

brokers=[
 {'broker':'Leerink Partners','date':'2026-09-28; 2026-10-12','rating':'Outperform','target_usd':14,'method':'SOTP cash flows into early 2040s; 12% discount rate. October report assigns no explicit value to CMP-001 BD or other platform opportunities.','sales_pos':'No auditable conditional annual sales curve or PoS disclosed in these notes.','pages':'September pp.1–3,12; October pp.16–17','sources':['leerink_sep','leerink_oct']},
 {'broker':'Piper Sandler','date':'2026-09-28','rating':'Overweight','target_usd':15,'method':'Projected EV $1.26bn plus mid-2027 estimated cash.','sales_pos':'No explicit conditional sales/PoS bridge. P.2 is an image-based earnings model dated August 13, 2026.','pages':'pp.1–2','sources':['piper']},
 {'broker':'Needham','date':'2026-10-15','rating':'Buy','target_usd':8,'method':'50% DCF / 50% EV-to-peak-sales; 9% discount rate; 0% terminal growth; 7x peak-sales multiple; 98m diluted shares.','sales_pos':'Conditional WW peak $2.106bn in 2046; 25% PoS applied separately in valuation.','pages':'pp.25–29,31','sources':['needham']},
 {'broker':'Oppenheimer','date':'2026-10-27','rating':'Outperform','target_usd':15,'method':'DCF: 12% discount rate, 2% terminal growth; described terminal FCF value $3.5bn in 2036.','sales_pos':'Do not interpret terminal FCF value as annual revenue or assume undisclosed PoS.','pages':'pp.1,3','sources':['oppenheimer']},
 {'broker':'JPMorgan','date':'2026-11-05','rating':'Overweight','target_usd':None,'method':'Quick take describes shares as undervalued on probability-adjusted CMP-002 potential.','sales_pos':'No current target/model on first page; rating history p.2 last lists $9 on June 16, 2026. That historical entry is not a fresh model update.','pages':'pp.1–2','sources':['jpmorgan']},
 {'broker':'William Blair','date':'2026-11-05','rating':'Outperform','target_usd':None,'method':'Relative peer valuation and platform thesis; no numerical price target in supplied note.','sales_pos':'2030 product revenue $53.939m: UCD $51.866m and SYNGAP $2.073m. Risk treatment not disclosed. Do not attribute total revenue to CMP-002.','pages':'pp.1,3–4','sources':['blair']},
 {'broker':'Wedbush','date':'2026-11-06','rating':'Outperform','target_usd':8,'method':'Discounted earnings and clinical NPV: 25x P/E, 25% discount rate; DCF: 12% WACC, 0% terminal growth.','sales_pos':'25% discount rate is not disclosed clinical PoS. No conditional sales bridge.','pages':'pp.1,3','sources':['wedbush']}
]
us=[37,95,231,484,730,938,1073,1217,1369,1417,1467,1519,1572,1627,1685,872,451,234,121,63,32,17]
ww=[37,118,289,605,912,1173,1342,1521,1712,1772,1834,1899,1965,2034,2106,1090,564,292,151,78,40,21]
rows=[{'year':y,'us_usdm':u,'worldwide_usdm':w,'status':'observed forecast, rounded as printed','conditional_on_approval':True,'source':'needham','page':26} for y,u,w in zip(range(2032,2054),us,ww)]
va=[{'year':y,'as_reported_usdm':v,'source':'needham','page':26,'status':'observed chart label of reproduced consensus; underlying composition and PoS unknown'} for y,v in zip(range(2032,2041),[148,353,577,754,1074,1272,1444,1587,1716])]

forecasts=[]
def forecast(id,pair,institution,date,target_year,value,geography,source_key,exclusions,operator='=',basis='unknown',note=''):
    forecasts.append(dict(id=id,pair=pair,institution=institution,report_date=date,target_year=target_year,original_sales_usdm=value,operator=operator,geography=geography,currency='USD',revenue_basis='annual product sales, as reported',risk_treatment=basis,pos=None,conditional_sales_usdm=None,source=source_key,strict_eligible=False,exclusion_reasons=exclusions,notes=note))
forecast('F1','Spinraza / SMA','Needham, Chad Messer','2016-08-01',2022,5000,'worldwide','spin_forecast',['PoS unknown','Outside 9–15-month primary vintage','No 36-month curve'],'>','unknown','After positive ENDEAR interim result. Forecast is greater than $5bn, not exactly $5bn.')
forecast('F2','Strensiq / HPP','Unspecified analysts cited by Bloomberg / FirstWord','2015-09-02',2018,355,'unknown','str_forecast',['PoS unknown','Geography unknown','No annual curve','Original report missing','Outside primary vintage'])
forecast('F3','Strensiq / HPP','JPMorgan','2015-07-27',None,1000,'unknown','alxn_peak',['Peak year unknown','PoS unknown','No annual curve'],'>')
forecast('F4','Kanuma / LAL deficiency','JPMorgan','2015-07-27',None,700,'unknown','alxn_peak',['Peak year unknown','PoS unknown','No annual curve'],'>')
for y,v in [(2018,83),(2019,373),(2022,1212)]:
    forecast('F5_'+str(y),'Onpattro / hATTR polyneuropathy','Clarivate Cortellis','2018-03',y,v,'US and Europe launches discussed; forecast geography not fully enumerated','on_forecast',['PoS unknown','Not established pure sell-side consensus','Future indication scope unresolved','No complete 36-month curve','Outside primary vintage'],note='Original publication p.23; sales owner and inclusion of cardiomyopathy require underlying model.')
forecast('F6','Daybue / Rett','SMBC Nikko, David Hoang',None,2035,487.2,'US','day_forecast',['Exact note date missing; described as preapproval','PoS unknown','Peak horizon not elapsed','No annual curve'],note='Quotation published March 10, 2023.')
forecast('F7','Daybue / Rett','RBC, Gregory Renza',None,2032,500,'US','day_forecast',['Exact note date missing; described as preapproval','PoS unknown','Peak horizon not elapsed','No annual curve'],'>',note='Quotation published March 10, 2023.')
forecast('F8','Kalydeco / CF','JPMorgan, Geoff Meacham','2012-05-15',2015,982,'unknown','kaly_forecast',['Postapproval','PoS unknown','Original-genotype actual sales inseparable','No annual curve'],note='Excluded control record; not evidence of preapproval bias.')

actuals=[]
def actual(pair,year,value,geo,src,scope='original disease; product-level reported sales',loc='product revenue table'):
    actuals.append(dict(pair=pair,year=year,sales_usdm=value,geography=geo,currency='USD',revenue_basis='recognized net product sales',period_convention='calendar year',scope=scope,source=src,locator=loc,status='observed'))
actual('Spinraza / SMA',2022,1793.5,'worldwide','biogen22')
for y,u,w in [(2016,177.5,209.4),(2017,280.1,339.8),(2018,374.3,475.1)]:
    actual('Strensiq / HPP',y,u,'US','alxn18');actual('Strensiq / HPP',y,w,'worldwide','alxn18')
for y,v in [(2016,29.1),(2017,65.6),(2018,92.0)]:actual('Kanuma / LAL deficiency',y,v,'worldwide','alxn18')
actual('Onpattro / hATTR polyneuropathy',2018,12.5,'worldwide','alny18')
actual('Onpattro / hATTR polyneuropathy',2022,558,'worldwide','alny22')
for y,v,src in [(2017,8.6,'brin17'),(2018,39.9,'brin19'),(2019,72.0,'brin19'),(2020,110.192,'brin21'),(2021,128.034,'brin21')]:actual('Brineura / CLN2',y,v,'worldwide',src)
for y,v,src in [(2023,177.2,'day24'),(2024,348.4,'day24'),(2025,391.4,'day25')]:actual('Daybue / Rett',y,v,'total reported product revenue; not assumed US-only',src)
for y,v in [(2013,371.285),(2014,463.750),(2015,631.674)]:actual('Kalydeco / CF',y,v,'worldwide','vrtx15','Mixed genotypes/ages; later within-disease expansions cannot be removed')
for pair,vals in [('Skysona / CALD',[(2023,12.373),(2024,9.917)]),('Zynteglo / beta-thalassemia',[(2023,16.692),(2024,62.273)])]:
    for y,v in vals:actual(pair,y,v,'US','blue24',loc='F-20; revenue recognized at infusion')

ledger=[]
def candidate(pair,year,group,decision,reason,src,verification='screened; full launch-era DMT adjudication pending'):
    ledger.append(dict(pair=pair,us_approval_year=year,group=group,decision=decision,reason=reason,source=src,verification=verification,strict_quantitative_inclusion=False))
candidate('Spinraza / SMA',2016,'genetic neurological','Priority DMT analogue','No eligible annual preapproval series recovered.','spin_approval','Launch approval and mechanism checked')
candidate('Brineura / CLN2',2017,'genetic neurological','Priority DMT analogue','Forecast unavailable; CNS delivery and age-window relevance.','brin17','Launch approval checked')
candidate('Daybue / Rett',2023,'neurodevelopmental','Adjacent cohort','Disease-specific benefit; durable disease modification not established by launch evidence.','day_fda','Launch FDA summary and original label checked')
candidate('Kalydeco / G551D CF',2012,'genotype defined','Priority DMT analogue','Later genotypes contaminate aggregate sales; recovered forecast is postapproval.','kaly_label','Original approval and expansion dates checked')
candidate('Strensiq / HPP',2015,'metabolic','Priority DMT analogue','Preapproval point forecast; geography and risk unresolved.','str_label','Label checked')
candidate('Onpattro / hATTR polyneuropathy',2018,'RNA / neurological','Ambiguous first-DMT cohort','Prior transplant; territorial treatment differences; forecast scope unresolved.','alny18','Primary filing checked; strict first-status needs adjudication')
candidate('Skysona / CALD',2022,'genetic neurological','Delivery comparator only','Prior allogeneic transplant; no preapproval revenue curve.','sky_fda','FDA launch review checked')
candidate('Zynteglo / beta-thalassemia',2022,'hematologic / gene therapy','Delivery comparator only','Prior transplantation; no preapproval revenue curve.','blue24','Primary issuer annual report checked')
for pair,y,why in [('Fabrazyme / Fabry',2003,'First US ERT; earlier EU treatment matters.'),('Aldurazyme / MPS I',2003,'Prior transplantation complicates first-ever DMT status.'),('Naglazyme / MPS VI',2005,'Prior transplantation needs adjudication.'),('Elaprase / MPS II',2006,'Somatic benefit cannot stand in for CNS rescue.'),('Myozyme / Pompe',2006,'Reconcile Lumizyme branding and age scope.'),('Vimizim / MPS IVA',2014,'Procedural ERT comparator; no forecast retrieved.'),('Kanuma / LAL deficiency',2015,'Only undated-horizon peak quote recovered.'),('Xenpozyme / ASMD',2022,'Non-CNS disease scope; no forecast retrieved.'),('Lamzede / alpha-mannosidosis',2023,'US approval later than EU; non-CNS scope.')]:
    candidate(pair,y,'enzyme replacement','Retain for screening',why,'ert_fda' if pair.startswith(('Aldurazyme','Naglazyme','Elaprase')) else 'ert_review')
candidate('Mepsevii / MPS VII',2017,'enzyme replacement','Retain for screening','Tiny population; forecast unavailable.','mep_approval','Primary approval release checked')
candidate('Luxturna / RPE65 retinal dystrophy',2017,'genetic sensory','Retain for screening','One-time surgery and viable-cell window differ from repeat ASO.','lux_fda','FDA approval record checked')
candidate('Zokinvy / progeria and selected laminopathies',2020,'genetic systemic','Retain for screening','Multiple initial populations require scope matching.','zok_fda','FDA original bulletin checked')
candidate('Nulibry / MoCD-A',2021,'metabolic neurological','Retain for screening','Very early treatment window; forecast unavailable.','nul_fda','FDA approval report checked')
candidate('Oxlumo / PH1',2020,'RNA / metabolic','Ambiguous first-DMT cohort','Prior pyridoxine/transplantation; separate original label.','ox_label','Current label checked; launch classification pending')
for pair,y,decision,why in [
 ('Skyclarys / Friedreich ataxia',2023,'Retain for screening','At cutoff, 36-month sales history needs maturity check.'),
 ('Joenja / APDS',2023,'Retain for screening','Earlier off-label care needs adjudication.'),
 ('Sohonos / FOP',2023,'Retain for screening','Age, safety and launch maturity require review.'),
 ('Veopoz / CHAPLE',2023,'Retain for screening','Ultra-small population; launch immature.'),
 ('Pyrukynd / PK deficiency',2022,'Retain for screening','Prior disease-directed interventions require review.'),
 ('Enjaymo / cold agglutinin disease',2022,'Ambiguous first-DMT cohort','Earlier off-label disease-directed care.'),
 ('Ztalmy / CDKL5-associated seizures',2022,'Adjacent cohort','Seizure treatment is not proof of developmental modification.'),
 ('Miplyffa / Niemann-Pick C',2024,'Ambiguous first-DMT cohort','Prior miglustat; immature.'),
 ('Aqneursa / Niemann-Pick C',2024,'Exclude strict first entry','Earlier Miplyffa approval.'),
 ('Xolremdi / WHIM',2024,'Retain for screening','Immature commercial history.'),
 ('Crenessity / CAH',2024,'Exclude strict no-prior-DMT cohort','Prior glucocorticoids; immature.'),
 ('Tryngolza / FCS',2024,'Retain for screening','Diet and geography matter; immature.'),
 ('Ctexli / CTX',2025,'Ambiguous first-DMT cohort','Earlier off-label chenodiol; immature.'),
 ('Forzinity / Barth syndrome',2025,'Retain for screening','Accelerated evidence; immature.'),
 ('Kygevvi / TK2 deficiency',2025,'Retain for screening','Immature; earlier investigational treatment matters.'),
 ('Qalsody / SOD1 ALS',2023,'Modality comparator only','Prior ALS DMTs; accelerated evidence.'),
 ('Attruby / ATTR cardiomyopathy',2024,'Exclude strict first entry','Earlier approved disease-directed treatment.'),
 ('Fabhalta / C3 glomerulopathy',2025,'Scope-contaminated comparator','Product has other indications; immature.')]:
    candidate(pair,y,'FDA recent-approval screen',decision,why,'fda_arc','FDA index screened; detailed label/first-status adjudication pending')
for pair,why in [('Zanvastro / Alexander disease','2026 tracking only'),('Zycubo / Menkes disease','2026 tracking only'),('Avlayah / Hunter CNS disease','Manifestation-specific first status; 2026 tracking only')]:
    candidate(pair,2026,'outside mature cohort','Track only',why,'fda_arc','FDA index screened; no outcome calculation')
for pair,y,why in [('Ceredase / Gaucher',1991,'Historical extension outside core window'),('Cerezyme / Gaucher',1994,'Follow-on to Ceredase; do not count twice'),('VPRIV / Gaucher',2010,'Follow-on'),('Elelyso / Gaucher',2012,'Follow-on'),('Lumizyme / Pompe',2010,'Reconcile with Myozyme; not a separate independent first-DMT launch')]:
    candidate(pair,y,'ERT controls','Exclude primary / historical extension',why,'ert_review')

matrix=[
 ['Spinraza','High: repeat intrathecal ASO, pediatric genetics','Motor-neuron preservation and measurable motor/survival effects differ from developmental rescue','Secondary dated analyst quote + audited sales; PoS unknown','Not classifiable as a three-year beat/miss'],
 ['Brineura','High: pediatric CNS, specialist delivery, narrow window','Reservoir infusion; progressive degeneration; much smaller pool','Primary sales/labels; preapproval forecast absent','Outcome unclassified'],
 ['Daybue','High: neurodevelopmental adoption, caregiver-observed benefit','Oral treatment; unclear launch-era DMT status; different tolerability','Identifiable preapproval peak quotes; no annual curve','Future peak years not reached'],
 ['Kalydeco','High for genotype, patient finding and label expansion','Oral therapy; organ-function response differs from CNS development','Primary sales; recovered forecast postapproval','Excluded quantitative control'],
 ['Strensiq','Medium-high: pediatric genetic diagnosis and chronic therapy','Somatic ERT, different endpoints and dosing economics','Secondary point estimate; geographic ambiguity','Apparent beat depends on unresolved scope'],
 ['Onpattro','Medium: RNA, specialist centers, geography and competition','Adult progressive disease; prior transplantation; IV delivery','Original Cortellis publication; PoS and indication mix unresolved','Apparent point miss, not strict sell-side result'],
 ['Skysona / Zynteglo','High for delivery constraints; low for routine dosing economics','Cell collection, conditioning and one-time treatment differ sharply','Primary product sales; no authentic preapproval curve','No forecast-error classification']
]

data={'as_of':'2026-11-09','study_status':'Completed bounded desk study; hypothesis not identified by strict primary sample. Full approval census and licensed historical-model panel remain incomplete.',
 'sources':S,'protocol_sha256':hashlib.sha256((OUT/'study_protocol.txt').read_bytes()).hexdigest(),'current_sellside':brokers,'needham_conditional_sales':rows,'visible_alpha_reproduced_chart':va,'historical_forecasts':forecasts,'actual_sales':actuals,'screened_candidates':ledger,'analogue_matrix':matrix,
 'needham_inputs':{'source':'needham','pages':[25,26,27,28,29,31],'us_launch_year':2032,'row_launch_year':2033,'us_prevalence_2026_under18':11000,'population_growth':0.005,'diagnosis_rate_2026':0.15,'diagnosis_rate_2032':0.18,'diagnosis_rate_2040_onward':0.50,'peak_penetration_of_diagnosed':0.50,'adherence_persistence':0.75,'launch_annual_wac_usd':575000,'annual_wac_growth':0.03,'gross_to_net_discount':0.15,'row_to_us_sales_ratio':0.25,'pos':0.25,'wacc':0.09,'terminal_growth':0,'peak_sales_multiple':7,'diluted_shares_m':98,'net_cash_usdm':135,'dcf_ev_usdm':514,'multiple_ev_usdm':745,'blended_ev_usdm':630,'blended_equity_usdm':765,'printed_peak_sales_multiple_input_usdm':1843,'printed_peak_sales_multiple_year':2043,'status':'observed analyst assumptions, not independently validated forecasts'},
 'capitalization_bridge':{'source':'camp_10q','date':'2026-09-30','common_shares':62754200,'prefunded_initial':6003758,'prefunded_second':21925368,'prefunded_exercise_price_usd':0.0001,'reference_stock_price_usd':3.72,'price_source':'November 5–6 supplied broker reports; not live November 9 quote','cash_usdm':124.522,'status':'observed inputs; derived equity value and equity-less-cash proxy, before other adjustments'},
 'protocol_deviations':[
 'No complete FDA orphan approval export was reconciled. Ledger is a screened candidate set, not an exhaustive universe or denominator for selection adjustment.',
 'No historical record satisfies the complete 36/60-month, risk-treatment, geography and vintage requirements. Strict quantitative sample remains empty; contextual point comparisons are separate.',
 'Public quotations and one original commercial forecast publication substitute only as lower-tier contextual evidence, not as fully normalized broker models.',
 'Current CAMP reports arrived during work and were added as a separate benchmark; they did not change historical cohort rules.',
 'Machine-readable JSON replaces the preferred CSV because nested source, scope and exclusion fields are retained without flattening. Calculations are reproducible with standard Python.',
 'Trial registry mirror was encountered but not accepted as an official verified registry. September 8-K controls trial-design facts pending official protocol reconciliation.'
 ],
 'data_dictionary':{
 'sales_usdm':'USD millions of recognized net product sales, unless record explicitly states otherwise; no inflation/FX conversion.',
 'original_sales_usdm':'Published forecast value before any transformation; operator preserves > bounds.',
 'conditional_sales_usdm':'Approval-conditional sales only when risk handling is documented. Null for unresolved historical records, never zero.',
 'pos':'Disclosed scalar approval probability; null means unknown. Not inferred from discount rate or price target.',
 'target_year':'Forecast calendar year; null denotes undated peak. It is not commercial-year index.',
 'report_date':'Original note/publication date when recovered; null when only publication of a quotation is known.',
 'geography':'Exact stated or unresolved territory; unknown must not be silently treated as worldwide.',
 'scope':'Disease/label/age/genotype coverage and contamination notes.',
 'strict_eligible':'Requires genuine preapproval vintage, identifiable revenue scope, recoverable conditional forecast and matched complete horizon.',
 'status':'Observed = source transcription; derived = arithmetic; proxy = imperfect measure; assumed = hypothesis; unknown = unresolved.',
 'source':'Key into sources; local originals use absolute path, web evidence uses direct URL.',
 'verification':'Degree of clinical/regulatory screening, separate from forecast data quality.',
 'decision':'Scientific cohort screening decision; quantitative data exclusion remains separate.',
 'candidate_year':'US year where checked; review/index-seeded entries remain subject to individual approval adjudication.'}}
(OUT/'research_evidence.json').write_text(json.dumps(data,indent=2))

def refs(*keys):
    result=[]
    for k in keys:
        s=S[k]
        if 'url' in s:result.append(f'<a href="{html.escape(s["url"],quote=True)}">{html.escape(s["title"])}</a>')
        else:result.append(f'<span class="local">{html.escape(k)} [user PDF]</span>')
    return '<span class="refs">Sources: '+'; '.join(result)+'.</span>'
def table(headers,rows):
    return '<div class="tablewrap"><table><thead><tr>'+''.join('<th>'+html.escape(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+str(x)+'</td>' for x in r)+'</tr>' for r in rows)+'</tbody></table></div>'

body=[]
def section(id,title,text):body.append(f'<section id="{id}"><h2>{title}</h2>{text}</section>')
section('answer','What the evidence establishes', '''
<p class="lead">The available evidence does <strong>not establish systematic underforecasting of approval-conditional sales for first rare-disease DMTs</strong>. It supports a narrower research agenda: identify which patient-finding, uptake, persistence, delivery and geographic assumptions were wrong in specific launches, then test those mechanisms against CMP-002’s actual product profile.</p>
<p>This is an evidence-access conclusion, not a finding that forecasts are unbiased. The strict primary sample is <strong>N = 0 drug–indication pairs</strong>: none of the recovered historical forecasts simultaneously provides a complete matched three-year curve, documented risk treatment, territory and indication scope, and an eligible vintage. A sign test, median bias, confidence interval, leave-one-out estimate or generic sales uplift would therefore be fabricated precision.</p>
<p>The current CAMP reports materially sharpen the question. Needham already models $2.1bn of conditional worldwide peak sales, substantial diagnosis growth, and premium chronic pricing. Its valuation then applies 25% PoS and discounts a 2032 launch. An undervaluation argument must identify the specific commercial assumption or valuation input that is wrong; “rare-disease analysts tend to be conservative” does not do that work.</p>
<p><strong>Scope:</strong> historical commercial forecasting and analogue selection, plus the supplied Street baseline. This report does not build an independent CMP-002 sales model, reverse DCF, clinical PoS estimate or price target.</p>
'''+refs('needham'))

section('street','The supplied Street baseline',
 '<p>Eight reports cover seven firms, dated September 28–November 6, 2026. These are analysts’ estimates and target valuations, not observations of what the buyside collectively believes. Most supplied notes are catalyst updates rather than full commercial models.</p>'+table(['Firm / report','Rating / target','Valuation approach','What can be extracted'],[
 [html.escape(b['broker']+' · '+b['date']),html.escape(b['rating'])+' / '+('$'+str(b['target_usd']) if b['target_usd'] is not None else 'not freshly stated'),html.escape(b['method']),html.escape(b['sales_pos'])+'<br><small>'+html.escape(b['pages'])+'</small>'] for b in brokers])+'''
<h3>Needham’s auditable commercial assumptions</h3>
<p>Pages 25–27 provide the most complete approval-conditional model in this packet. US launch is 2032; EU4+UK revenue starts in 2033 and is set to 25% of US sales. The model labels its 2026 US population as 11,000 patients under 18, grows it 0.5% annually, and increases diagnosis from 15% to 50% by 2040. Penetration reaches 50% of diagnosed patients in 2037. Those are separate denominators: the mature model treats roughly one-quarter of estimated prevalent patients before the adherence/persistence adjustment.</p>
<p>Launch annual WAC is $575,000, growing 3% per year. The model applies a 15% gross-to-net discount and a 75% combined adherence/persistence factor. Its “net annual price” is consequently $366,563 at launch: <strong>$575,000 × 85% × 75%</strong>. Economically, that is revenue per modeled patient after utilization, not simply a net drug price. Applying a separate persistence haircut to that figure would double count it.</p>
<p>At the 2046 peak, the model has about 3,039 US patients and $554,459 of annual revenue per modeled patient, yielding about $1.685bn US and $421m outside the US. These are broker assumptions to test, not established epidemiology, achievable price, persistence or clinical efficacy. Diagnosis growth after launch is already explicitly present.</p>
'''+table(['Calendar year','Needham conditional WW sales, $m','VA consensus reproduced in Needham, $m'],[[y,ww[y-2032],v] for y,v in zip(range(2032,2041),[148,353,577,754,1074,1272,1444,1587,1716])])+'''
<p>The chart on p.26 presents a faster consensus ramp with convergence around 2040. The consensus composition, snapshot date and treatment of risk are not disclosed. Preserve these as reproduced chart observations; do not treat them as an independently verified conditional consensus panel.</p>
<h3>Valuation and reconciliation points</h3>
<ul>
<li>Needham’s 25% PoS belongs in the valuation bridge. Its conditional sales curve must not be divided by 25% again. Its DCF and 7x peak-sales method receive equal weights, producing a printed blended equity value of $765m and approximately $8 per share on 98m diluted shares.</li>
<li>Needham p.29 uses $1.843bn in 2043 for the multiple method, while p.26 shows $1.899bn in 2043 and a $2.106bn peak in 2046. P.27’s sensitivity matrix uses $538,309, versus $554,459 in its adjacent peak summary. These are visible internal input discrepancies, not extraction errors. Reconcile the native model before replicating its target.</li>
<li>The headline $6 drug / $2 cash decomposition does not exactly match p.29’s printed $630m drug / $135m cash on 98m shares. Those figures imply approximately $6.43 and $1.38; the rounded $8 target is still consistent with the total. Preserve exact dollar values rather than relying on headline rounding.</li>
<li>Needham’s p.28 DCF expense rows differ from its p.31 operating model: for example, 2027 R&amp;D is about $14m versus $55m and SG&amp;A $6m versus $24m. The relationship is consistent with 25% weighting, but the model’s expense-risk methodology is not fully documented. These DCF rows are unsuitable as unconditional cash-burn assumptions.</li>
<li>William Blair’s p.4 has 2030 SYNGAP revenue as well as much larger UCD revenue. Timing, conditional status and pipeline attribution require clarification before comparing this with Needham’s 2032 launch. Leerink explicitly leaves several other opportunities unvalued. A single “Street model” would conceal these differences.</li>
</ul>
'''+refs('needham','blair','leerink_oct')+'''
<h3>Share counts explain part of the quoted EV dispersion</h3>
<p>The September 30 filing records 62.7542m common shares and two pre-funded warrant blocks totaling 27.929126m shares at $0.0001 exercise prices. Together these give about 90.6833m economic shares before ordinary option and future financing adjustments. This reconciles the roughly 62.8m versus 90.7m counts in the reports. At the reports’ $3.72 reference price, that is about $337.3m equity value and $212.8m equity value less $124.522m cash. This is a capitalization check, not a live November 9 quote or a complete enterprise-value calculation. Needham’s 98m diluted denominator is a further distinct basis.</p>
'''+refs('camp_10q')+'''
<p>For the separate valuation project, use current company operating costs as a starting point, then model trial stages and financing explicitly. The broker packet’s 2027 R&amp;D/G&amp;A estimates include Piper’s $50m/$20m, Needham’s $55m/$24m and Blair’s $61.29m/$20.746m. These are company-level forecasts with differing pipeline assumptions, not a universal preclinical biotech cost template.</p>
'''+refs('piper','needham','blair'))

section('context','CMP-002: the context that determines relevance', '''
<p>As of the November 5 update, trial activities had begun and first dosing was still expected by year-end 2026. CMP-002 is a regulatory-RNA-targeting ASO intended to increase endogenous SYNGAP1 expression. Human benefit had not been demonstrated. CAMP also disclosed a SHANK3 program; the company is not literally a single-asset entity.</p>
'''+refs('camp_update')+'''
<p>The September protocol disclosure describes intrathecal treatment, three doses over about three months, and exploratory seizure, sleep, motor, communication, behavior and developmental endpoints. Initial eligibility is narrower than the disease population: age 2–&lt;18, specified protein-truncating variants in exons 5–19, and a substantial symptomatic burden. This is not an approved label. A chronic commercial dosing interval, breadth of benefit, durability and reversibility remain unknown.</p>
'''+refs('camp_8k')+'''
<p>Existing care includes antiseizure treatment, dietary/device approaches where appropriate, and developmental and supportive services. Uptake would occur on top of an existing care pathway. A caregiver might accept repeated procedures for broad functional gains while responding differently to a modest seizure-only benefit; that is a scenario to test, not an observed adoption rate.</p>
'''+refs('chop')+'''
<p>Patient counts require several distinct measures: biological prevalence, pathogenic and treatment-responsive genotype prevalence, diagnosed patients, patients known to advocacy groups, label eligibility, reimbursed eligibility, and ability to receive treatment. An original census study counted 1,400 known patients worldwide, including 401 in the US, at March 31, 2024. That historical advocacy count is neither a 2026 count nor total diagnosed prevalence. Its variant-incidence analysis also shows that extrapolated missense and truncating populations need separate scrutiny.</p>
'''+refs('syngap_census')+'''
<p>Needham separately cites a September 2026 global advocacy census of 1,871 and claims-based estimates from earlier company materials. Those populations and methods should not be blended into one diagnosis-rate denominator. Its physician survey comprises 16 respondents managing about 85 patients; stated willingness to use a hypothetical profile is useful qualitative evidence, not independently observed demand. The <em>11,000 under-18 US population</em> in its model needs its own epidemiological validation.</p>
'''+refs('needham')+'''
<p>Competitive first status is provisional. Stoke’s August 2026 update places its SYNGAP1 work in lead optimization. Commercial forecasts should track future RNA and gene-therapy entrants, trial progress and time to launch, rather than assume permanent exclusivity. A late-stage Dravet ASO can inform development or administration questions, but is not yet a historical launched SYNGAP1 sales analogue.</p>
'''+refs('stoke'))

section('method','Protocol, definitions and analysis pipeline', '''
<p>The dated protocol is supplied separately. It was written before this run’s case-level forecast-error calculations; prior familiarity with well-known cases means this is not blinded preregistration. Approval and clinical sources seed the cohort; forecast availability does not determine scientific relevance. Dated forecasts are then matched with issuer sales, and only documented transformations are permitted.</p>
'''+table(['Term','Operational treatment'],[
 ['First DMT','First intervention in the specified territory supported at launch by mechanism and clinical evidence of altering disease course or pathophysiology. Record earlier transplant, diet and meaningful off-label disease modification.'],
 ['First disease-specific therapy','First disease-specific approval; can be symptomatic. Report separately when DMT status is uncertain.'],
 ['First in class','Novel mechanism or class; does not imply first effective treatment or first DMT.'],
 ['Replacement / restorative / potentially curative','Describe mechanism and intended durability separately. These labels do not guarantee complete functional recovery.'],
 ['Rare disease','US orphan framework: fewer than 200,000 affected, with the statutory cost-recovery exception separately flagged. Population size is still stratified commercially.'],
 ['Unit of analysis','Drug–indication pair. Multiple analyst estimates do not create independent drug outcomes.'],
 ['Primary comparison','Nearest forecast to 12 months before approval within 9–15 months; earlier date breaks ties. Matched first 36 months of net sales, preferably US.'],
 ['Secondary comparisons','Last preapproval vintage, pre-pivotal/early-stage vintage, first 60 months and annual diagnostics; never pooled silently.'],
 ['Error','Actual / conditional forecast − 1; preserve absolute-dollar error. No percentage if denominator is zero; no arbitrary pseudocount.'],
 ['Timing','Calendar-time comparison retains launch delays; launch-aligned comparison isolates ramp only when the original forecast supports alignment.'],
 ['PoS','Remove only a documented multiplication in the revenue row. Do not infer stage-average PoS or divide already conditional sales.'],
 ['Scope','No later indications; age/genotype expansions flagged. Territories, revenue owner, royalties, milestones and currencies must match.']])+'''
<p>Conditional-on-launch analysis is legitimate for the commercial question. It does not establish that approved drugs represent all programs: PoS normalization does not remove selection on unobserved efficacy, label quality, commercial attractiveness or survival of coverage. The current sample also faces <em>document-access selection</em>: spectacular forecasts and large launches are more likely to leave public quotations.</p>
<p>Original broker models offer the best precision but require licensed access. Public dated quotations are fast to audit but usually omit curves and risk treatment. Original company filings offer strong recognized-sales evidence yet often cannot separate labels or territories. Claims, infusion-center records, testing laboratories, patient organizations and payer policy histories may identify mechanisms, but each observes a selected population. These sources are complements, not interchangeable proxies.</p>
<p>No paid data, bulk scraping or large OCR was undertaken. Several targeted leads were pursued after the initial pass; expansion stopped when original historical forecasts became the binding constraint. Official registry details could not be independently reconciled; a third-party CTIS mirror was not treated as the official record.</p>
<h3>Protocol deviations and incomplete elements</h3>
<ol>'''+''.join('<li>'+html.escape(x)+'</li>' for x in data['protocol_deviations'])+'''</ol>
<p>A full approval-based census remains unfinished. Consequently the ledger cannot support a formal estimate of forecast-availability bias or a population-wide conclusion. The record-level exclusions are retained so licensed data can later extend this study without changing its rules.</p>''')

section('literature','What broader launch studies do—and do not—show',
table(['Study','Recovered result','Why it does not answer the exact question'],[
 ['Deloitte 2020','149 US launches, 2012–2017; first-year actuals: 48% &gt;120% of consensus, 16% within 80–120%, 36% below 80%.','Consensus measured at approval; mixed therapies, not preapproval first DMTs. Rare-disease subgroup requires separate definitions. '+refs('deloitte')],
 ['Deloitte / ISPOR 2024','284 drugs/new indications in 2012–2021; selected rare-disease company-size groups had high meet-or-exceed rates.','Meeting a forecast is not beating it; indications and company classes differ. Reasons for failure come from an underperformer subset, not a causal decomposition. '+refs('ispor')],
 ['McKinsey 2024','Roughly 40% of rare-disease first-time-company launches exceeded expectations; less crowded markets performed better.','First-time company is not first DMT. Shared commercial databases mean these studies are not independent replications. '+refs('mck')],
 ['Ilicki / Spicer 2026 abstract','Survey of 43 investors/BD professionals; many underestimated reported rare-disease launch performance.','Measures beliefs about launch results, not a matched panel of broker forecast errors. Full text unavailable. '+refs('illicki')],
 ['ZS first-launch study','30 launches in 2019–2021: 13 over, 13 under, four within a ±20% band.','Not specific to rare first DMTs or the chosen preapproval estimand. '+refs('zs')]
])+'''<p>These studies support taking unmet need, competition and execution seriously. They do not justify converting a “meet or beat” statistic into a probability that analysts underestimate CMP-002, or adding a universal rare-disease premium to its sales forecast.</p>''')

section('results','Quantitative results and their limits', '''
<p><strong>Strict matched 36-month cohort: N=0. Strict 60-month cohort: N=0. Formal aggregate signed bias: not estimable.</strong> The same empty-sample result applies to high-quality-only, fixed-US, early-stage and label-clean sensitivities. There is no valid three-year result to repeat in a five-year-mature subset. Do not report a win rate from the heterogeneous observations below.</p>
'''+table(['Contextual observation','As-reported arithmetic','Why excluded from the primary result'],[
 ['Spinraza: Needham August 2016 forecast &gt;$5bn worldwide in 2022; actual $1.7935bn.','Actual was less than 35.9% of the forecast; error below −64.1%.','Unknown PoS; one late-stage analyst; later single year, not first 36 months. '+refs('spin_forecast','biogen22')],
 ['Strensiq: quoted 2018 estimate $355m; actual $475.1m WW or $374.3m US.','+33.8% if WW; +5.4% if US.','Forecast geography and PoS unknown. These are alternative scope checks, not two observations. '+refs('str_forecast','alxn18')],
 ['Onpattro: Clarivate 2018 publication projected $1.212bn in 2022; actual $558m.','−54.0% on an as-reported comparison.','Cortellis composition, risk treatment and anticipated indication scope unresolved. '+refs('on_forecast','alny22')],
 ['Daybue: preapproval US peak quotes of $487.2m in 2035 and &gt;$500m in 2032.','No realized peak error available.','Future forecast years have not elapsed; no observed annual curve. '+refs('day_forecast')],
 ['Brineura: $8.6m/$39.9m/$72.0m in 2017/2018/2019.','First three reported calendar years total $120.5m.','No authentic preapproval curve; partial launch year means this is not first 36 months. '+refs('brin17','brin19')]
])+'''<p>The negative point examples prevent a one-sided success narrative, but cannot establish overforecasting either. Different horizons, modalities, vintages and data quality make a pooled average misleading. Original annual curves are needed to determine whether early launch beats coexist with later misses.</p>''')

section('analogues','Analogue relevance, evidence quality and outcome are separate',
table(['Analogue','What is relevant','Key mismatch','Forecast evidence','Outcome classification'],matrix)+'''
<p>Relevance ratings were assigned to mechanisms before extracting the case errors. No composite numerical score is used: a close administration analogue with poor forecast data remains scientifically useful but quantitatively unusable. Similar TAM alone is inadequate; a large disease may reveal procedural bottlenecks, while a similarly sized oral market may tell little about repeat lumbar puncture adoption.</p>''')

section('cases','Case studies: what to test in each', '''
<h3>Spinraza / SMA</h3>
<p><strong>Before approval:</strong> the recovered August 2016 Needham quote followed favorable pivotal interim evidence. It was not a preclinical forecast and was not consensus. <strong>Observed:</strong> the reported 2022 outcome was far below that ambitious forecast. Separately, a postapproval second-quarter 2017 consensus was beaten sharply; that cannot be relabeled a preapproval forecasting success.</p>
<p><strong>Mechanisms to distinguish:</strong> fast access to known patients and loading doses can accelerate first-year sales; persistence, maintenance dosing, subsequent treatment choices and territory mix can alter later years. Company disclosures document competitive and geographic pressures, but do not assign a causal fraction of the 2016 forecast miss to each factor. A small commercial-insurance claims study also illustrates that scheduled doses need not equal observed utilization; it is not a population-wide adherence estimate.</p>
<p><strong>Transfer:</strong> prioritize procedure capacity, starts versus maintained patients, and age-specific benefit. Do not transfer SMA’s clinical effect size to SYNGAP1. This case is particularly valuable because it can challenge both a “rapid launch guarantees large lifetime sales” thesis and a “intrathecal delivery prevents uptake” thesis.</p>
'''+refs('spin_approval','spin_forecast','biogen22','spin_quarter','spin_label','spin_claims')+'''
<h3>Brineura / CLN2</h3>
<p><strong>Before approval:</strong> no usable contemporaneous sales curve was recovered. <strong>Observed:</strong> sales rose from $8.6m in the partial 2017 launch year to $128.034m in 2021. Original approval addressed slowing loss of ambulation in children aged at least three. Later age expansions must be separated.</p>
<p><strong>Mechanisms to distinguish:</strong> diagnosis, referral and center activation can each limit starts. Intraventricular delivery through an implanted access device has a different burden from intrathecal ASO dosing. Low early revenue could reflect a genuinely tiny pool, slow center activation or simply a forecast that already expected both. Without the forecast and patient/center series, it is not evidence that analysts missed.</p>
<p><strong>Transfer:</strong> strong analogue for pediatric CNS logistics and treatment windows; weak direct price or population analogue. Obtain time from diagnosis to referral, referral to procedure, and procedure to reimbursed treatment before raising early CMP-002 penetration.</p>
'''+refs('brin17','brin19','brin21','brin_label')+'''
<h3>Daybue / Rett</h3>
<p><strong>Before approval:</strong> Reuters quoted identifiable US peak estimates from SMBC and RBC, but not their intervening annual trajectories. <strong>Observed:</strong> reported product sales were $177.2m, $348.4m and $391.4m in 2023–2025, totaling $917.0m across the three calendar years. That is neither three full commercial years from an April launch nor a quantity comparable with one future year’s peak.</p>
<p><strong>Mechanisms to distinguish:</strong> unmet need can generate initial interest while tolerability and perceived benefit affect continuation. The original label’s gastrointestinal adverse-event profile makes persistence a necessary question; it does not quantify its contribution to revenue. Caregiver reports, refill cohorts, free-drug use and payer access are needed to distinguish starts from sustained treatment.</p>
<p><strong>Transfer:</strong> a high-priority neurodevelopmental adoption comparator, kept in the adjacent disease-specific cohort. Oral delivery differs from CMP-002. Do not claim proven developmental recovery or use early total-product revenue to declare that 2032/2035 US forecasts have been beaten.</p>
'''+refs('day_forecast','day24','day25','day_label','day_fda')+'''
<h3>Kalydeco / G551D cystic fibrosis</h3>
<p><strong>Before approval:</strong> no suitable original annual curve was recovered. A readily found JPMorgan forecast is dated May 2012, after January approval, and is excluded. <strong>Observed:</strong> product sales reached $631.674m in 2015, but later genotype and age expansions make aggregate product revenue unsuitable for the original G551D population.</p>
<p><strong>Mechanisms to distinguish:</strong> known genotype-positive patients, testing expansion and new label eligibility are different growth sources. A revenue beat driven by later mutations would not answer the fixed-indication/label question. <strong>Transfer:</strong> model responsive genotype and age eligibility explicitly; do not raise both prevalence and penetration for the same newly identified patient.</p>
'''+refs('kaly_label','kaly_forecast','vrtx15')+'''
<h3>Strensiq / hypophosphatasia</h3>
<p><strong>Before approval:</strong> a September 2015 quotation gives a $355m 2018 forecast, but the public excerpt does not establish geography or PoS. <strong>Observed:</strong> worldwide revenue was $475.1m, while US revenue alone was $374.3m. Resolving geography therefore changes the apparent magnitude substantially.</p>
<p><strong>Mechanisms to distinguish:</strong> finding previously undiagnosed patients, treating the known pool, geographic rollout and realized price could all contribute. A plausible patient-finding story is not a measured revenue bridge. The source’s unrelated acquisition-history error also argues for obtaining the underlying report. <strong>Transfer:</strong> useful for pediatric genetic diagnosis and chronic treatment adoption, with somatic endpoints and weight-dependent economics that differ from CNS ASOs.</p>
'''+refs('str_forecast','alxn18','str_label')+'''
<h3>Onpattro / hATTR polyneuropathy</h3>
<p><strong>Before approval:</strong> Clarivate’s March 2018 publication gives $83m in 2018, $373m in 2019 and $1.212bn in 2022. It is an authentic dated forecast publication, but its Cortellis figures are not established as pure sell-side consensus. <strong>Observed:</strong> 2018 sales were $12.5m and 2022 sales $558m.</p>
<p><strong>Mechanisms to distinguish:</strong> launch timing, infusion access, competition, geography and assumptions about cardiomyopathy could explain differences. Cardiomyopathy revenue must not be imported into a polyneuropathy test; a successor product’s sales cannot be added to rescue the original product forecast. Prior transplantation and European treatment history also complicate “first DMT” status.</p>
<p><strong>Transfer:</strong> RNA modality alone does not establish comparable adoption. This is a useful counterweight to a blanket bullish thesis, pending a clean underlying forecast and original-indication allocation.</p>
'''+refs('on_forecast','alny18','alny22')+'''
<h3>Skysona / CALD and Zynteglo / beta-thalassemia</h3>
<p><strong>Before approval:</strong> no usable annual analyst curve recovered. <strong>Observed:</strong> 2023/2024 US sales were $12.373m/$9.917m for Skysona and $16.692m/$62.273m for Zynteglo. Revenue is recognized at infusion; cell-collection guidance is not revenue. The products are kept separate from each other and from Lyfgenia.</p>
<p><strong>Mechanisms to distinguish:</strong> eligibility, conditioning, collection/manufacturing and infusion capacity can separate patient interest from recognized sales. Prior transplantation means these are not strict “no previous DMT” examples. Subsequent safety evidence must be dated rather than backdated into launch-era classification.</p>
<p><strong>Transfer:</strong> useful operational downside cases, not direct chronic-ASO revenue multiples and not proven analyst misses without their forecasts.</p>
'''+refs('blue24','sky_fda'))

transfer=[
 ['Diagnosis expansion','Known-patient and biological-prevalence pools differ across genetic diseases.','Needham already grows diagnosis to 50%. Validate pathogenic-genotype prevalence, testing access and diagnostic conversion.','Diagnosed-patient flow; sensitivity until independently supported. Avoid adding the same effect again to penetration.'],
 ['Fast prevalent-patient uptake','Some first launches can reach a known pool quickly; annual and cumulative trajectories can diverge.','Require eligible diagnosed patients, physician intent tied to a realistic profile, payer approvals and procedure capacity.','Separate prevalent backlog from new diagnoses; scenario, not generic premium.'],
 ['Broad functional efficacy','Observable benefit can affect adoption and continuation.','Require human data across functional domains and age groups; seizure improvement alone is insufficient.','Separate seizure-only, broad-benefit and early-age benefit scenarios; no preclinical effect-size conversion.'],
 ['Persistence and utilization','Starts, scheduled doses and paid treatment exposure differ.','Confirm dose interval, tolerability, caregiver burden, discontinuation and reinitiation.','Cohort continuation and billable doses; avoid reapplying Needham’s 75% factor.'],
 ['Price and GTN','List price is not recognized net revenue.','Obtain payer mix, rebates, free drug, dosing and contracting assumptions.','Separate WAC, discounts and utilization; base case requires direct support.'],
 ['Delivery capacity','CNS and cell-therapy products require different clinical infrastructure.','Measure centers, procedure slots, anesthesia needs, referral delays and caregiver travel.','Constraint on starts and maintenance; scenario until measured.'],
 ['Geographic rollout','A worldwide estimate can miss because of rollout, local price or scope.','Replace a simple ROW multiplier with territory-level eligibility, access and net price when justified.','Separate territory sensitivities; no later disease indications.'],
 ['Competition','Later substitutes can alter a successful initial ramp.','Track entrant efficacy, route and development timing; first status at launch remains uncertain.','Share, persistence and exclusivity scenarios.'],
 ['Clinical risk / timing / financing','Conditional sales and today’s value answer different questions.','Document PoS and cost-stage weighting; reconcile shares and other assets.','Valuation project only; no sales-premium adjustment.']]
section('transfer','What can enter the CMP-002 model',
table(['Mechanism','Historical lesson','CMP-002 evidence needed','Permitted use now'],transfer)+'''
<p><strong>Ready now:</strong> the audited transcription of Needham’s assumptions and the share-count bridge can enter a comparison workbook as observed benchmarks. Patient-funnel definitions, territory separation, and the distinction between list price and utilization should enter model structure. <strong>Not ready:</strong> a historical bias coefficient, a revised clinical PoS, a generic rare-disease sales uplift, or an empirically calibrated CMP-002 penetration/persistence estimate. The case studies inform scenario design, not those numerical inputs.</p>''')

section('claims','Investor claims: supported, qualified, unsupported',
table(['Status','Claim','Boundary'],[
 ['Supported','Current analysts can value CMP-002 conservatively today while modeling blockbuster sales conditional on success.','Needham provides a direct example; target valuation is not the market price.'],
 ['Supported','First-DMT commercial outcomes depend on diagnosis, access, benefit, utilization and competitive context.','Mechanisms justify explicit modeling; they do not identify a universal directional bias.'],
 ['Qualified','Treatment availability may expand diagnosed and treated populations.','Test the magnitude against the existing forecast; Needham already assumes diagnosis growth.'],
 ['Qualified','Certain historical launches exceeded some contemporaneous estimates.','Specify analyst, vintage, geography and horizon; the recovered Strensiq quote is not fully normalized.'],
 ['Unsupported','Sell-side systematically underforecasts first rare-disease DMT revenue.','Strict matched historical sample is empty; broader studies use different estimands.'],
 ['Unsupported','Spinraza or Daybue proves CMP-002 will exceed its Street curve.','Different clinical evidence and delivery; incomplete forecast matching.'],
 ['Unsupported','Normalizing PoS eliminates survivorship or access bias.','It changes forecast scale, not which programs launch or which reports survive.'],
 ['Unsupported','CAMP’s market valuation implies a specific low sales forecast.','Reverse valuation is not identified without fixing clinical risk, timing, costs, financing and other assets.']]))

section('missing','Ranked evidence acquisition specification',
table(['Priority','Obtain','Why it matters / access route','Stopping rule'],[
 ['1','Original models for Spinraza, Brineura, Daybue, Strensiq, Kalydeco and Onpattro at prescribed vintages.','Licensed broker archive or user-provided reports. Request annual sales, expected launch, original label/geography, PoS location and analyst identity—not just price targets.','One verified primary-vintage model per drug first; expand analyst breadth only after scope and actuals reconcile.'],
 ['2','Contemporaneous consensus snapshots and constituent histories.','Visible Alpha / Evaluate / other licensed historical data, subject to product rights. Recover snapshot timestamps and contributors; reject current backfilled histories as historical consensus.','Pilot on three diverse products; stop if original timestamps or risk handling cannot be recovered.'],
 ['3','Quarterly original-indication, territory-specific actuals.','Issuer filings, historical earnings tables and partner disclosures. Separate expansions, royalties and product switches.','Exclude a pair from strict analysis if credible separation is impossible; retain qualitative evidence.'],
 ['4','Reconciled US orphan-approval census, 2000–2025.','FDA orphan database plus Drugs@FDA/CBER; deduplicate ingredients, indications, follow-ons and territory dates.','Freeze screening decisions before revealing additional sales outcomes. No bulk collection undertaken here.'],
 ['5','Native CAMP models and current consensus definitions.','Resolve Needham p.26–29 discrepancies; Blair 2030/UCD rows; consensus PoS, sample and date; share-count conventions.','Use exact reported values with flags until the native model resolves differences.'],
 ['6','CMP-002 eligible patient and utilization evidence.','Genetics labs, referral centers, patient organizations, natural history and payer/claims sources observe different parts of the funnel. Any nonpublic outreach requires separate authorization.','Predefine populations and validation checks; stop when new sources are only weak or duplicative proxies.']])+'''
<p>Original analyst archives have the highest immediate information value. More public peak-sales headlines are unlikely to resolve the missing conditional annual curves. No paid access or outreach is initiated by this report.</p>''')

section('ledger','Screened candidate and exclusion ledger',
f'<p>{len(ledger)} candidate/control entries. This is the complete ledger of this desk study’s screened set, <strong>not a complete universe of all eligible rare-disease launches</strong>. Index/review entries remain provisional; lack of a forecast is kept separate from scientific exclusion.</p>'+table(['Drug / disease','US year','Screening decision','Reason / data limitation','Source / verification'],[[html.escape(x['pair']),x['us_approval_year'],html.escape(x['decision']),html.escape(x['reason']),refs(x['source'])+'<br><small>'+html.escape(x['verification'])+'</small>'] for x in ledger])+'''
<p>Remaining discovery coverage includes additional inherited-metabolic drugs, older non-neurologic first treatments, and withdrawn/commercially unsuccessful products. No full failed-launch census was completed. ERT follow-ons and gene therapies after prior DMTs are deliberately retained as controls rather than quietly omitted. Orphan oncology is outside the primary cohort.</p>''')

section('audit','Audit trail and files', '''
<p>The companion JSON retains original values, missing fields, source locations, risk treatment and exclusions. The calculation script uses only the Python standard library and reproduces the contextual point comparisons, sums, capitalization bridge and Needham checks. It produces no aggregate bias estimate. Printed revenue rows are rounded; reconstructed arithmetic may differ slightly.</p>
<p>Verification separated three tasks: (1) source transcription and arithmetic, including visual inspection of critical broker tables; (2) calibration to a reported historical forecast, which remains unavailable for most pairs; and (3) independent validation of CMP-002 assumptions, which this historical study cannot supply. Passing arithmetic checks is not validation of the sales thesis.</p>
<p>Source quality and access failures are recorded below. Files contain no invented forecasts, no inferred probabilities, no later-indication allocation and no synthetic monthly curves.</p>
'''+table(['Source ID','Document / location','Evidence type and access'],[[k,('<a href="'+html.escape(s['url'],quote=True)+'">'+html.escape(s['title'])+'</a>') if 'url' in s else html.escape(s['title'])+'<br><small>'+html.escape(s['path'])+'</small>',html.escape(s['type'])+'<br>'+html.escape(s.get('access_note',''))] for k,s in S.items()]))

css='''body{font:16px/1.65 system-ui,-apple-system,sans-serif;color:#172334;background:#f4f6f8;margin:0}main{max-width:1180px;margin:auto;padding:50px 40px;background:white}header{border-bottom:3px solid #173d57;padding-bottom:28px;margin-bottom:30px}.eyebrow{color:#48657a;font-size:13px;letter-spacing:1.5px;text-transform:uppercase}h1{font-size:38px;line-height:1.15;max-width:950px;font-weight:650}h2{font-size:26px;color:#173d57;margin-top:50px}h3{font-size:20px;margin-top:30px}.lead{font-size:20px}p{max-width:1040px}.refs{display:block;font-size:12px;color:#566474;line-height:1.5;margin:7px 0 12px}a{color:#11668a}nav{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:13px;margin:22px 0}.tablewrap{overflow-x:auto;margin:20px 0}table{border-collapse:collapse;width:100%;font-size:13px;line-height:1.45}th{background:#183f58;color:white;text-align:left;padding:12px;vertical-align:top}td{border-bottom:1px solid #dce3e7;padding:12px;vertical-align:top}tr:nth-child(even){background:#f5f8fa}td .refs{margin:5px 0;font-size:11px}small{color:#637181;overflow-wrap:anywhere}li{margin:10px 0}.local{font-weight:600}footer{margin-top:50px;padding-top:20px;border-top:1px solid #ccd6df;color:#637181;font-size:12px}@media print{body{background:white}main{padding:0}nav{display:none}h2,h3{break-after:avoid}tr{break-inside:avoid}a{color:inherit}table{font-size:10px}}'''
nav=''.join(f'<a href="#{i}">{label}</a>' for i,label in [('answer','Answer'),('street','Street baseline'),('context','CMP-002'),('method','Protocol'),('literature','Literature'),('results','Results'),('cases','Cases'),('transfer','Model use'),('claims','Investor claims'),('missing','Missing evidence'),('ledger','Ledger'),('audit','Sources')])
doc='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CMP-002 — historical forecast evidence and Street baseline</title><style>'+css+'</style></head><body><main><header><div class="eyebrow">Independent research · 9 November 2026</div><h1>CMP-002: historical revenue-forecast evidence and the current Street baseline</h1><p>First rare-disease DMTs · fixed drug–indication scope · approval-conditional commercial forecasts</p><nav>'+nav+'</nav></header>'+''.join(body)+'<footer>Research cutoff: 9 November 2026. Historical point comparisons are contextual and not a normalized cohort result. Source material and limitations are retained in research_evidence.json.</footer></main></body></html>'
(OUT/'CMP002_research_brief.html').write_text(doc)
print(json.dumps({'sources':len(S),'candidate_entries':len(ledger),'historical_forecast_records':len(forecasts),'actual_sales_records':len(actuals),'strict_primary_n':0,'html_bytes':len(doc.encode())},indent=2))
