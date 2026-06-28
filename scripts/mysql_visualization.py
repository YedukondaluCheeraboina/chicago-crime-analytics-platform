"""
===============================================================================
Project    : Chicago Crime Data Analytics
Use Case   : 4 - MySQL Reporting & Integration
File       : mysql_visualization.py

Description:
This script reads reporting views from MySQL and generates
visualizations using Matplotlib and Seaborn.

Views Used
----------
1. vw_crime_yearly
2. vw_crime_by_category

Graphs Generated
----------------
1. Yearly Crime Trend
2. Yearly Arrest Trend
3. Crime Category Distribution
4. Crime Percentage Distribution

Author : Yedukondalu Cheeraboina(y.cheeraboina@accenture.com)
===============================================================================
"""


# ============================================================================
# Import Required Libraries
# ============================================================================

import os

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sqlalchemy import create_engine

from utils.database_config import get_database_url


# ============================================================================
# Create Output Folder
# ============================================================================

os.makedirs("../graphs/mysql_visualization", exist_ok=True)


# ============================================================================
# Connect to MySQL
# ============================================================================

print("=" * 70)
print("MYSQL VISUALIZATION")
print("=" * 70)

from utils.database_config import get_database_url

DATABASE_URL = get_database_url()

engine = create_engine(

    DATABASE_URL,

    pool_pre_ping=True,

    pool_recycle=3600,

    future=True

)

print("\nDatabase Connected Successfully.")


# ============================================================================
# Read MySQL Views
# ============================================================================

yearly_df = pd.read_sql(
    "SELECT * FROM vw_crime_yearly",
    engine
)

category_df = pd.read_sql(
    "SELECT * FROM vw_crime_by_category",
    engine
)

print("\nViews Loaded Successfully.")

print(f"Yearly Records : {len(yearly_df)}")
print(f"Category Records : {len(category_df)}")


# ============================================================================
# Configure Visualization
# ============================================================================

plt.style.use("ggplot")

sns.set_theme(style="whitegrid")

plt.rcParams["figure.figsize"] = (10, 6)

plt.rcParams["font.size"] = 11


# ============================================================================
# Visualization 1 - Yearly Crime Trend
# ============================================================================

print("\nGenerating Yearly Crime Trend...")
print("-" * 70)

plt.figure(figsize=(10, 6))

sns.lineplot(
    data=yearly_df,
    x="Year",
    y="Crime_Count",
    marker="o",
    linewidth=2.5
)

plt.title("Yearly Crime Trend")

plt.xlabel("Year")

plt.ylabel("Crime Count")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "../graphs/mysql_visualization/yearly_crime_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Yearly Crime Trend graph saved successfully.")


# ============================================================================
# Business Observation
# ============================================================================

highest = yearly_df.loc[
    yearly_df["Crime_Count"].idxmax()
]

lowest = yearly_df.loc[
    yearly_df["Crime_Count"].idxmin()
]

print("\nBusiness Observation")
print("-" * 70)

print(
    f"Highest Crime Year : {int(highest['Year'])}"
)

print(
    f"Crime Count        : {int(highest['Crime_Count'])}"
)

print()

print(
    f"Lowest Crime Year  : {int(lowest['Year'])}"
)

print(
    f"Crime Count        : {int(lowest['Crime_Count'])}"
)


# ============================================================================
# Visualization 2 - Yearly Arrest Trend
# ============================================================================

print("\nGenerating Yearly Arrest Trend...")
print("-" * 70)

plt.figure(figsize=(10, 6))

sns.barplot(
    data=yearly_df,
    x="Year",
    y="Arrest_Count"
)

plt.title("Yearly Arrest Count")

plt.xlabel("Year")

plt.ylabel("Number of Arrests")

plt.tight_layout()

plt.savefig(
    "../graphs/mysql_visualization/yearly_arrest_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Yearly Arrest Trend graph saved successfully.")


# ============================================================================
# Business Observation
# ============================================================================

highest_arrest = yearly_df.loc[
    yearly_df["Arrest_Count"].idxmax()
]

lowest_arrest = yearly_df.loc[
    yearly_df["Arrest_Count"].idxmin()
]

print("\nBusiness Observation")
print("-" * 70)

print(
    f"Highest Arrest Year : {int(highest_arrest['Year'])}"
)

print(
    f"Arrest Count        : {int(highest_arrest['Arrest_Count'])}"
)

print()

print(
    f"Lowest Arrest Year  : {int(lowest_arrest['Year'])}"
)

print(
    f"Arrest Count        : {int(lowest_arrest['Arrest_Count'])}"
)


# ============================================================================
# Visualization 3 - Crime Category Distribution
# ============================================================================

print("\nGenerating Crime Category Distribution...")
print("-" * 70)

# Sort categories by crime count (highest first)
category_sorted = category_df.sort_values(
    by="Crime_Count",
    ascending=False
)

plt.figure(figsize=(12, 8))

sns.barplot(
    data=category_sorted,
    x="Crime_Count",
    y="Primary_Type"
)

plt.title("Crime Category Distribution")

plt.xlabel("Crime Count")

plt.ylabel("Crime Category")

plt.tight_layout()

plt.savefig(
    "../graphs/mysql_visualization/crime_category_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Crime Category Distribution graph saved successfully.")


# ============================================================================
# Business Observation
# ============================================================================

highest_category = category_sorted.iloc[0]
lowest_category = category_sorted.iloc[-1]

print("\nBusiness Observation")
print("-" * 70)

print(f"Most Common Crime  : {highest_category['Primary_Type']}")
print(f"Crime Count        : {int(highest_category['Crime_Count'])}")
print(f"Percentage         : {highest_category['Crime_Percentage']:.2f}%")

print()

print(f"Least Common Crime : {lowest_category['Primary_Type']}")
print(f"Crime Count        : {int(lowest_category['Crime_Count'])}")
print(f"Percentage         : {lowest_category['Crime_Percentage']:.2f}%")


# ============================================================================
# Visualization 4 - Crime Percentage Distribution
# ============================================================================

print("\nGenerating Crime Percentage Distribution...")
print("-" * 70)

plt.figure(figsize=(10, 10))

plt.pie(
    category_sorted["Crime_Percentage"],
    labels=category_sorted["Primary_Type"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Crime Percentage Distribution")

plt.tight_layout()

plt.savefig(
    "../graphs/mysql_visualization/crime_percentage_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Crime Percentage Distribution graph saved successfully.")


# ============================================================================
# Project Summary
# ============================================================================

print("\n" + "=" * 70)
print("MYSQL VISUALIZATION SUMMARY")
print("=" * 70)

print(f"Yearly Records              : {len(yearly_df)}")
print(f"Crime Categories            : {len(category_df)}")
print(f"Total Crimes                : {yearly_df['Crime_Count'].sum()}")
print(f"Total Arrests               : {yearly_df['Arrest_Count'].sum()}")

print("\nGraphs Generated")
print("-" * 70)
print("1. yearly_crime_trend.png")
print("2. yearly_arrest_trend.png")
print("3. crime_category_distribution.png")
print("4. crime_percentage_distribution.png")

print("\nAll visualizations generated successfully.")
print("\nChicago Crime Data Analytics Project Completed Successfully!")

print("=" * 70)

