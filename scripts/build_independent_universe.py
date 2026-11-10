"""Outcome-independent classification of the frozen FDA frame.

Clinical judgments are explicitly provisional except where deep-dive sources adjudicate them.
No prior deck or historical forecast data is read by this script.
"""
from pathlib import Path
import json,re,html
from datetime import datetime
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'data/independent'
frame=json.loads((OUT/'cder_full_frame.json').read_text())
groups={
'first_approved_dmt_candidate': {
'Nulibry':'MoCD-A; first approved cPMP replacement. Prior investigational treatment within development is a launch-bridge issue, not automatic disqualification from first-DMT status.',
'Fabrazyme':'Fabry disease; first US enzyme replacement. Earlier European agalsidase approvals require geography discipline.',
'Naglazyme':'MPS VI; first approved enzyme replacement. Somatic benefit is not evidence of CNS rescue.',
'Myozyme':'Pompe disease; first approved enzyme replacement. Infantile and late-onset cohorts differ; later Lumizyme brand must reconcile.',
'Elaprase':'MPS II; first approved enzyme replacement. Peripheral exposure does not establish cognitive benefit.',
'Increlex':'Severe primary IGF-1 deficiency; first targeted replacement candidate. Growth endpoint and prior GH treatment limit analogy.',
'Kalydeco':'G551D CF; first CFTR modulator, not first care capable of improving CF outcomes. Expanded genotypes require separation.',
'Vimizim':'MPS IVA; first approved enzyme replacement. Endurance response and irreversible skeletal disease matter.',
'Myalept':'Generalized lipodystrophy; replacement of deficient leptin. Existing metabolic drugs and diet; US excludes partial disease.',
'Strensiq':'Pediatric-onset HPP; first approved enzyme replacement. Age at onset differs from age at treatment.',
'Kanuma':'LAL deficiency; first approved enzyme replacement. Infant survival and adult liver disease are different profiles.',
'Spinraza':'SMA; first approved SMN-targeted DMT. Age, motor-neuron reserve, loading and chronic intrathecal maintenance.',
'Brineura':'CLN2; first approved treatment slowing ambulation loss. Repeat ICV infusions, not lumbar intrathecal injections.',
'Mepsevii':'MPS VII; first approved enzyme replacement. CNS efficacy not established; exceptionally small identified population.',
'Oxervate':'Neurotrophic keratitis; restorative corneal healing candidate, but prior surgery/supportive treatment and finite course.',
'Zokinvy':'HGPS and specified processing-deficient progeroid laminopathies; survival benefit. Multiple initial subpopulations must retain scope.',
'Voxzogo':'Achondroplasia; pathway-targeted growth intervention. Epiphyseal window and long-term clinical outcomes require qualification.',
'Xenpozyme':'ASMD; first approved enzyme replacement for non-CNS manifestations.',
'Skyclarys':'Friedreich ataxia; first approved disease-targeted treatment. Functional evidence, not genetic correction.',
'Sohonos':'FOP; reduces new heterotopic ossification. Skeletal maturity/age restrictions; prevention differs from reversal.',
'Xolremdi':'WHIM; first approved targeted treatment candidate. Prior G-CSF and immunoglobulin must be considered.',
'Kygevvi':'TK2 deficiency; nucleotide replacement, pediatric-onset scope. Earlier compassionate use and immature follow-up.',
'Forzinity':'Barth syndrome; first approved treatment candidate under accelerated approval. DMT status remains uncertain from muscle-strength surrogate.',
},
'boundary_prior_disease_modifying_care': {
'Orfadin':'HT1; nitisinone plus dietary restriction. Diet and liver transplant preceded approval.',
'Aldurazyme':'MPS I; first approved ERT, but HSCT was disease modifying and remains crucial for severe CNS disease.',
'Soliris':'PNH; first approved complement DMT, but HSCT can be curative. aHUS and later diseases contaminate mature product sales.',
'Kuvan':'PKU; first drug, but dietary Phe control was established disease-modifying care. Response subset and geography rights matter.',
'Arcalyst':'CAPS; first approved IL-1 therapy candidate, but off-label anakinra preceded it; Ilaris followed.',
'Carbaglu':'NAGS deficiency; targeted metabolic replacement candidate with prior protein restriction and ammonia scavengers.',
'Gattex':'SBS; intestinal adaptation DMT candidate; somatropin, nutritional rehabilitation and transplant preceded it.',
'Cholbam':'Bile acid synthesis disorders and specified peroxisomal disorders; earlier bile-acid use and multiple initial subgroups.',
'Xuriden':'Hereditary orotic aciduria; first approved formulation; prior uridine replacement precludes treatment-naive natural experiment.',
'Natpara':'Hypoparathyroidism; first approved PTH replacement but calcium/vitamin D and off-label PTH preceded it.',
'Defitelio':'Post-HSCT VOD with renal/pulmonary dysfunction; acute inpatient rescue, weak chronic-CNS commercial analogy.',
'Exondys 51':'DMD exon 51; first approved exon-skipping therapy, but corticosteroids already altered course. Accelerated surrogate approval.',
'Crysvita':'XLH; first anti-FGF23 drug, but phosphate/active vitamin D were disease-targeted care. Later TIO excluded.',
'Onpattro':'hATTR polyneuropathy; first US RNAi DMT, but transplant and off-label stabilizers preceded it; European tafamidis already approved.',
'Gamifant':'Primary HLH; first targeted approved antibody candidate, but immunochemotherapy and HSCT preceded it.',
'Cablivi':'aTTP; first specific approved drug, but plasma exchange and immunosuppression altered course.',
'Vyndaqel':'ATTR cardiomyopathy; first approved for this phenotype; transplant/off-label stabilizers and mixed hereditary/wild-type cases.',
'Givlaari':'AHP; chronic RNAi prophylaxis, but hemin and transplant are meaningful prior disease-targeted interventions.',
'Tepezza':'Thyroid eye disease; first approved targeted drug, but immunosuppression and surgery predated it.',
'Koselugo':'NF1 plexiform neurofibromas; first approved targeted therapy; benign tumor mechanism adjacent, surgery and mixed future scopes.',
'Dojolvi':'LC-FAOD; first approved triheptanoin product, but diet/MCT and compassionate use preceded it.',
'Oxlumo':'PH1; first RNAi drug, but pyridoxine-responsive disease and liver/kidney transplant preceded it.',
'Imcivree':'POMC/PCSK1/LEPR obesity; first pathway-targeted candidate; original genotype groups and later BBS/hypothalamic indications must separate.',
'Enjaymo':'Cold agglutinin disease; first approved complement drug, but rituximab-based disease treatment preceded it.',
'Pyrukynd':'PK deficiency; first approved activator, but transfusion/splenectomy and HSCT preceded it.',
'Camzyos':'Obstructive HCM; first myosin inhibitor, but surgery and established pharmacologic care preceded it.',
'Lamzede':'Alpha-mannosidosis non-CNS disease; first approved ERT, but HSCT precedent and CNS limitation.',
'Joenja':'APDS; first approved PI3Kdelta therapy, but sirolimus/HSCT can modify disease.',
'Qalsody':'SOD1 ALS; first genotype-targeted ASO but riluzole and edaravone predate it. Accelerated NfL endpoint.',
'Veopoz':'CHAPLE; first approved targeted complement drug, but off-label eculizumab disease control preceded it.',
'Miplyffa':'NPC neurological manifestations; first US approval in combination with miglustat; off-label/European miglustat already disease targeted.',
'Tryngolza':'FCS; first US APOC3-targeted approval, but strict diet and European volanesorsen preceded it.',
'Yartemlea':'Transplant-associated TMA; first approved targeted candidate, but supportive changes/off-label complement blockade; acute setting.',
},
'adjacent_symptomatic_or_dmt_uncertain': {
'Xiaflex':'Dupuytren contracture; enzymatic tissue remodeling with prior corrective surgery. Adjacent, weak fit to genetic CNS DMT.',
'Xyrem':'Narcolepsy cataplexy; symptom control, established earlier treatments.',
'Xenazine':'Huntington chorea; symptom control, not demonstrated neurodegeneration modification.',
'Hetlioz':'Non-24; circadian entrainment; not an underlying genetic CNS rescue analogue.',
'Scenesse':'EPP phototoxicity; photoprotection rather than correction of underlying heme disorder.',
'Bylvay':'PFIC pruritus at initial approval; clinical disease-course effects require separate evidence.',
'Livmarli':'Alagille pruritus at initial approval; do not retroactively call launch evidence disease modifying.',
'Ztalmy':'CDKL5 seizure treatment; no established developmental disease modification at approval.',
'Daybue':'Rett; disease-specific symptom/functional evidence, DMT classification uncertain.',
'Firdapse':'LEMS symptom transmission; earlier compounded amifampridine and disease-directed immunotherapy.',
'Filsuvez':'DEB/JEB wound treatment; tissue healing, not systemic correction; Vyjuvek preceded DEB component.',
'Crenessity':'CAH androgen control; adjunct to established glucocorticoid replacement.',
'Esbriet':'IPF antifibrotic; same-day first approvals with Ofev, cannot assume solitary first entrant.',
'Ofev':'IPF antifibrotic; same-day first approvals with Esbriet; later ILD indications contaminate sales.',
'Spevigo':'GPP flare control; first specific targeted approval candidate with prior systemic therapies.',
'Sylvant':'Idiopathic multicentric Castleman disease; prior immunotherapy; remote biology/commercial setting.',
},
'follower_or_established_alternative': {
'Tracleer':'Earlier epoprostenol for PAH.', 'Remodulin':'Earlier epoprostenol and bosentan for PAH.',
'Somavert':'Earlier surgery/somatostatin analogs for acromegaly.', 'Zavesca':'Earlier Gaucher ERT.',
'Ventavis':'Earlier PAH disease treatments.', 'Iplex':'Increlex approved earlier in 2005.',
'Exjade':'Earlier iron chelation.', 'Letairis':'Earlier PAH therapies.', 'Somatuline Depot':'Earlier acromegaly therapies.',
'Nplate':'Earlier ITP immunomodulation/splenectomy.', 'Promacta':'Earlier ITP care and Nplate.',
'Ilaris':'Arcalyst preceded CAPS approval; later indications confound product sales.',
'Kalbitor':'C1 inhibitor and other HAE treatments predate it.', 'Vpriv':'Ceredase/Cerezyme predate it.',
'Lumizyme':'Same active enzyme as Myozyme, brand/age/manufacturing distinction, not independent first DMT.',
'Krystexxa':'Earlier urate-lowering treatment; refractory-population comparator.',
'Firazyr':'Earlier HAE therapies.', 'Ferriprox':'Earlier chelation.', 'Elelyso':'Earlier Gaucher ERT.',
'Signifor':'Prior surgery and endocrine drug treatment.', 'Juxtapid':'Earlier HoFH lipid-lowering/apheresis.',
'Kynamro':'Earlier HoFH care and Juxtapid.', 'Adempas':'Mixed PAH/CTEPH; prior PAH drugs and pulmonary endarterectomy.',
'Opsumit':'Earlier PAH agents.', 'Cerdelga':'Earlier Gaucher therapies.', 'Orkambi':'Kalydeco earlier; genotype expansion.',
'Uptravi':'Earlier PAH agents.', 'Ocaliva':'UDCA preceded PBC approval.', 'Emflaza':'Longstanding off-label steroids; Exondys already approved.',
'Austedo':'Xenazine earlier; symptomatic.', 'Radicava':'Riluzole earlier.', 'Hemlibra':'Prior factor/bypass therapy in hemophilia.',
'Symdeko':'Earlier CFTR modulators.', 'Tavalisse':'Earlier ITP therapies.', 'Palynziq':'Diet and Kuvan earlier.',
'Galafold':'Fabrazyme earlier.', 'Takhzyro':'Earlier HAE prophylaxis.', 'Revcovi':'Adagen earlier.',
'Tegsedi':'Onpattro earlier in US; transplant/stabilizer care earlier.', 'Ultomiris':'Soliris earlier.',
'Wakix':'Earlier symptomatic narcolepsy therapies.', 'Trikafta':'Earlier CFTR modulators.',
'Reblozyl':'Earlier transfusion/HSCT; later MDS not eligible for original thalassemia-only comparison.',
'Adakveo':'Hydroxyurea earlier; retain discontinued/negative outcomes as controls.',
'Oxbryta':'Hydroxyurea earlier; withdrawn therapy retained as a control, not deleted for failure.',
'Vyondys 53':'Earlier DMD care and exon-skipping class.', 'Isturisa':'Earlier endocrine treatment.',
'Uplizna':'Soliris NMOSD approval and off-label immunotherapy earlier.',
'Evrysdi':'Spinraza and Zolgensma earlier.', 'Viltepso':'Earlier DMD treatments.',
'Enspryng':'Soliris/Uplizna earlier.', 'Orladeyo':'Earlier HAE prophylaxis.',
'Evkeeza':'Earlier HoFH drugs/apheresis.', 'Amondys 45':'Earlier DMD treatments.',
'Empaveli':'Soliris/Ultomiris earlier.', 'Rezurock':'Earlier GVHD immunosuppression/approved treatment.',
'Nexviazyme':'Earlier Pompe ERT.', 'Skytrofa':'Earlier GH replacement.', 'Tavneos':'Earlier ANCA vasculitis immunosuppression.',
'Vyvgart':'Earlier gMG immunotherapies/approved complement inhibition.',
'Amvuttra':'Onpattro earlier.', 'Relyvrio':'Riluzole/edaravone earlier; withdrawn therapy retained as a control.',
'Filspari':'Earlier IgAN care and Tarpeyo; accelerated endpoint at initial approval.',
'Rystiggo':'Earlier gMG drugs.', 'Ngenla':'Earlier GH replacement.', 'Pombiliti':'Earlier Pompe ERT.',
'Rivfloza':'Oxlumo earlier.', 'Zilbrysq':'Earlier gMG treatment.', 'Agamree':'Earlier DMD steroids and targeted drugs.',
'Fabhalta':'Earlier PNH therapies; later renal diseases excluded.', 'Wainua':'Earlier hATTR drugs.',
'Duvyzat':'Earlier DMD DMT/corticosteroids.', 'Winrevair':'Earlier PAH treatment; new class not first DMT.',
'Voydeya':'Add-on to approved PNH therapy.', 'Iqirvo':'UDCA/Ocaliva earlier.', 'Piasky':'Earlier PNH therapies.',
'Yorvipath':'Natpara and calcium/vitamin D earlier.', 'Livdelzi':'Earlier PBC therapies.',
'Niktimvo':'Earlier GVHD therapies.', 'Aqneursa':'Miplyffa approved four days earlier; prior miglustat.',
'Hympavzi':'Earlier hemophilia replacement/prophylaxis.', 'Attruby':'Tafamidis earlier.',
'Alhemo':'Earlier hemophilia treatments.', 'Alyftrek':'Earlier CFTR modulators.',
'Gomekli':'Koselugo earlier for pediatric NF1 PN.', 'Qfitlia':'Earlier hemophilia care.',
'Imaavy':'Earlier gMG therapies.', 'Andembry':'Earlier HAE prophylaxis.', 'Ekterly':'Earlier HAE rescue.',
'Sephience':'Diet/Kuvan/Palynziq earlier.', 'Dawnzera':'Earlier HAE prophylaxis.',
'Wayrilz':'Earlier ITP treatments.', 'Palsonify':'Earlier acromegaly therapies.',
'Jascayd':'Esbriet/Ofev earlier.', 'Redemplo':'Tryngolza earlier in US.', 'Myqorzo':'Camzyos and established care earlier.',
'Repatha':'HoFH component follows earlier lipid-lowering drugs.',
}}
lookup={k:(group,reason) for group,d in groups.items() for k,reason in d.items()}
symptoms={'Myobloc','Dysport','Apokyn','Banzel','Qutenza','Ampyra','Onfi','Northera','Epidiolex','Diacomit','Sabril','Sunosi'}
infection=re.compile(r'malaria|tuberculosis|anthrax|leishmaniasis|cryptosporidium|giardia|amebi|chagas|onchocerciasis|smallpox|fascioliasis|ebola|trypanosomi|cytomegalovirus|candidiasis|aspergillosis|mucormycosis|HIV-1',re.I)
support={'Zometa','Extraneal','Radiogardase','ChiRhoStim','NutreStore','Nulojix','Voraxaze','Praxbind','Macrilen','Omegaven','TissueBlue','NexoBrid','Terlivaz','Xermelo'}
manual_onc={'Poteligeo','Copiktra','Turalio','Ogsiveo'}
priority={'Brineura','Spinraza','Mepsevii','Naglazyme','Vimizim','Kanuma','Luxturna','Kuvan','Myalept','Arcalyst','Dojolvi','Ztalmy','Daybue','Nulibry','Kebilidi','Lenmeldy','Miplyffa','Qalsody'}
historical={'Adagen','Ceredase','Cerezyme','Cystagon','Cystadane','Ucephan','Buphenyl','Sucraid','Rilutek','Pulmozyme','Flolan','Actimmune','Betaseron'}
ledger=[]
for r in frame:
 name=r['Proprietary  Name']; group=r['initial_screen']; reason=group
 if group=='outside_primary_period' and name in historical: group='historical_extension'; reason='Pre-2000 landmark/prior-care comparator; not pooled with primary period.'
 elif group not in {'outside_primary_period','not_orphan_designated_at_original_approval'}:
  if name in lookup: group,reason=lookup[name]
  elif name in manual_onc or group=='oncology_or_tumor_candidate_review': group='excluded_oncology_tumor_or_support'; reason='Orphan oncology/tumor/supportive setting kept outside primary chronic rare-DMT cohort.'
  elif name in symptoms: group='excluded_symptomatic_followers'; reason='Established symptomatic treatment class; not first disease-modifying therapy.'
  elif infection.search(r['indication_at_approval']): group='excluded_infectious_disease'; reason='Acute infection/anti-infective treatment outside genetic/metabolic/chronic rare-DMT scope; often established treatment alternatives.'
  elif name in support or any(z in r['indication_at_approval'].lower() for z in ['internal contamination','diagnosis of','organ rejection','selectively stain']): group='excluded_supportive_diagnostic_or_acute'; reason='Diagnostic/supportive/acute or established treatment setting, weak fit to chronic first-DMT estimand.'
  else: group='unresolved_screen'; reason='Requires manual clinical adjudication; not silently excluded.'
 date=r['FDA Approval Date']
 if isinstance(date,str) and '/' in date:
  try: date=datetime.strptime(date,'%m/%d/%Y').date().isoformat()
  except ValueError: pass
 ledger.append({'id':r['frame_id'],'product':name,'ingredient':r['Active Ingredient/Moiety'],'indication':r['indication_at_approval'],'us_approval_date':date,'orphan_status':r['Orphan Drug Designation'],'classification':group,'reason':reason,'classification_status':'provisional clinical screen; regulator confirms indication/date, not first-DMT judgment','priority': 'deep_dive' if name in priority else 'screen_only','source':'FDA-CDER-2025','source_locator':r['source_locator'],'route':r['Route of Administration(1)'],'forecast_status':'not used for inclusion; assess separately'})
# The live CBER roster includes 2026 additions; preserve all entries and classify explicitly.
raw=(ROOT/'sources/regulatory/fda_cell_gene_2026-11-09.html').read_text()
table=re.findall(r'<table\b.*?</table>',raw,re.S|re.I)[0]
for idx,tr in enumerate(re.findall(r'<tr\b.*?</tr>',table,re.S|re.I)[1:],1):
 cells=re.findall(r'<td\b.*?</td>',tr,re.S|re.I)
 if not cells: continue
 text=html.unescape(re.sub('<[^>]+>',' ',cells[0])); text=re.sub(r'\s+',' ',text).strip()
 links=re.findall(r'href="([^"]+)"',cells[0]); url=links[0] if links else None
 if url and url.startswith('/'): url='https://www.fda.gov'+url
 ledger.append({'id':f'CBER-{idx}','product':text,'classification':'cber_review_pending','reason':'Approval date/indication requires product-page cross-check; current roster alone is not a historical census.','classification_status':'pending','priority':'screen_only','source':'FDA-CBER-roster','source_url':url,'source_locator':f'product table row {idx}','us_approval_date':None,'forecast_status':'not used for inclusion; assess separately'})
# Product pages verify selected original dates. Current indications are not silently
# treated as original labels; detailed initial-label review remains a case-level gate.
cber_verified={
'LUXTURNA':('2017-12-19','first_approved_dmt_candidate','Biallelic RPE65 retinal dystrophy; viable retinal tissue and subretinal procedure limit eligibility.'),
'KEBILIDI':('2024-11-13','first_approved_dmt_candidate','AADC deficiency; CNS gene delivery, first US approved targeted replacement candidate; prior neurotransmitter-directed care requires sensitivity.'),
'LENMELDY':('2024-03-18','boundary_prior_disease_modifying_care','MLD; prior HSCT in selected patients. Narrow presymptomatic/early-symptomatic window; conditioning and autologous manufacture.'),
'RETHYMIC':('2021-10-08','boundary_prior_disease_modifying_care','Congenital athymia; prior investigational thymus transplantation, individualized tissue delivery.'),
'VYJUVEK':('2023-05-19','first_approved_dmt_candidate','COL7A1 dystrophic epidermolysis bullosa wound gene therapy; repeat topical administration. Original age scope needs initial label.'),
'ENCELTO':('2025-03-05','first_approved_dmt_candidate','Adult MacTel2; ocular implant, first approved candidate. Commercial follow-up immature.'),
'WASKYRA':('2025-12-09','boundary_prior_disease_modifying_care','Wiskott-Aldrich syndrome; prior allogeneic HSCT. Current label excludes available matched related donor.'),
'PAPZIMEOS':('2025-08-14','adjacent_symptomatic_or_dmt_uncertain','Adult recurrent respiratory papillomatosis; prior surgery/off-label bevacizumab, viral rather than genetic disease.'),
'SKYSONA':('2022-09-16','boundary_prior_disease_modifying_care','Cerebral ALD; prior HSCT. Later safety restrictions must not be substituted for original label.'),
'ZYNTEGLO':('2022-08-17','boundary_prior_disease_modifying_care','Transfusion-dependent beta thalassemia; prior HSCT and luspatercept. One-time exposure and conditioning.'),
'FAYUVI':('2026-09-17','outside_primary_period_2026','MPS IIIA neurologic manifestations with preserved neurodevelopmental function; informative future CNS window comparator, no mature sales.'),
'GENGLYCOS':('2026-08-19','outside_primary_period_2026','GSDIa adjunct to nutritional management; prior diet/cornstarch. Not a 2000–2025 entrant.'),
'KRESLADI':('2026-03-26','outside_primary_period_2026','Severe LAD-I without matched sibling HSCT donor; prior transplant boundary.'),
'OTARMENI':('2026-04-23','outside_primary_period_2026','OTOF hearing loss with preserved outer hair cell function; cochlear implant and tissue-window comparator.'),
}
onc={'ABECMA','ADSTILADRIN','AMTAGVI','AUCATZYL','BREYANZI','CARVYKTI','IMLYGIC','KYMRIAH','PROVENGE','TECARTUS','TECELRA','TUDRIQEV','VOCERYQ','YESCARTA'}
followers={'BEQVEZ','CASGEVY','ELEVIDYS','HEMGENIX','ITVISMA','LANTIDRA','LYFGENIA','ROCTAVIAN','RYONCIL','ZEVASKYN','ZOLGENSMA'}
for r in ledger:
 if not r['id'].startswith('CBER'): continue
 key=r['product'].split()[0].replace('™','')
 if key in cber_verified:
  r['us_approval_date'],r['classification'],r['reason']=cber_verified[key]
  r['classification_status']='original date checked on FDA product page; clinical first-status judgment provisional unless case adjudicated'
 elif key in onc:
  r['classification']='excluded_oncology_tumor_or_support'; r['reason']='Oncology/tumor cell or gene therapy outside primary cohort; approval date not independently extracted.'
 elif key in followers:
  r['classification']='follower_or_established_alternative'; r['reason']='Earlier disease-modifying medicines, replacement therapy or transplantation; not a clean first-DMT launch. Original date not independently extracted.'
 else:
  r['classification']='excluded_supportive_diagnostic_or_acute'; r['reason']='Cord-blood/HSCT adjunct, tissue repair, cosmetic or supportive intervention; outside focused chronic rare-genetic DMT cohort. Original date not independently extracted.'
 if r['classification_status']=='pending': r['classification_status']='provisional product-level scope screen; original date/label not independently adjudicated'
 r['priority']='deep_dive' if key in {'LUXTURNA','KEBILIDI','LENMELDY'} else 'screen_only'
(OUT/'approval_screen.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
candidate_groups={'first_approved_dmt_candidate','boundary_prior_disease_modifying_care','adjacent_symptomatic_or_dmt_uncertain','historical_extension','outside_primary_period_2026'}
(OUT/'candidate_universe.json').write_text(json.dumps([r for r in ledger if r['classification'] in candidate_groups],ensure_ascii=False,indent=2)+'\n')
print('Complete CDER row disposition',dict(Counter(x['classification'] for x in ledger if x['id'].startswith('CDER'))))
print('Unresolved',[(x['id'],x['product']) for x in ledger if x['classification']=='unresolved_screen'])
print('CBER entries',sum(x['id'].startswith('CBER') for x in ledger))
