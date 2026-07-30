import pandas as pd
from pathlib import Path

PROCESSED = Path("C:/Users/vanki/OneDrive/Desktop/bluestock_mf_capstone/data/processed")
performance = pd.read_csv(PROCESSED / "clean_performance.csv")

def recommend_funds(risk_appetite):
    risk_map = {
        "Low": ["Low"],
        "Moderate": ["Moderate", "Moderately High"],
        "High": ["High", "Very High"]
    }
    grades = risk_map.get(risk_appetite, ["Moderate"])
    filtered = performance[performance["risk_grade"].isin(grades)]
    top3 = filtered.nlargest(3, "sharpe_ratio")[
        ["scheme_name", "risk_grade", "sharpe_ratio", "return_1yr_pct"]
    ]
    return top3

if __name__ == "__main__":
    for risk in ["Low", "Moderate", "High"]:
        print(f"Top 3 Funds for {risk} Risk:")
        print(recommend_funds(risk))
        print()
