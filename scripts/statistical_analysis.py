"""
===============================================================================
Project    : Chicago Crime Data Analytics
Use Case   : 3 - Statistical Insights & Pattern Detection
File       : statistical_analysis.py

Description:
This script performs statistical analysis on the feature-engineered
Chicago Crime Dataset to identify crime patterns, peak crime hours,
community area outliers, and correlations between numerical features.

Tasks Performed:
1. Crime Intensity by Time
2. Community Area Outlier Detection
3. Correlation Analysis

Input :
    ../feature_engineered_data/crime_feature_engineered.csv

Output :
    Statistical graphs saved in ../graphs/statistical_analysis/

Author : Yedukondalu Cheeraboina(y.cheeraboina@accenture.com)
===============================================================================
"""

# ============================================================================
# Import Required Libraries
# ============================================================================

import os

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns


# ============================================================================
# Create Output Directory
# ============================================================================

os.makedirs(
    "../graphs/statistical_analysis",
    exist_ok=True
)


# ============================================================================
# Load Dataset
# ============================================================================

print("=" * 70)
print("STATISTICAL INSIGHTS & PATTERN DETECTION")
print("=" * 70)

df = pd.read_csv(
    "../feature_engineered_data/crime_feature_engineered.csv",
    parse_dates=["date", "date_of_update"]
)

print("\nDataset Loaded Successfully.")

print(f"Rows : {len(df)}")
print(f"Columns : {len(df.columns)}")


# ============================================================================
# Configure Visualization
# ============================================================================

plt.style.use("ggplot")

sns.set_theme(style="whitegrid")

plt.rcParams["figure.figsize"] = (10,6)

plt.rcParams["font.size"] = 11


# ============================================================================
# Crime Intensity by Time
# ============================================================================

print("\nAnalyzing Crime Intensity by Time...")
print("-" * 70)

crimes_by_hour = (
    df.groupby("Hour")
      .size()
      .reset_index(name="Crime_Count")
      .sort_values(by="Hour")
)

print("\nCrime Count by Hour")

print(crimes_by_hour)


# ============================================================================
# Plot Crime Count by Hour
# ============================================================================

plt.figure(figsize=(12,6))

sns.lineplot(
    data=crimes_by_hour,
    x="Hour",
    y="Crime_Count",
    marker="o",
    linewidth=2
)

plt.title("Crime Intensity by Hour of the Day")

plt.xlabel("Hour (24-Hour Format)")

plt.ylabel("Number of Crimes")

plt.xticks(range(24))

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "../graphs/statistical_analysis/crime_by_hour.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nCrime by Hour graph saved successfully.")


# ============================================================================
# Business Observation
# ============================================================================

print("\nBusiness Observation")
print("-" * 70)

peak_hour = crimes_by_hour.loc[
    crimes_by_hour["Crime_Count"].idxmax()
]

least_hour = crimes_by_hour.loc[
    crimes_by_hour["Crime_Count"].idxmin()
]

print(f"Peak Crime Hour      : {int(peak_hour['Hour']):02d}:00")
print(f"Number of Crimes     : {int(peak_hour['Crime_Count'])}")

print()

print(f"Least Crime Hour     : {int(least_hour['Hour']):02d}:00")
print(f"Number of Crimes     : {int(least_hour['Crime_Count'])}")


# ============================================================================
# Additional Statistics
# ============================================================================

print("\nAdditional Statistics")
print("-" * 70)

print(f"Average Crimes per Hour : {crimes_by_hour['Crime_Count'].mean():.2f}")

print(f"Maximum Crimes in an Hour : {int(crimes_by_hour['Crime_Count'].max())}")

print(f"Minimum Crimes in an Hour : {int(crimes_by_hour['Crime_Count'].min())}")


# ============================================================================
# Community Area Crime Counts
# ============================================================================

print("\nAnalyzing Community Area Outliers...")
print("-" * 70)

community_crimes = (
    df.groupby("community_code")
      .size()
      .reset_index(name="Crime_Count")
      .sort_values(by="Crime_Count")
)

print("\nCrime Count per Community Area")

print(community_crimes)


# ============================================================================
# Mean Crime Count using NumPy
# ============================================================================

mean_crimes = np.mean(community_crimes["Crime_Count"])

print(f"\nAverage Crimes per Community Area : {mean_crimes:.2f}")


# ============================================================================
# Box Plot
# ============================================================================

plt.figure(figsize=(10,6))

sns.boxplot(
    y=community_crimes["Crime_Count"]
)

plt.title("Crime Count Distribution Across Community Areas")

plt.ylabel("Crime Count")

plt.tight_layout()

plt.savefig(
    "../graphs/statistical_analysis/community_area_boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nCommunity Area Box Plot saved successfully.")


# ============================================================================
# IQR Method
# ============================================================================

Q1 = community_crimes["Crime_Count"].quantile(0.25)

Q3 = community_crimes["Crime_Count"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)

upper_bound = Q3 + (1.5 * IQR)

print("\nIQR Statistics")
print("-" * 70)

print(f"Q1            : {Q1}")
print(f"Q3            : {Q3}")
print(f"IQR           : {IQR:.2f}")
print(f"Lower Bound   : {lower_bound:.2f}")
print(f"Upper Bound   : {upper_bound:.2f}")


# ============================================================================
# Detect Outliers
# ============================================================================

outliers = community_crimes[
    community_crimes["Crime_Count"] > upper_bound
]

print("\nOutlier Community Areas")
print("-" * 70)

if outliers.empty:
    print("No Outlier Community Areas Found.")
else:
    print(outliers)


# ============================================================================
# Business Observation
# ============================================================================

print("\nBusiness Observation")
print("-" * 70)

print(f"Average Crimes per Community : {mean_crimes:.2f}")

print(f"Total Community Areas        : {len(community_crimes)}")

print(f"Outlier Areas Identified     : {len(outliers)}")

if not outliers.empty:

    print("\nHigh Crime Community Areas")

    for _, row in outliers.iterrows():

        print(
            f"Community Area {int(row['community_code'])} "
            f"-> {int(row['Crime_Count'])} Crimes"
        )


# ============================================================================
# Crime Cross-Correlation Analysis
# ============================================================================

print("\nAnalyzing Correlation Between Numerical Features...")
print("-" * 70)

numeric_df = df[
    [
        "Year",
        "Month",
        "Hour",
        "arrest",
        "domestic",
        "beat_num",
        "district_code",
        "ward_no",
        "community_code",
        "latitude",
        "longitude"
    ]
].copy()

# Convert Boolean columns to integers
numeric_df["arrest"] = numeric_df["arrest"].astype(int)
numeric_df["domestic"] = numeric_df["domestic"].astype(int)

print("\nSelected Numerical Columns")

print(numeric_df.head())


# ============================================================================
# Correlation Matrix
# ============================================================================

correlation_matrix = numeric_df.corr()

print("\nCorrelation Matrix")
print("-" * 70)

print(correlation_matrix)


# ============================================================================
# Correlation Heatmap
# ============================================================================

plt.figure(figsize=(12, 10))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Matrix of Numerical Features")

plt.tight_layout()

plt.savefig(
    "../graphs/statistical_analysis/correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nCorrelation Heatmap saved successfully.")


# ============================================================================
# Strongest Correlations
# ============================================================================

print("\nHighest Correlations")
print("-" * 70)

corr_pairs = (
    correlation_matrix.where(
        np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool)
    )
    .stack()
    .sort_values(ascending=False)
)

print(corr_pairs.head(10))


# ============================================================================
# Business Observation
# ============================================================================

print("\nBusiness Observation")
print("-" * 70)

highest_corr = corr_pairs.index[0]
highest_value = corr_pairs.iloc[0]

print(
    f"Strongest Positive Correlation : "
    f"{highest_corr[0]} ↔ {highest_corr[1]}"
)

print(f"Correlation Value : {highest_value:.2f}")

print("\nCorrelation analysis completed successfully.")


