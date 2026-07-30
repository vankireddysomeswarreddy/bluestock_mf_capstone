import pandas as pd
from pathlib import Path

# Paths
BASE = Path("C:/Users/vanki/OneDrive/Desktop/bluestock_mf_capstone")
RAW = BASE / "data/raw/Bluestock_MF_Datasets"
PROCESSED = BASE / "data/processed"

# Load all 10 datasets
files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    df = pd.read_csv(RAW / file)
    print(f"✅ {file}: {df.shape}")
    print(f"   Columns: {df.columns.tolist()}")
    print(f"   Head: {df.head(2)}\n")

print("🎉 All 10 datasets loaded!")