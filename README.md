BlueStock MF Capstone Project
Mutual Fund Analytics Platform
An end-to-end data engineering and analytics project for Indian Mutual Funds, built for BlueStock Fintech.
---
Project Overview
This capstone project analyzes 40 mutual fund schemes across 10+ fund houses using real NAV data from AMFI India. It includes:
ETL Pipeline (Python/Pandas)
SQLite Database
EDA Visualizations (15+ charts)
Performance Metrics (Sharpe, Alpha, Beta, VaR)
Interactive Dashboard (Power BI - 4 pages)
Advanced Analytics (VaR, Cohort, Recommender)
---
Project Structure
bluestock_mf_capstone/
├── data/
│   ├── raw/        # Original CSV files
│   ├── processed/  # Cleaned data
│   └── db/         # SQLite database
├── notebooks/      # Jupyter notebooks (Day 1-6)
├── scripts/        # Python scripts
├── sql/            # SQL schema and queries
├── dashboard/      # Power BI files
├── reports/        # Final reports and PPT
└── README.md
Key Metrics
Metric	Value
Total Schemes	40
Total AUM	₹81 Lakh Crore
SIP Inflows (Dec 2025)	₹31,002 Crore
Total Folios	26.12 Crore
Data Period	Jan 2022 - May 2026
NAV Records	46,000+
Investor Transactions	32,778
---
Tech Stack
Python — Pandas, NumPy, SciPy, Matplotlib, Seaborn, Plotly
Database — SQLite, SQLAlchemy
Dashboard — Power BI Desktop
Version Control — Git, GitHub
IDE — Jupyter Notebook, VS Code
---
Key Findings
Best Sharpe Ratio: Mirae Asset Large Cap (1.45)
Best Alpha: SBI Small Cap (+30.34%)
Top Fund House: SBI MF (₹12.5 Lakh Cr AUM)
High-Risk Funds: Small Cap funds (VaR > -2.5%)
At-Risk Investors: 1,332 SIP investors with gaps > 35 days
---
Fund Recommendations
Low Risk Investors:
ICICI Pru Liquid Fund (Sharpe: 7.68)
Kotak Liquid Fund (Sharpe: 6.18)
ABSL Liquid Fund (Sharpe: 5.14)
Moderate Risk:
Mirae Asset Large Cap (Sharpe: 1.06)
HDFC Top 100 (Sharpe: 1.06)
ICICI Pru Bluechip (Sharpe: 1.03)
High Risk:
Kotak Emerging Equity (Sharpe: 0.96)
ICICI Pru Midcap (Sharpe: 0.95)
SBI Small Cap (Sharpe: 0.94)
---
Deliverables
Day	Task	Status
Day 1	Project Setup + Data Ingestion	✅
Day 2	Data Cleaning + SQLite DB	✅
Day 3	EDA Analysis (15+ charts)	✅
Day 4	Performance Analytics	✅
Day 5	Power BI Dashboard (4 pages)	✅
Day 6	Advanced Analytics	✅
Day 7	Final Report + PPT	✅
---
How to Run
Clone the repository
Install dependencies: `pip install -r requirements.txt`
Run notebooks in order (01 to 06)
Open `dashboard/bluestock\\\_mf\\\_dashboard.pbix` in Power BI
---
Author
Name: Vankireddy Someswarreddy
Role: Data Analyst Intern
Company: BlueStock Fintech
Date: July 2026
GitHub: https://github.com/Vankireddysomeswarreddy/bluestock_mf_capstone
---
License
This project is for educational purposes only.
Data sourced from AMFI India (amfiindia.com) and mfapi.
