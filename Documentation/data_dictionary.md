# Data Dictionary

## dim_fund
amfi_code, scheme_name, fund_house, category

## fact_nav
amfi_code, date, nav

## fact_transactions
investor_id, amfi_code, transaction_type, amount_inr

## fact_performance
amfi_code, return_1yr_pct, sharpe_ratio, alpha, beta