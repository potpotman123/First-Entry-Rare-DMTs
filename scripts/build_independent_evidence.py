"""Curated extraction records for the independent rebuild; no forecast selects a case.
Run after build_independent_universe.py. Standard library only.
"""
from pathlib import Path
import json, hashlib, csv
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'data/independent'
prior=json.loads((ROOT/'data/research_evidence.json').read_text())
screen=json.loads((OUT/'approval_screen.json').read_text())
sources={}
def src(k,title,url,locator,status='primary source checked',local=None):
 sources[k]=dict(title=title,url=url,locator=locator,verification=status,retrieved='2026-11-09',local_file=local)
for k in ['camp_update','camp_8k','chop','syngap_census','stoke','spin_approval','spin_label','spin_forecast','biogen22','brin17','brin19','brin21','day_fda','day_label','day24','day25','str_label','str_forecast','alxn18','kaly_label','vrtx15','mep_approval','mck','ispor']:
 v=prior['sources'][k];src(k,v['title'],v['url'],v.get('locator','See linked source / prior evidence record'),'reused verified source; selection independently fixed')
src('werber04','Yaron Werber (SG Cowen), Lysosomal storage diseases market, January 2004','https://sites.ualberta.ca/~dcl3/Ref_2007-Aug-17/Orphan%20drugs/Market%2Blysosomal%2Bstorage%2Bdiseases.pdf','Nature Reviews Drug Discovery 3, pp.9–10; Table 1 p.10; Table 2 identities; DOI 10.1038/nrd1286','original analyst-authored publication; table visually checked','sources/publications/Werber_2004_lysosomal_storage_diseases_market.pdf')
src('bmrn07','BioMarin 2007 Form 10-K','https://www.sec.gov/Archives/edgar/data/1048477/000119312508040467/d10k.htm','MD&A, Naglazyme net product sales and foreign-currency discussion')
src('genz07','Genzyme 2007 annual financial statements, Exhibit 13','https://www.sec.gov/Archives/edgar/data/732485/000104746908002100/a2182799zex-13.htm','MD&A, Myozyme product revenue; annual report incorporated into Form 10-K')
src('shire07','Shire full-year 2007 financial results','https://www.sec.gov/Archives/edgar/data/936402/000095010308000425/dp08699_ex9901.htm','Product sales table / ELAPRASE discussion')
src('vimforecast','Fierce Pharma, Vimizim panel nod fuels new BioMarin buyout buzz, Nov.21 2013','https://www.fiercepharma.com/m-a/vimizim-panel-nod-fuels-new-biomarin-buyout-buzz','Paragraph quoting Bloomberg analysts: $416m annual sales in 2017','dated secondary quotation; underlying Bloomberg constituent models unavailable')
src('vimactual','BioMarin 2017 Form 10-K, Note 20 product revenues','https://www.sec.gov/Archives/edgar/data/1048477/000156459018003114/R28.htm','2017 Vimizim 413,251; table units USD thousands')
src('kanforecast','Reuters May 6 2015, Alexion to buy Synageva','https://uk.investing.com/news/stock-market-news/alexion-pharma-to-buy-synageva-biopharma-for-%248.4-billion-47702','Cortellis $603m in 2020; management >$1bn expectation is a separate statement','dated Reuters quotation of Cortellis; analyst composition and risk basis unknown')
src('alxn20','Alexion 2020 Form 10-K','https://www.sec.gov/Archives/edgar/data/899866/000089986621000014/alxn-20201231.htm','Product table p.92 / Note 18 F-66: Kanuma 117.9; intangible impairment discussion pp.64,87–88')
src('kanimpair','Alexion 2020 Form 10-K, intangible assets note','https://www.sec.gov/Archives/edgar/data/899866/000089986621000014/R12.htm','June 2020 reassessment of patient growth and commercial resource priorities; $2,042.3m impairment')
src('myalept15','Aegerion 2015 Form 10-K','https://www.sec.gov/Archives/edgar/data/1338042/000155837016004149/aegr-20151231x10k.htm','MYALEPT price increase, Medicaid rebate and net revenue discussion')
src('myaleptgt','Aegerion Jan.11 2016 preliminary FY2015 update','https://www.sec.gov/Archives/edgar/data/1338042/000119312516425825/d108787dex991.htm','MYALEPT: approximately 30% GTN, 27 percentage points attributable to Medicaid rebates; preliminary company disclosure')
src('arc10','Regeneron 2010 annual report','https://newsroom.regeneron.com/static-files/b9b76883-1727-4b17-b922-237adfb1655c','ARCALYST revenues 2010/2009/2008; 2010 includes $4.8m deferred revenue')
src('mep17','Ultragenyx 2017 Form 10-K','https://www.sec.gov/Archives/edgar/data/1515673/000156459018002535/rare-10k_20171231.htm','2017 product sales $0.5m, including named-patient sales')
src('meplabel','Mepsevii prescribing information','https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=925d4e21-fd98-474d-a34d-a0b3558ed750','Indication and limitation: CNS effect not determined; current label is not substituted for original age scope')
src('lux18','Spark 2018 Form 10-K','https://www.sec.gov/Archives/edgar/data/1609351/000160935119000042/spark-201810xk.htm','2018 net product revenue $27.0m; $37.8m contract revenue excluded')
src('nul21','Nulibry original FDA label, 2021','https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/214018s000lbl.pdf','Sections 1,2 and14: MoCD-A mortality, daily IV dosing, clinical evidence')
src('ztalmy23','Marinus March 2024 commercial update filed with SEC','https://www.sec.gov/Archives/edgar/data/1267813/000155837024002473/mrns-20240305xex99d2.htm','Slides6–7: 2023 US net revenue $19.6m, >165 active patients at year-end; claims-data strategy')
src('ztalmy24','Marinus November 2024 commercial update','https://www.sec.gov/Archives/edgar/data/1267813/000155837024015311/mrns-20241112xex99d2.htm','Patient-identification and launch slides; management claims, not an independent registry')
src('cha13','Cha, Rifai and Sarraf, Pharmaceutical forecasting: throwing darts?','https://pubmed.ncbi.nlm.nih.gov/24080692/','Nat Rev Drug Discov 2013;12:737–738; DOI10.1038/nrd4127','bibliographic record verified; Nature full text inaccessible this pass, no numerical result used')
for name in ['LUXTURNA','KEBILIDI','LENMELDY','VYJUVEK','FAYUVI']:
 row=next(r for r in screen if r['id'].startswith('CBER') and r['product'].startswith(name))
 src(name.lower()+'_fda','FDA '+name+' product approval record',row['source_url'],'Original approval letter date and indication section')
src('cder','FDA CDER original approval compilation, 1985–2025','https://www.fda.gov/drugs/drug-approvals-and-databases/compilation-cder-new-molecular-entity-nme-drug-and-new-biologic-approvals','2025 Compilation worksheet; source row locators retained','official structured frame read-only','sources/regulatory/fda_cder_1985_2025.xlsx')
src('cber','FDA approved cellular and gene therapy roster','https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/approved-cellular-and-gene-therapy-products','Current roster retrieved Nov.9 2026; 55 rows','official current roster, not historical census','sources/regulatory/fda_cell_gene_2026-11-09.html')

points=[]
for product,indication,date,year,f,a,fs,ats,quality in [
 ('Naglazyme','MPS VI','2004-01',2007,30,86.2,'werber04','bmrn07','A: original analyst-authored publication; scope incomplete'),
 ('Myozyme','Pompe','2004-01',2007,65,200.7,'werber04','genz07','A: original analyst-authored publication; scope incomplete'),
 ('Elaprase','MPS II','2004-01',2007,30,181.8,'werber04','shire07','A: original analyst-authored publication; scope incomplete'),
 ('Vimizim','MPS IVA','2013-11-21',2017,416,413.251,'vimforecast','vimactual','B: dated quotation of unspecified Bloomberg analysts'),
 ('Kanuma','LAL deficiency','2015-05-06',2020,603,117.9,'kanforecast','alxn20','B: dated Reuters quotation of Cortellis; not verified pure sell-side consensus')]:
 row=next(r for r in screen if r['product']==product)
 points.append(dict(id='NEW-'+product,pair=product+' / '+indication,product=product,forecast_date=date,forecast_date_precision='month' if len(date)==7 else 'day',approval_date=row['us_approval_date'],forecast_usdm=f,actual_usdm=a,target_year=year,forecast_source=fs,actual_source=ats,forecast_locator=sources[fs]['locator'],actual_locator=sources[ats]['locator'],forecast_geography='global inferred from context; not explicit in extracted estimate',actual_geography='worldwide reported product sales',forecast_revenue_basis='sales; net-versus-gross and revenue owner not fully specified',actual_revenue_basis='recognized net product sales',currency='nominal USD millions',pos=None,pos_status='unknown; no normalization applied',conditional_sales_usdm=None,stage='Phase III in source' if fs=='werber04' else 'near approval / late stage',vintage_stratum='earlier than primary window' if fs=='werber04' else 'later than primary window',horizon='single calendar target year; not 36 or 60 commercial months',later_indications='none identified in target-year product actuals; original expected age/phenotype scope still requires model',evidence_quality=quality,selection='regulator-derived / frozen mechanism priority; forecast access did not determine clinical inclusion',raw_actual_over_forecast_minus_1=a/f-1,break_even_scalar_pos=f/a if f<a else None,strict_36m_eligible=False,strict_60m_eligible=False,exclusion_reasons=['not a cumulative annual curve','risk basis unknown','geography/revenue basis incompletely matched','outside primary forecast-vintage window']))

werber_table=[]
for p,y03,y07,pre in [('Cerezyme',732,948,False),('Zavesca',1,27,False),('Fabrazyme',73,397,False),('Replagal',57,168,False),('Aldurazyme',12,204,False),('Myozyme',None,65,True),('I2S / Elaprase',None,30,True),('Aryplase / Naglazyme',None,30,True)]:
 werber_table.append(dict(product=p,estimated_2003_usdm=y03,estimated_2007_usdm=y07,preapproval_at_publication=pre,disposition='new preapproval target-year observation' if pre else 'already marketed at publication; excluded from preapproval sample',source='werber04',locator='Table1 p.10'))

cases=[]
def case(product,disease,cohort,relevance,dimensions,evidence,direction,belief,observed,mechanism,alternatives,transfer,missing,refs):
 cases.append(dict(product=product,disease=disease,cohort=cohort,relevance=relevance,dimensions=dimensions,forecast_evidence=evidence,commercial_direction=direction,preapproval_belief=belief,observed=observed,mechanism_hypothesis=mechanism,competing_explanations=alternatives,cmp_model_use=transfer,missing_data=missing,sources=refs,claim_status='Observed source facts distinguished from investigator mechanism/transfer hypotheses; not causal attribution'))
case('Spinraza','SMA','first approved targeted DMT','High for route and exposure; imperfect biology',
 ['CNS / motor-neuron disease','Early treatment and residual function','Genetic diagnosis','Repeated intrathecal ASO','Chronic revenue; competition'],
 'Reused dated Needham quotation; no matched annual curve','Mixed by horizon; long-target miss in one forecast',
 'Aug.1 2016 Needham quotation expected more than $5bn worldwide sales in 2022; this is one analyst, outside the primary vintage window.',
 'Biogen reported $1,793.5m in 2022. That is more than 64% below the quoted threshold; early launch enthusiasm is not evidence of long-run forecast accuracy.',
 'Initial prevalent-patient conversion and loading can accelerate early revenue; competing therapies and switches can reduce later product share.',
 'Do not conflate total SMA market growth with Spinraza revenue. Age, disease severity, newborn screening and intrathecal feasibility differ from SYNGAP1.',
 'Use a loading/maintenance cohort model, procedure capacity and competitor scenarios. Do not copy SMA efficacy or patient penetration into SYNGAP1.',
 'Original Needham model and primary-vintage reports; quarterly US/global patient starts, maintenance and switches; documented PoS treatment.',
 ['spin_forecast','biogen22','spin_label'])
case('Brineura','CLN2','first approved DMT','High for repeated CNS delivery and function preservation',
 ['Pediatric neurodegeneration','Irreversible loss / treatment timing','Enzyme/genetic diagnosis','Repeated ICV reservoir infusion','Chronic specialist-center treatment'],
 'Actual trajectory available; authentic preapproval annual curve missing','Not evaluable against a forecast',
 'No usable original preapproval annual model recovered. An undated or unspecified peak estimate cannot be converted into a launch curve.',
 'Reported global revenues rose from about $8.6m in 2017 to $39.9m in 2018, $72.0m in 2019 and $110.192m in 2020. These calendar years do not equal first 36 commercial months.',
 'A working delivery network and timely diagnosis can matter as much as prevalence. Preserving function and reversing lost development are distinct claims.',
 'CLN2 is degenerative; SYNGAP1 developmental impairment may have a different reversible component. ICV infusion is operationally different from lumbar intrathecal dosing.',
 'Use center activation, visits per patient, treatment delays and age/function strata; no numerical penetration transfer without matched patient data.',
 '2016–2017 original BioMarin models, forecast launch dates, quarterly early revenues and original label/center capacity history.',
 ['brin17','brin19','brin21'])
case('Mepsevii','MPS VII','first approved ERT','High for tiny identified population; low for CNS efficacy',
 ['Inherited metabolic disease','Heterogeneous severity/survival','Very small diagnosed pool','Chronic IV enzyme','Preapproval named-patient access'],
 'Actual and label evidence; preapproval annual curve missing','Not evaluable',
 'No usable annual sell-side forecast recovered; the case remains in the universe despite poor forecast access.',
 'Ultragenyx reported $0.5m product sales in 2017 including named-patient sales; the label does not establish CNS benefit.',
 'A few patients and the timing of paid access can materially change revenue in an ultra-small cohort.',
 'Free drug, compassionate access, country reimbursement and dosing by weight can mimic penetration changes. This is not evidence of a large latent population becoming commercial.',
 'Model counts and treated patient-months directly at the low end; retain uncertainty in genetic confirmation and access. Do not use peripheral ERT efficacy to predict neurological rescue.',
 '2016/2017 annual forecasts, original risk/geography assumptions, paid versus free access and quarterly country revenue.',
 ['mep_approval','mep17','meplabel'])
case('Naglazyme','MPS VI','first approved ERT','Medium-high for commercial patient finding',
 ['Somatic storage disorder','Chronic childhood-onset disease','Sparse centers / identification','Weekly IV enzyme','Global and weight-based exposure'],
 'New original analyst publication','Raw 2007 actual above forecast',
 'January 2004 SG Cowen-authored table: $30m sales for 2007. Risk and exact geography unspecified.',
 'BioMarin reported $86.2m in 2007, including $68.7m outside the US. Raw difference +187%; US sales alone derive to $17.5m.',
 'International rollout and patient access are candidate contributors. The contemporaneous forecast provides an earlier belief, not a complete patient/pricing model.',
 'If the forecast were US-only, the apparent beat would reverse. FX added $4.3m versus 2006; expected ex-US partnering versus direct sales could change recognized revenue.',
 'Supports testing geographic and revenue-owner assumptions. It cannot support a universal diagnosis multiplier or SYNGAP1 CNS-response assumption.',
 'Underlying SG Cowen annual model, expected territory rights/launch dates, probability treatment, net price and treated patients.',
 ['werber04','bmrn07'])
case('Myozyme','Pompe','first approved ERT','Medium; strong age/phenotype lesson',
 ['Muscle/respiratory enzyme deficiency','Infant survival vs late-onset disease','Genetic/enzyme identification','Chronic IV enzyme','International and weight-based exposure'],
 'New original analyst publication','Raw 2007 actual above forecast',
 'January 2004 SG Cowen-authored table: $65m in 2007, Phase III at publication.',
 'Genzyme reported $200.7m in 2007 versus $59.2m in 2006. Commercial rollout included multiple major territories; favorable FX contributed $4.3m versus 2006.',
 'Earlier/wider country access, patients treated, exposure and price are candidate mechanisms.',
 'Expected infant-versus-adult scope is unresolved. A later brand/manufacturing distinction with Lumizyme must not create an independent first-DMT observation.',
 'Separate incident early-treated children from older prevalent patients; allow efficacy, dose and reimbursement to differ. Do not assume neurological developmental rescue from muscle survival benefit.',
 'Original 2004/2005 model, age mix, country revenue, launch assumptions and original conditionality.',
 ['werber04','genz07'])
case('Elaprase','MPS II','first approved ERT','Medium; useful disconfirmation of diagnosis-only story',
 ['Somatic storage disorder with CNS manifestations','Heterogeneous cognitive disease','Known vs unrecognized patients','Weekly IV enzyme','Multiple territories / paid early access'],
 'New original analyst publication','Raw 2007 actual above forecast',
 'January 2004 analyst table: $30m in 2007. The same article described most estimated Hunter patients as already diagnosed.',
 'Shire reported $181.8m in 2007; its discussion credits a full US year, European launches and preapproval Latin American sales.',
 'Launch geography, conversion, dose and price deserve investigation before diagnosis expansion is credited.',
 'A raw sixfold ratio can also reflect risk weighting or forecasted timing. Systemic enzyme benefit does not establish cognitive efficacy.',
 'Distinguish diagnosed from accessible and willing to start; do not treat every historical sales beat as newly found patients.',
 'Original I2S/TKT model, Shire acquisition/territory assumptions, risk basis and forecast patient counts.',
 ['werber04','shire07'])
case('Vimizim','MPS IVA','first approved ERT','Medium; near-in-line commercial comparator',
 ['Somatic/skeletal storage disease','Irreversible skeletal burden','Rare diagnosis / centers','Weekly IV enzyme','Chronic global rollout'],
 'New dated secondary analyst quotation','Approximately in line on raw target year',
 'Nov.21 2013 article cited Bloomberg analysts expecting $416m annual sales in 2017, shortly before Feb.2014 approval.',
 'BioMarin reported $413.251m in 2017: raw difference −0.66%.',
 'A reasonably anticipated market/launch is possible; not every first enzyme launch produced a large positive surprise.',
 'An apparent match could conceal offsetting patient, price, geography and timing errors. Constituent analysts and risk basis remain unknown.',
 'Retain as a neutral countercase when reviewing the earlier ERT cluster; avoid treating commercial archetype alone as a forecast uplift.',
 'Bloomberg constituent models and timestamped annual consensus; approval-conditionality and geography.',
 ['vimforecast','vimactual'])
case('Kanuma','LAL deficiency','first approved ERT','High for patient-finding downside; medium biology fit',
 ['Infant severe vs later liver disease','Age/phenotype heterogeneity','Hidden patients / differential diagnosis','Chronic IV enzyme','Diagnosis investment and commercial priorities'],
 'New dated Cortellis quotation; primary actual and impairment evidence','Large raw shortfall',
 'Reuters May6 2015 cited Cortellis at $603m in 2020. The separately quoted company >$1bn ambition is not an analyst forecast.',
 'Alexion reported $117.9m in 2020: raw difference −80.45%. In 2020 it lowered long-term patient-growth assumptions and recorded a $2,042.3m intangible impairment.',
 'The filing directly describes patient-growth difficulty and reprioritization of commercial effort. A theoretically undiagnosed population need not become a treated population.',
 'The filing is retrospective and does not decompose the analyst gap. Territory, net price, pandemic disruption and original risk basis remain unresolved.',
 'Model diagnosis as a funded operational process with conversion losses, not a percentage that rises automatically. Include a slow-finding downside.',
 'Cortellis underlying forecast contributors, annual curves, geography/PoS; original patient-finding assumptions and longitudinal diagnosis-to-start conversion.',
 ['kanforecast','alxn20','kanimpair'])
case('Luxturna','RPE65 retinal dystrophy','first approved gene therapy for indication','High for viable tissue and delivery; low for recurring revenue',
 ['Monogenic loss of function','Residual viable tissue','Genetic eligibility','Subretinal surgery','One-time treatment / changing revenue owner'],
 'Primary label and early actual; forecast curve missing','Not evaluable',
 'No matched preapproval annual curve recovered. Disease prevalence is broader than eligible viable-retina patients.',
 'Spark reported $27.0m net product revenue in 2018; contract revenue is separate. Later ownership and territory rights complicate a consistent series.',
 'Procedure readiness, tissue eligibility and reimbursement can restrict conversion even with a causal therapy.',
 'One-time backlog depletion and royalty accounting differ from repeat ASO revenue. Limited public sales disclosure is not proof of weak demand.',
 'Use an eligibility and center-capacity funnel, but do not import one-time prices or cumulative-sales shape into CMP-002.',
 'Original 2016–2017 forecasts, territory-specific end-market sales after acquisition, procedures/patient and original tissue criteria.',
 ['luxturna_fda','lux18'])
case('Nulibry','MoCD-A','first approved replacement DMT','High for diagnostic urgency; weaker size and route fit',
 ['Metabolic neonatal neurologic injury','Very early irreversible injury','Urgent genetic confirmation','Daily IV replacement','Extremely small incident cohorts'],
 'Original FDA label; annual analyst forecast missing','Not evaluable',
 'Prior investigational cPMP exposure must inform launch conversion but does not automatically disqualify a first approved therapy.',
 'Original label targets mortality risk and daily IV administration; it permits initiation for presumed disease with genetic confirmation required.',
 'Timing of diagnosis can determine clinical opportunity, not merely how quickly a commercially eligible backlog is captured.',
 'A neonatal survival window is much narrower than the currently studied SYNGAP1 age range. Severe historical mortality changes prevalent-pool arithmetic.',
 'Use to challenge assumptions about reversible function and incident versus prevalent patients; no transferable penetration percentage is established.',
 '2019–2021 fosdenopterin/BridgeBio models, paid-versus-investigational patients, incident diagnoses and reported product economics.',
 ['nul21'])
case('Lenmeldy','MLD','prior-HSCT boundary; first approved gene therapy','High for treatment window; commercially immature',
 ['Pediatric neurologic degeneration','Presymptomatic/early symptomatic only','Diagnosis before loss of opportunity','Autologous cells plus conditioning','One-time manufacture/capacity'],
 'FDA indication/date; no mature forecast test','Immature',
 'Original approval in March2024 cannot yield 36 commercial months by this study date.',
 'Indication specifies presymptomatic late-infantile, presymptomatic early-juvenile or early-symptomatic early-juvenile children.',
 'Earlier genetic identification may expand the treatable window rather than unlock all older diagnosed patients.',
 'HSCT precedent and ex-vivo manufacturing prevent clean first-treatment or operational equivalence to CMP-002.',
 'Build age/function eligibility explicitly; keep developmental benefit separate from symptom control.',
 'Preapproval Orchard/Kyowa models, initial-label eligible population, manufactured/infused patients and territory timing.',
 ['lenmeldy_fda'])
case('Kebilidi','AADC deficiency','first approved targeted US candidate; prior-care sensitivity','High for genetic CNS restoration; immature',
 ['Monogenic CNS neurotransmitter defect','Motor milestones / age','Genetic identification','Intraputaminal gene delivery','One-time neurosurgical exposure'],
 'FDA record; no mature forecast test','Immature',
 'Approval November2024 is too recent for the primary sales horizon. Earlier symptomatic/neurotransmitter care requires explicit review.',
 'FDA indicates adult and pediatric AADC deficiency. No mature cumulative accuracy estimate is available here.',
 'Residual developmental capacity and specialist procedural delivery are clinically relevant hypotheses.',
 'Gene addition to specific brain regions, one-time surgery and AADC biology differ from repeat regRNA-targeting ASO therapy.',
 'Use efficacy and delivery dimensions separately; do not convert motor milestone data into a SYNGAP1 commercial response rate.',
 'PTC preapproval annual models, original label/review, country-specific treatment starts, reimbursement and procedure capacity.',
 ['kebilidi_fda'])
case('Myalept','Generalized lipodystrophy','first replacement candidate; prior metabolic care','High for net price and narrow eligibility',
 ['Causal hormone deficiency','Phenotype-specific eligibility','Generalized vs partial disease','Daily subcutaneous replacement','Payer mix / rebates'],
 'Primary operational/GTN evidence; annual forecast missing','Not evaluable',
 'A broader lipodystrophy population cannot be equated with the US generalized-disease market.',
 'Aegerion disclosed approximately 30% 2015 US gross-to-net adjustments in a preliminary update, with 27 percentage points attributable to Medicaid rebates.',
 'Payer mix and price history can dominate WAC-to-revenue conversion even in a rare replacement therapy.',
 'This single-product, historical estimate is not a contemporary ASO discount benchmark; rights transfers and accounting also matter.',
 'Model net revenue by payer and territory; use 15% or another GTN only as a justified CMP assumption, not an orphan-drug constant.',
 '2013–2014 Amylin/BMS/AstraZeneca analyst models, original population scope and payer/price assumptions.',
 ['myalept15','myaleptgt'])
case('Arcalyst','CAPS','first approved disease-targeted candidate with prior off-label blockade','Medium for competition and revenue recognition',
 ['Inflammatory genetic syndrome','Rapid symptom/inflammation response','Small diagnosed specialty pool','Repeated subcutaneous drug','Prior off-label care / fast follower'],
 'Primary actuals; original annual forecast missing','Not evaluable',
 'Prior off-label anakinra and subsequent Ilaris prevent a simple untreated-to-monopoly narrative.',
 'Regeneron reported $6.3m, $18.4m and $25.3m in 2008–2010; 2010 included $4.8m of deferred sales recognition.',
 'Accounting and conversion from free/clinical supply can distort revenue ramps independently of new patient demand.',
 'Later pericarditis revenue must not be attributed to CAPS. Different efficacy and administration choices affect competition.',
 'Separate starts, paid treatment and recognized revenue; keep competitors in the adoption model.',
 '2007 Regeneron/Arcalyst annual models, deferred-revenue schedule and CAPS-only sales through later indications.',
 ['arc10'])
case('Kuvan','PKU','boundary: prior disease-modifying diet','Medium for responder fraction and existing care',
 ['Biochemical pathway modulation','Longstanding preventable neurodevelopmental injury','Newborn-screened diagnosed population','Chronic oral drug','Response testing / prior diet'],
 'Clinical screen only in new pass','Not evaluable',
 'Diet already altered disease course, so first approved drug does not mean first DMT under a care-inclusive definition.',
 'Candidate retained to test whether response-defined eligibility and established care make apparent TAM misleading; no new forecast error estimated.',
 'Biochemical responsiveness and willingness to change existing treatment can be more important than prevalence.',
 'Early-screened PKU diagnosis economics are unlike underdiagnosed SYNGAP1; oral administration is easier than intrathecal dosing.',
 'Model biologically responsive and clinically eligible fractions separately from diagnosis and penetration.',
 'Original 2006–2007 sapropterin forecasts, response-testing assumptions and BioMarin/Merck territory economics; verify original care evidence before quantitative use.',
 ['cder'])
case('Dojolvi','LC-FAOD','boundary: prior diet/MCT and compassionate triheptanoin','Medium for paid-access conversion',
 ['Metabolic substrate provision','Heterogeneous severity','Known patients / metabolic centers','Oral nutritional administration','Compassionate-to-commercial transition'],
 'Clinical screen only in new pass','Not evaluable',
 'First approved formulation differs from first available disease-targeted intervention.',
 'Retained despite lack of a new matched annual forecast; initial-label and exposure adjudication remains open.',
 'Conversion of existing users and payer willingness to reimburse an approved product can shape launch revenue.',
 'Switching from prior nutritional care is distinct from creating access to a new CNS mechanism. Adherence metrics may have different meaning.',
 'Track previously treated, free-access and genuinely new patients separately.',
 '2019–2020 Ultragenyx models, paid transition counts and original-label dietary comparator; verify clinical first-status boundary.',
 ['cder'])
case('Ztalmy','CDKL5 deficiency disorder','adjacent disease-specific antiseizure treatment','High commercial-clinic fit; not established DMT',
 ['Genetic developmental epilepsy','Seizure outcome vs development','Genetic testing / claims identification','Chronic oral suspension','Caregiver tolerance and persistence'],
 'Primary operational metrics; usable preapproval curve missing','Not evaluable',
 'An antiseizure approval should not be reclassified as developmental disease modification. Multi-indication ganaxolone forecasts are excluded.',
 'Marinus disclosed $19.6m US net revenue in 2023 and >165 active patients at year-end; it described greater use of third-party data for patient targeting.',
 'Specialist reach and caregiver-supported initiation are observable commercial processes; patient lists are not treated patients.',
 'Company targeting counts are not validated prevalence. Annual revenue divided by a year-end count is not annual net price per patient.',
 'Use diagnosis-to-referral-to-prescription-to-start-to-persistence transitions, with explicit oral versus procedure burden.',
 '2021/early2022 CDD-only models, competing indication allocations, paid patient-months, discontinuation and GTN.',
 ['ztalmy23','ztalmy24'])
case('Daybue','Rett','adjacent disease-specific therapy; DMT uncertain','High for caregiver adoption and tolerability',
 ['Neurodevelopmental syndrome','Symptom/functional endpoints','Diagnosed pediatric/adult pool','Chronic oral treatment','Tolerability / continuation'],
 'Reused actuals and label; no strict cumulative forecast','Not evaluable on primary endpoint',
 'First Rett approval is not equivalent to proof of genetic disease modification. Existing analyst peak quotations do not provide a cumulative curve.',
 'Reported product revenue was $177.2m in 2023, $348.4m in 2024 and $391.4m in 2025. Initiation, tolerability and sustained use need separate evidence.',
 'The early prevalent backlog and later continuation may drive different phases of the curve.',
 'New territories, formulation changes and follow-up length can confound apparent persistence. Oral experience cannot fix intrathecal willingness.',
 'Model starts and continuing treated patient-months separately; do not apply a single adherence factor twice.',
 'Preapproval 2022–2023 curves, label/geography assumptions, cohort continuation with consistent denominators and paid dispensing.',
 ['day_fda','day_label','day24','day25'])
case('Miplyffa','NPC','boundary: prior miglustat / same-era new entrants','Medium clinical context; immature',
 ['Inherited neurodegeneration','Function preservation','Diagnostic delay','Oral combination with miglustat','Prior off-label care / close competitor'],
 'Regulatory screen; no mature forecast test','Immature',
 'First US NPC approval does not erase earlier European/off-label miglustat treatment.',
 'September2024 original approval is too recent for 36-month actuals; Aqneursa followed within days.',
 'Combination treatment and close competition make product share distinct from disease-level treatment uptake.',
 'Cross-country care and labeling differ; pooling all NPC brands would change the unit of analysis.',
 'Maintain a disease-market model and a separate CMP share model; no assumption of permanent first-mover exclusivity.',
 'Preapproval NPC-only curves, original label and prior-care sources, combination costs and competitor switches.',
 ['cder'])
case('Qalsody','SOD1 ALS','boundary: prior ALS DMTs; genotype-targeted ASO','High modality fit; low age/biology match',
 ['Adult neurodegeneration','Rapid irreversible loss','Genotype-specific fraction','Repeated intrathecal ASO','Accelerated biomarker approval'],
 'Regulatory screen; no matched annual forecast','Not evaluable',
 'First SOD1-directed therapy differs from first ALS DMT. Biomarker evidence and demonstrated functional benefit must remain separate.',
 '2023 approval allows only limited mature follow-up; this pass does not recover a matched cumulative curve or separate reported product economics.',
 'Diagnostic genotype confirmation, uncertain perceived benefit and repeated procedures can affect adoption.',
 'Adult ALS survival and motor-neuron disease are distant from childhood SYNGAP1 developmental trajectories.',
 'Use route/modality operational questions and surrogate-versus-clinical evidence gates; do not transfer ALS survival or uptake.',
 '2022/early2023 tofersen models, conditionality, paid patient exposure and original accelerated-approval evidence.',
 ['cder'])

gaps=[
 dict(stratum='Non-NME / repurposed approvals',examples=['Fintepla','Ravicti','Procysbi','Cystadrops'],status='not exhaustively reconciled',effect='Original NME frame can miss first rare indications; examples mostly symptomatic/followers but cannot assume all omitted drugs are ineligible.'),
 dict(stratum='No original orphan designation',examples=[],status='544 primary-period CDER rows retained separately',effect='No designation is not proof of non-rarity. Review required before claiming a complete rare-disease population.'),
 dict(stratum='OOPD approval universe',examples=[],status='export failed; search form retained',effect='Cannot quantify omitted non-NME/supplement approvals or statutory cost-recovery-exception prevalence.'),
 dict(stratum='CBER historical withdrawals / non-cell-gene biologics',examples=[],status='current roster only',effect='Not a complete historical biologics census. Retain named withdrawal controls in CDER and reconcile archival biologics before population inference.'),
 dict(stratum='Outside focused clinical scope',examples=['rare infections','acute rescue','benign tumor interventions'],status='explicit exclusions beyond original oncology exclusion',effect='No generalized conclusion about all orphan drugs follows.'),
]
population_context=[
 dict(disease='SYNGAP1',date='2024-03-31',geography='worldwide',count=1400,measure='advocacy-network census of known patients',status='observed report of counted patients, not prevalence',source='syngap_census'),
 dict(disease='SYNGAP1',date='2024 report context',geography='US',count=401,measure='patients counted in source discussion',status='observed report; neither current diagnosis total nor commercially eligible count',source='syngap_census'),
 dict(disease='MPS VI',date='2004-01',geography='worldwide',count=1100,measure='historical estimated affected population',status='analyst belief at forecast vintage, not current epidemiology or accessible patients',source='werber04'),
 dict(disease='MPS II',date='2004-01',geography='worldwide',count=2000,measure='historical estimated affected population',status='analyst belief at forecast vintage; article describes most as diagnosed',source='werber04'),
 dict(disease='Pompe',date='2004-01',geography='worldwide',count=None,range=[5000,10000],measure='historical estimated affected population',status='analyst belief at forecast vintage; expected eligible age mix unresolved',source='werber04'),
 dict(disease='CDKL5 / Ztalmy',date='2023-12-31',geography='US commercial context',count=165,comparison='greater than',measure='active patients on product',status='company-reported treatment count, not disease prevalence or annual patient-years',source='ztalmy23'),
]
for x in cases:
 hits=[r for r in screen if r['product'].split(' (')[0].lower()==x['product'].lower()]
 x['original_us_approval_date']=hits[0]['us_approval_date'] if hits else None
 x['accessible_us_patient_population']=None
 x['population_matching_status']='Not independently quantified on consistent date/label/territory basis; no numerical TAM-distance score assigned.'
 x['population_evidence']=[p for p in population_context if p['disease']==x['disease'] or p['disease'].startswith(x['disease']+' /')]
dictionary={
 'unit':'Drug–indication pair; raw frame rows are approvals/products, not independent forecast outcomes.',
 'classification':'Provisional clinical scope/first-status screen; does not certify scientific DMT status.',
 'source_locator':'Worksheet row or document table/section; raw source preserved where feasible.',
 'null':'Unknown/not obtained, never zero.',
 'forecast_usdm':'Observed quoted nominal USD millions, without imputed PoS correction.',
 'actual_usdm':'Observed recognized net product revenue; consolidated worldwide unless specified.',
 'raw_actual_over_forecast_minus_1':'Derived A/F−1; positive means raw actual exceeds quoted forecast. Not normalized forecast bias.',
 'break_even_scalar_pos':'Hypothetical F/A where F=p×conditional forecast; not an estimate of actual approval probability.',
 'strict_36m_eligible':'Requires complete matched first 36 commercial months, original disease, geography, revenue basis, currency, vintage and known conditionality.',
 'dimensions':'Investigator qualitative relevance on biology, age/window, diagnosis, administration and exposure; no outcome-fitted composite score.',
 'commercial_direction':'Unknown unless target-specific evidence exists. Immaturity/access gaps are not commercial failures.',
 'source_reuse':'Marked where earlier verified evidence is used after independent case selection.',
 'knowledge_time':'Preapproval forecast beliefs are separated from subsequent company explanations and investigator hypotheses.',
}
payload=dict(as_of='2026-11-09',question='Do preapproval forecasts systematically underestimate approval-conditional revenue for first rare-disease DMTs?',status='Exploratory source-independent reconstruction; primary matched sample unavailable',protocol_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'protocol').glob('*.txt'))},frame_counts=dict(Counter(r['classification'] for r in screen)),sources=sources,new_target_year_comparisons=points,complete_werber_table=werber_table,cases=cases,population_context=population_context,coverage_gaps=gaps,data_dictionary=dictionary,strict_36m_N=0,strict_60m_N=0,pooled_bias_estimate=None,pooled_beat_rate=None)
(OUT/'evidence.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
def export_csv(name,rows,fields):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
  for r in rows:w.writerow({k:json.dumps(r.get(k),ensure_ascii=False) if isinstance(r.get(k),(list,dict)) else r.get(k) for k in fields})
export_csv('forecast_actuals.csv',points,list(points[0]))
export_csv('analogue_matrix.csv',cases,['product','disease','original_us_approval_date','cohort','relevance','dimensions','accessible_us_patient_population','population_matching_status','forecast_evidence','commercial_direction','cmp_model_use','missing_data','sources'])
export_csv('approval_screen.csv',screen,['id','product','us_approval_date','classification','reason','classification_status','priority','source','source_locator'])
print(f'{len(cases)} case dossiers; {len(points)} new target-year observations; {len(sources)} sources; strict N=0')
