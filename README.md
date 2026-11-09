# First Entry Rare DMTs

Independent research on whether preapproval sell-side forecasts systematically underestimate approval-conditional sales for first rare-disease disease-modifying therapies, and what the evidence means for CMP-002 in SYNGAP1-related disorder.

**Current assessment, 9 November 2026:** systematic underforecasting is not established. The supplied prior analysis strengthens a case-by-case investigation of omitted eligible populations, patient finding, treatment exposure, geography and competition. Several headline comparisons mix realized outcomes with forecast revisions or postapproval estimates.

This historical study is separate from the independent CMP-002 sales forecast and CAMP valuation project. No generic rare-disease uplift or new price target has been calculated.

## Start here

- [Updated assessment](reports/current_assessment.html) — what the prior analysis changes, what needs correction, and implications for CMP-002.
- [Prior-analysis audit](data/prior_deck_audit.json) — nine product summaries, 27 dated estimate leads, 16 issues and two exploratory target-year comparisons.
- [Integrated evidence](data/research_evidence.json) — source records, the current Street baseline, historical data and 53 candidate/control entries. This is a screened set, not an exhaustive approval census.
- [Original research brief](reports/archive/initial_research_brief.html) — preserved first-pass case studies, literature review and seven-firm CAMP comparison.
- [Source manifest](sources/source_manifest.json) — all nine original PDFs and two task briefs, with hashes and provenance.
- [Research protocol](protocol/study_protocol_v1.txt) and [explicit amendment](protocol/amendment_2026-11-09.txt).
- [Continuation handoff](context/handoff.txt).

Download HTML reports to read them in a browser; GitHub may display their source rather than render them. The repository remains private.

## Evidence boundaries

Strict matched three- and five-year cumulative samples remain N=0: no complete original annual curve is yet matched on risk, geography, label and horizon. This is an access/matching limitation, not a finding that forecasts are unbiased.

The new deck declares its historical estimates unadjusted for probability. That declaration is recorded, while conflicting appendix entries remain unresolved. Peak forecasts are not transformed into synthetic annual curves. Later indications are excluded from the primary analysis. Fast followers are kept separate from first DMTs.

## Reproduce

Python 3 standard library is sufficient:

```sh
python3 scripts/integrate_prior_analysis.py
python3 scripts/reproduce_calculations.py
python3 scripts/check_project.py
```

Original first-pass data and code are retained in archive folders. The archived authoring scripts preserve the original workstation paths; the current integration, calculation and validation scripts resolve paths relative to this checkout.

Source PDFs are user-provided research materials, retained unchanged for this private project. Their inclusion does not grant redistribution rights or authorize making this repository public. Temporary page renders, caches, credentials and unrelated workspace files are excluded.
