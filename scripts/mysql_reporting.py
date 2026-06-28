"""
===============================================================================
Project    : Chicago Crime Data Analytics
Use Case   : 4 - MySQL Reporting & Integration
File       : mysql_reporting.py

Description:
This script reads MySQL reporting views into Pandas DataFrames,
validates the data, displays reporting information,
and exports the reports to CSV.

Views Read:
1. vw_crime_yearly
2. vw_crime_by_category

Author : Yedukondalu Cheeraboina(y.cheeraboina@accenture.com)
===============================================================================
"""

# ============================================================================
# Import Required Libraries
# ============================================================================

import os

import pandas as pd

from sqlalchemy import create_engine

from utils.database_config import get_database_url


# ============================================================================
# Create Reports Folder
# ============================================================================

os.makedirs("../reports", exist_ok=True)


# ============================================================================
# Create SQLAlchemy Engine
# ============================================================================

print("=" * 70)
print("MYSQL REPORTING")
print("=" * 70)

DATABASE_URL = get_database_url()

engine = create_engine(

    DATABASE_URL,

    pool_pre_ping=True,

    pool_recycle=3600,

    future=True

)

print("\nDatabase Connected Successfully.")


# ============================================================================
# Read Yearly View
# ============================================================================

yearly_df = pd.read_sql(

    "SELECT * FROM vw_crime_yearly",

    engine

)

print("\nYearly Crime Report")

print("-" * 70)

print(yearly_df)


# ============================================================================
# Read Category View
# ============================================================================

category_df = pd.read_sql(

    "SELECT * FROM vw_crime_by_category",

    engine

)

print("\nCrime Category Report")

print("-" * 70)

print(category_df)


# ============================================================================
# Report Summary
# ============================================================================

print("\nREPORT SUMMARY")

print("=" * 70)

print(f"Yearly Records      : {len(yearly_df)}")

print(f"Category Records    : {len(category_df)}")

print(f"Total Crimes        : {yearly_df['Crime_Count'].sum()}")

print(f"Total Arrests       : {yearly_df['Arrest_Count'].sum()}")

print(f"Crime Categories    : {category_df['Primary_Type'].nunique()}")


# ============================================================================
# Export Reports
# ============================================================================

yearly_df.to_csv(

    "../reports/yearly_crime_report.csv",

    index=False

)

category_df.to_csv(

    "../reports/crime_category_report.csv",

    index=False

)

print("\nReports Exported Successfully.")


print("\nProcess Completed Successfully.")

print("=" * 70)