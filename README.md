# First Entry Rare DMTs

Independent research on whether preapproval sell-side forecasts systematically underestimate approval-conditional sales for first rare-disease disease-modifying therapies, and what the evidence means for CMP-002 in SYNGAP1-related disorder.

**Current assessment, independent rebuild, 9 November 2026:** an original January 2004 SG Cowen publication supplies three preapproval target-year forecasts below later ERT sales. Newly recovered Vimizim and Kanuma comparisons provide near-in-line and downside countercases. Unknown probability treatment and incomplete scope prevent a normalized pooled bias estimate. The evidence supports specific commercial mechanisms, not a universal first-DMT uplift.

The rebuild starts from 1,387 FDA CDER original approvals plus 55 current CBER cell/gene roster entries. Every retrieved row has an explicit provisional disposition. There are 82 primary-period candidates/boundaries/adjacent therapies, 13 earlier precedents and four verified 2026 entrants. These are not 82 confirmed first DMTs or a complete historical orphan-drug census. Twenty analogue dossiers keep missing-data and immature cases visible.

This historical study is separate from the independent CMP-002 sales forecast and CAMP valuation project. No generic rare-disease uplift or new price target has been calculated.

## Start here

- [Independent research report](reports/independent_research.html) — new regulatory universe, five new target-year checks, 20 case dossiers, CMP-002 implications and exact missing-model requests.
- [Independent evidence](data/independent/evidence.json), [full 1,442-row screen](data/independent/approval_screen.json), [99-entry extended candidate universe](data/independent/candidate_universe.json), and [validation](data/independent/validation.json).
- [Independent rebuild protocol](protocol/independent_rebuild_2026-11-09.txt), [case-priority freeze](protocol/independent_case_priority_2026-11-09.txt), and [coverage/deviations](protocol/independent_deviations_and_coverage.txt).
- [Updated assessment](reports/current_assessment.html) — what the prior analysis changes, what needs correction, and implications for CMP-002.
- [Prior-analysis audit](data/prior_deck_audit.json) — nine product summaries, 27 dated estimate leads, 16 issues and two exploratory target-year comparisons.
- [Integrated evidence](data/research_evidence.json) — source records, the current Street baseline, historical data and 53 candidate/control entries. This is a screened set, not an exhaustive approval census.
- [Original research brief](reports/archive/initial_research_brief.html) — preserved first-pass case studies, literature review and seven-firm CAMP comparison.
- [Source manifest](sources/source_manifest.json) — all nine original PDFs and two task briefs, with hashes and provenance.
- [Research protocol](protocol/study_protocol_v1.txt) and [explicit amendment](protocol/amendment_2026-11-09.txt).
- [Continuation handoff](context/handoff.txt).

Download HTML reports to read them in a browser; GitHub may display their source rather than render them. The repository remains public, as explicitly authorized by the user on 9 November 2026, including the supplied sell-side material and context.

## Evidence boundaries

Strict matched three- and five-year cumulative samples remain N=0: no complete original annual curve is yet matched on risk, geography, label and horizon. This is an access/matching limitation, not a finding that forecasts are unbiased.

The new deck declares its historical estimates unadjusted for probability. That declaration is recorded, while conflicting appendix entries remain unresolved. Peak forecasts are not transformed into synthetic annual curves. Later indications are excluded from the primary analysis. Fast followers are kept separate from first DMTs.

## Reproduce

Python 3 standard library is sufficient:

```sh
python3 scripts/build_independent_universe.py
python3 scripts/build_independent_evidence.py
python3 scripts/render_independent_report.py
python3 scripts/check_independent_research.py
```

The saved FDA extraction is already included. Re-extracting the original XLSX uses `openpyxl` read-only; network retrieval is optional and the failed OOPD export is explicitly marked unusable. Universe construction does not read prior deck or forecast outcomes. Evidence construction reuses selected prior verified sources only after case selection.

To reproduce the earlier supplied-analysis integration:

```sh
python3 scripts/integrate_prior_analysis.py
python3 scripts/reproduce_calculations.py
python3 scripts/check_project.py
```

Original first-pass data and code are retained in archive folders. The archived authoring scripts preserve the original workstation paths; the current integration, calculation and validation scripts resolve paths relative to this checkout.

Source PDFs are user-provided research materials, retained unchanged. The user explicitly authorized keeping this repository public and saving everything, including sell-side context, on 9 November 2026. Earlier archived documents may refer to the superseded private-only instruction. Temporary page renders, caches, credentials and unrelated workspace files are excluded.
