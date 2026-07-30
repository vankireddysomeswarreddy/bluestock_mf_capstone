import requests
import pandas as pd
import os
from pathlib import Path
from datetime import datetime

# ========== CONFIG ==========
BASE_URL = "https://api.mfapi.in/mf"
OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ========== FETCH NAV ==========
def fetch_nav(scheme_code, scheme_name):
    try:
        url = f"{BASE_URL}/{scheme_code}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if 'data' in data:
            df = pd.DataFrame(data['data'])
            df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
            df['nav'] = pd.to_numeric(df['nav'], errors='coerce')
            df['scheme_code'] = scheme_code
            df['scheme_name'] = scheme_name
            return df
    except Exception as e:
        print(f"Error: {scheme_name} -> {e}")
    return None

# ========== MAIN ==========
def main():
    schemes = {
        125497: "HDFC Top 100 Direct Plan",
        119551: "SBI Bluechip Direct Plan",
        120503: "ICICI Bluechip Direct Plan",
        118632: "Nippon Large Cap Direct Plan",
        119092: "Axis Bluechip Direct Plan",
        120841: "Kotak Bluechip Direct Plan"
    }

    all_navs = []
    print("Fetching Live NAV from mfapi.in...")
    
    for code, name in schemes.items():
        print(f"  -> {name}")
        df = fetch_nav(code, name)
        if df is not None:
            all_navs.append(df)

    if all_navs:
        combined = pd.concat(all_navs, ignore_index=True)
        combined = combined.sort_values('date')
        
        filename = OUTPUT_DIR / "live_nav.csv"
        combined.to_csv(filename, index=False)
        print(f"\n✅ Saved {len(combined)} records to {filename}")
    else:
        print("❌ No data fetched!")

if __name__ == "__main__":
    main()