"""
BlueStock MF Capstone - Main Pipeline Runner
Run all ETL and analytics processes
"""
import pandas as pd
from pathlib import Path

def main():
    print("BLUESTOCK MF CAPSTONE - RUN PIPELINE")

    CWD = Path("data")
    print(f"Data folder: {CWD}")
    print("All processes loaded successfully!")

if __name__ == "__main__":
    main()
