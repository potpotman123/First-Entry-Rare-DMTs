"""Reproduce the desk-study arithmetic. No external packages or network required.
Run: python3 reproduce_calculations.py
Inputs and results are resolved relative to this script, not the working directory.
These calculations do NOT estimate systematic historical forecasting bias.
"""
from pathlib import Path
import json

folder = Path(__file__).resolve().parent
data = json.loads((folder / 'research_evidence.json').read_text())

def actual(pair, year, geography):
    rows = [r for r in data['actual_sales']
            if r['pair'] == pair and r['year'] == year and r['geography'] == geography]
    assert len(rows) == 1, (pair, year, geography)
    return rows[0]['sales_usdm']

def forecast(record_id):
    return next(r for r in data['historical_forecasts'] if r['id'] == record_id)

def point(record_id, year, geography):
    f = forecast(record_id)
    a = actual(f['pair'], year, geography)
    assert f['original_sales_usdm'] > 0
    return {'actual_usdm': a, 'forecast_as_reported_usdm': f['original_sales_usdm'],
            'error_fraction': a / f['original_sales_usdm'] - 1,
            'error_operator': '<' if f['operator'] == '>' else '=',
            'normalization': 'NONE: historical PoS unresolved; not a strict result',
            'forecast_id': record_id, 'actual_geography_used': geography,
            'interpretation': 'Contextual arithmetic only; see scope and exclusion flags in source dataset.'}

cap = data['capitalization_bridge']
economic_shares = cap['common_shares'] + cap['prefunded_initial'] + cap['prefunded_second']
equity_usdm = economic_shares * cap['reference_stock_price_usd'] / 1e6
n = data['needham_inputs']
launch_revenue_per_patient = n['launch_annual_wac_usd'] * (1 - n['gross_to_net_discount']) * n['adherence_persistence']
peak_wac = n['launch_annual_wac_usd'] * (1 + n['annual_wac_growth']) ** (2046-2032)
peak_us = 12154 * .5 * .5 * peak_wac * .85 * .75 / 1e6
needham3 = sum(r['worldwide_usdm'] for r in data['needham_conditional_sales'] if r['year'] in (2032,2033,2034))
va3 = sum(r['as_reported_usdm'] for r in data['visible_alpha_reproduced_chart'] if r['year'] in (2032,2033,2034))

results = {
    'as_of': data['as_of'],
    'strict_primary_drug_indication_n': len({r['pair'] for r in data['historical_forecasts'] if r['strict_eligible']}),
    'strict_36_month_bias': None,
    'strict_60_month_bias': None,
    'reason_for_null': 'No fully matched risk-normalized annual curves; no pooling of contextual point comparisons.',
    'contextual_point_comparisons': {
        'spinraza_2022': point('F1', 2022, 'worldwide'),
        'strensiq_if_forecast_worldwide': point('F2', 2018, 'worldwide'),
        'strensiq_if_forecast_US': point('F2', 2018, 'US'),
        'onpattro_2022': point('F5_2022', 2022, 'worldwide')
    },
    'calendar_year_sums_not_first_36_months': {
        'brineura_2017_2019_usdm': sum(actual('Brineura / CLN2', y, 'worldwide') for y in (2017,2018,2019)),
        'daybue_2023_2025_usdm': sum(r['sales_usdm'] for r in data['actual_sales'] if r['pair']=='Daybue / Rett')
    },
    'capitalization_check': {
        'economic_shares_before_options_and_future_financing': economic_shares,
        'reference_price_usd': cap['reference_stock_price_usd'],
        'equity_value_usdm': equity_usdm,
        'equity_less_cash_proxy_usdm': equity_usdm-cap['cash_usdm'],
        'not_a_live_quote_or_complete_EV': True
    },
    'needham_checks': {
        'launch_revenue_per_modeled_patient_usd': launch_revenue_per_patient,
        'peak_2046_wac_derived_usd': peak_wac,
        'peak_US_derived_from_rounded_population_usdm': peak_us,
        'peak_WW_derived_usdm': peak_us*1.25,
        'multiple_method_EV_from_printed_inputs_usdm': 1843*.25*7/(1.09**17),
        'blended_equity_from_printed_legs_usdm': (649+880)/2,
        'blended_equity_per_share_from_printed_legs_usd': ((649+880)/2)/98,
        'cash_per_share_from_printed_inputs_usd': 135/98,
        'drug_per_share_from_printed_inputs_usd': 630/98,
        'conditional_WW_2032_2034_calendar_sum_usdm': needham3,
        'reproduced_VA_2032_2034_calendar_sum_usdm': va3,
        'VA_comparison_note': 'As-printed chart sums only; consensus risk treatment and composition unknown; not a validated conditional comparison.',
        'printed_peak_multiple_input_usdm': 1843,
        'printed_multiple_year': 2043,
        'printed_curve_2043_usdm': 1899,
        'printed_curve_peak_2046_usdm': 2106,
        'unresolved_discrepancies_preserved': True
    }
}

assert results['strict_primary_drug_indication_n'] == 0
assert all(r['conditional_sales_usdm'] is None for r in data['historical_forecasts'])
assert len(data['current_sellside']) == 7
assert len(data['needham_conditional_sales']) == 22
assert len({r['id'] for r in data['historical_forecasts']}) == len(data['historical_forecasts'])
assert abs(results['calendar_year_sums_not_first_36_months']['daybue_2023_2025_usdm'] - 917) < 1e-9
assert abs(results['calendar_year_sums_not_first_36_months']['brineura_2017_2019_usdm'] - 120.5) < 1e-9
assert abs(launch_revenue_per_patient - 366562.5) < 1e-9
for r in data['historical_forecasts'] + data['actual_sales'] + data['screened_candidates']:
    assert r['source'] in data['sources']

(folder / 'calculation_results.json').write_text(json.dumps(results, indent=2))
print('Source references and arithmetic checked. Strict primary N=0; no aggregate bias estimated.')
