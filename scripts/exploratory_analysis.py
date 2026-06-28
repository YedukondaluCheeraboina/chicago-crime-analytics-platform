"""
===============================================================================
Project    : Chicago Crime Data Analytics
Use Case   : 2 - Exploratory Data Analysis & Visualization
File       : exploratory_analysis.py

Description:
This script performs Exploratory Data Analysis (EDA) on the
feature-engineered Chicago Crime Dataset.

Tasks Performed:
1. Crime Trend Over Years
2. Crime Distribution by Category
3. Arrest Rate Analysis
4. Crime Heatmap
5. Community Area Analysis

Input :
    ../feature_engineered_data/crime_feature_engineered.csv

Output :
    Graphs saved in ../graphs/

Author : Yedukondalu Cheeraboina(y.cheeraboina@accenture.com)
===============================================================================
"""

# ============================================================================
# Import Required Libraries
# ============================================================================

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

import os


# ============================================================================
# Load Dataset
# ============================================================================

print("=" * 70)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 70)

df = pd.read_csv(
    "../feature_engineered_data/crime_feature_engineered.csv",
    parse_dates=["date", "date_of_update"]
)

print("\nDataset Loaded Successfully.")

print(f"Rows : {len(df)}")
print(f"Columns : {len(df.columns)}")


# ============================================================================
# Create Output Directories
# ============================================================================

os.makedirs("../graphs/crime_trend", exist_ok=True)
os.makedirs("../graphs/crime_categories", exist_ok=True)
os.makedirs("../graphs/arrest_analysis", exist_ok=True)
os.makedirs("../graphs/heatmaps", exist_ok=True)
os.makedirs("../graphs/community_analysis", exist_ok=True)


# ============================================================================
# Configure Visualization Settings
# ============================================================================

plt.style.use("ggplot")

sns.set_theme(style="whitegrid")

plt.rcParams["figure.figsize"] = (10, 6)

plt.rcParams["font.size"] = 11


# ============================================================================
# Crime Trend Over Years
# ============================================================================

print("\nAnalyzing Crime Trend Over Years...")
print("-" * 70)

# Group crimes by Year
crime_by_year = (
    df.groupby("Year")
      .size()
      .reset_index(name="Crime_Count")
)

print("\nCrime Count by Year")

print(crime_by_year)


# Plot Crime Trend

plt.figure(figsize=(10,6))

plt.plot(
    crime_by_year["Year"],
    crime_by_year["Crime_Count"],
    marker="o",
    linewidth=2
)

plt.title("Crime Trend Over Years")

plt.xlabel("Year")

plt.ylabel("Number of Crimes")

plt.xticks(crime_by_year["Year"])

plt.grid(True)

plt.tight_layout()

plt.savefig("../graphs/crime_trend/crime_trend_over_years.png")

plt.show()

print("\nCrime Trend graph saved successfully.")


# ============================================================================
# Crime Distribution by Category
# ============================================================================

print("\nAnalyzing Crime Distribution by Category...")
print("-" * 70)

crime_category = (
    df.groupby("primary_type")
      .size()
      .reset_index(name="Crime_Count")
      .sort_values(by="Crime_Count", ascending=False)
)

print("\nCrime Count by Category")

print(crime_category)


# ============================================================================
# Calculate Crime Percentage
# ============================================================================

total_crimes = len(df)

crime_category["Percentage"] = (
    crime_category["Crime_Count"] / total_crimes
) * 100

crime_category["Percentage"] = crime_category["Percentage"].round(2)

print("\nCrime Category Percentage")

print(crime_category)


# ============================================================================
# Top 10 Crime Categories
# ============================================================================

top10_crimes = crime_category.head(10)

print("\nTop 10 Crime Categories")

print(top10_crimes)


# ============================================================================
# Plot Top 10 Crime Categories
# ============================================================================

plt.figure(figsize=(12,6))

plt.bar(
    top10_crimes["primary_type"],
    top10_crimes["Crime_Count"]
)

plt.title("Top 10 Crime Categories")

plt.xlabel("Crime Category")

plt.ylabel("Number of Crimes")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig(
    "../graphs/crime_categories/top10_crime_categories.png"
)

plt.show()


# ============================================================================
# Business Observation
# ============================================================================

print("\nBusiness Observation")
print("-" * 70)

most_common = top10_crimes.iloc[0]

print(
    f"Most Frequent Crime : {most_common['primary_type']}"
)

print(
    f"Crime Count : {most_common['Crime_Count']}"
)

print(
    f"Percentage : {most_common['Percentage']}%"
)


# ============================================================================
# Arrest Rate Analysis
# ============================================================================

print("\nAnalyzing Arrest Rate...")
print("-" * 70)

total_crimes = len(df)

total_arrests = df["arrest"].sum()

arrest_rate = (total_arrests / total_crimes) * 100

print(f"\nTotal Crimes   : {total_crimes}")
print(f"Total Arrests  : {total_arrests}")
print(f"Arrest Rate    : {arrest_rate:.2f}%")


# ============================================================================
# Arrest Status Distribution
# ============================================================================

arrest_distribution = (
    df["arrest"]
      .value_counts()
      .rename_axis("Arrest")
      .reset_index(name="Crime_Count")
)

print("\nArrest Distribution")

print(arrest_distribution)


# ============================================================================
# Arrest Rate by Year
# ============================================================================

arrest_year = (
    df.groupby("Year")["arrest"]
      .mean()
      .reset_index()
)

arrest_year["Arrest Rate (%)"] = (
    arrest_year["arrest"] * 100
).round(2)

print("\nYear-wise Arrest Rate")

print(arrest_year[["Year", "Arrest Rate (%)"]])


# ============================================================================
# Plot Arrest Rate by Year
# ============================================================================

plt.figure(figsize=(10,6))

sns.lineplot(
    data=arrest_year,
    x="Year",
    y="Arrest Rate (%)",
    marker="o",
    linewidth=2
)

plt.title("Arrest Rate Across Years")

plt.xlabel("Year")

plt.ylabel("Arrest Rate (%)")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "../graphs/arrest_analysis/arrest_rate_by_year.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nArrest Rate graph saved successfully.")


# ============================================================================
# Business Observation
# ============================================================================

print("\nBusiness Observation")
print("-" * 70)

highest = arrest_year.loc[
    arrest_year["Arrest Rate (%)"].idxmax()
]

lowest = arrest_year.loc[
    arrest_year["Arrest Rate (%)"].idxmin()
]

print(f"Overall Arrest Rate : {arrest_rate:.2f}%")

print(
    f"Highest Arrest Rate : {int(highest['Year'])} ({highest['Arrest Rate (%)']}%)"
)

print(
    f"Lowest Arrest Rate  : {int(lowest['Year'])} ({lowest['Arrest Rate (%)']}%)"
)


# ============================================================================
# Heatmap - Crime Frequency by Month and Day of Week
# ============================================================================

print("\nAnalyzing Crime Frequency by Month and Day of Week...")
print("-" * 70)

crime_heatmap = pd.pivot_table(
    df,
    values="id",
    index="MonthName",
    columns="DayOfWeek",
    aggfunc="count",
    fill_value=0
)


month_order = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

crime_heatmap = crime_heatmap.reindex(month_order)


print("\nCrime Frequency Table")

print(crime_heatmap)


# ============================================================================
# Plot Heatmap
# ============================================================================

plt.figure(figsize=(12,7))

sns.heatmap(
    crime_heatmap,
    annot=True,
    fmt="d",
    cmap="YlOrRd",
    linewidths=0.5
)

plt.title("Crime Frequency by Month and Day of Week")

plt.xlabel("Day of Week")

plt.ylabel("Month")

plt.tight_layout()

plt.savefig(
    "../graphs/heatmaps/crime_month_day_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nCrime Heatmap saved successfully.")


# ============================================================================
# Business Observation
# ============================================================================

print("\nBusiness Observation")
print("-" * 70)

highest_value = crime_heatmap.max().max()

highest_position = crime_heatmap.stack().idxmax()

print(f"Highest Crime Frequency : {highest_value}")

print(f"Month : {highest_position[0]}")

print(f"Day : {highest_position[1]}")


# ============================================================================
# Top Community Areas by Crime Count
# ============================================================================

print("\nAnalyzing Top Community Areas...")
print("-" * 70)

community_crimes = (
    df.groupby("community_code")
      .size()
      .reset_index(name="Crime_Count")
      .sort_values(by="Crime_Count", ascending=False)
)

print("\nCrime Count by Community Area")

print(community_crimes)


# ============================================================================
# Top 10 Community Areas
# ============================================================================

top10_community = community_crimes.head(10)

print("\nTop 10 Community Areas")

print(top10_community)


# ============================================================================
# Plot Top Community Areas
# ============================================================================

plt.figure(figsize=(12,6))

sns.barplot(
    data=top10_community,
    x="community_code",
    y="Crime_Count"
)

plt.title("Top 10 Community Areas by Crime Count")

plt.xlabel("Community Area")

plt.ylabel("Number of Crimes")

plt.tight_layout()

plt.savefig(
    "../graphs/community_analysis/top10_community_areas.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nTop Community Areas graph saved successfully.")


# ============================================================================
# Business Observation
# ============================================================================

print("\nBusiness Observation")
print("-" * 70)

highest_area = top10_community.iloc[0]

print(f"Highest Crime Community Area : {int(highest_area['community_code'])}")

print(f"Crime Count : {int(highest_area['Crime_Count'])}")


print(f"\nTotal Community Areas : {df['community_code'].nunique()}")

print(f"Average Crimes per Community : {community_crimes['Crime_Count'].mean():.2f}")

print(f"Maximum Crimes : {community_crimes['Crime_Count'].max()}")

print(f"Minimum Crimes : {community_crimes['Crime_Count'].min()}")


