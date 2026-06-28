"""
===============================================================================
Project    : Chicago Crime Data Analytics
Use Case   : 1 - Feature Engineering
File       : feature_engineering.py

Description:
This script performs feature engineering on the cleaned Chicago Crime Dataset.

Tasks Performed:
1. Load the cleaned dataset
2. Display dataset information
3. Generate new features from the Date column
4. Verify and drop original redundant year column
5. Order DayOfWeek chronologically
6. Validate generated features
7. Display feature engineering summary
8. Save feature engineered dataset

Input  : ../cleaned_data/crime_cleaned_stage1.csv
Output : ../feature_engineered_data/crime_feature_engineered.csv

Author : Yedukondalu Cheeraoina(y.cheerabona@accenture.com)
===============================================================================
"""

# ============================================================================
# Import Required Libraries
# ============================================================================

import pandas as pd

# ============================================================================
# Load Cleaned Dataset
# ============================================================================

print("=" * 70)
print("CHICAGO CRIME DATA - FEATURE ENGINEERING")
print("=" * 70)

df = pd.read_csv(
    "../cleaned_data/crime_cleaned_stage1.csv",
    parse_dates=["date", "date_of_update"]
)

print("\nCleaned dataset loaded successfully.")

# ============================================================================
# Initial Dataset Information
# ============================================================================

print("\nDataset Information")
print("-" * 70)

print(f"Shape : {df.shape}")

print("\nColumns")

for column in df.columns:
    print(column)

print("\nData Types")
print(df.dtypes)

# ============================================================================
# Feature Engineering
# ============================================================================

print("\nGenerating New Features...")
print("-" * 70)

# Extract Year
df["Year"] = df["date"].dt.year

# Extract Month Number
df["Month"] = df["date"].dt.month

# Extract Month Name
df["MonthName"] = df["date"].dt.month_name()

# Extract Day Name
df["DayOfWeek"] = df["date"].dt.day_name()

# Extract Hour
df["Hour"] = df["date"].dt.hour

print("New features created successfully.")

# ============================================================================
# Verify Existing Year Column
# ============================================================================

print("\nVerifying Existing and Generated Year Columns")
print("-" * 70)

if (df["year"] == df["Year"]).all():
    print("Verification Successful: Both 'year' and 'Year' columns are identical.")

    # Drop original year column
    df.drop(columns=["year"], inplace=True)

    print("Original 'year' column dropped successfully.")
else:
    print("Warning: 'year' and 'Year' columns do not match.")
    print("Original 'year' column retained.")

# ============================================================================
# Arrange Day of Week Order
# ============================================================================

days_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

df["DayOfWeek"] = pd.Categorical(
    df["DayOfWeek"],
    categories=days_order,
    ordered=True
)

print("\nDayOfWeek column ordered successfully.")

# ============================================================================
# Display Newly Created Features
# ============================================================================

print("\nSample of Generated Features")
print("-" * 70)

print(df[
    [
        "date",
        "Year",
        "Month",
        "MonthName",
        "DayOfWeek",
        "Hour"
    ]
].head(10))

# ============================================================================
# Validate Generated Features
# ============================================================================

print("\nValidating Generated Features")
print("-" * 70)

print("\nYear Range")
print(sorted(df["Year"].unique()))

print("\nMonth Range")
print(sorted(df["Month"].unique()))

print("\nMonth Names")
print(df.groupby("Month")["MonthName"].first().tolist())

print("\nDays of Week")
print(df["DayOfWeek"].cat.categories.tolist())

print("\nHour Range")
print(sorted(df["Hour"].unique()))

# ============================================================================
# Missing Value Validation
# ============================================================================

print("\nMissing Values in Generated Features")
print("-" * 70)

generated_features = [
    "Year",
    "Month",
    "MonthName",
    "DayOfWeek",
    "Hour"
]

print(df[generated_features].isnull().sum())

# ============================================================================
# Feature Statistics
# ============================================================================

print("\nFeature Statistics")
print("-" * 70)

print(f"Minimum Year : {df['Year'].min()}")
print(f"Maximum Year : {df['Year'].max()}")

print(f"\nMinimum Month : {df['Month'].min()}")
print(f"Maximum Month : {df['Month'].max()}")

print(f"\nMinimum Hour : {df['Hour'].min()}")
print(f"Maximum Hour : {df['Hour'].max()}")

print(f"\nUnique Days of Week : {df['DayOfWeek'].nunique()}")
print(f"Unique Months       : {df['MonthName'].nunique()}")

# ============================================================================
# Final Dataset Information
# ============================================================================

print("\nFinal Dataset Information")
print("-" * 70)

print(df.info())

# ============================================================================
# Feature Engineering Summary
# ============================================================================

print("\n" + "=" * 70)
print("FEATURE ENGINEERING SUMMARY")
print("=" * 70)

print(f"Total Records              : {len(df)}")
print(f"Total Columns              : {len(df.columns)}")
print(f"Original Columns           : 22")
print(f"New Features Added         : 5")
print(f"Current Columns            : {len(df.columns)}")
print(f"Feature Engineered Dataset : crime_feature_engineered.csv")

print(f"\nYear Range                : {df['Year'].min()} - {df['Year'].max()}")
print(f"Month Range               : {df['Month'].min()} - {df['Month'].max()}")
print(f"Hour Range                : {df['Hour'].min()} - {df['Hour'].max()}")

print(f"\nUnique Crime Types        : {df['primary_type'].nunique()}")
print(f"Unique Days of Week       : {df['DayOfWeek'].nunique()}")
print(f"Unique Months             : {df['MonthName'].nunique()}")

print(f"\nMissing Values Remaining  : {df.isnull().sum().sum()}")
print(f"Duplicate Records         : {df.duplicated().sum()}")

print("\nFeature Engineering Completed Successfully.")

# ============================================================================
# Final Columns
# ============================================================================

print("\nFinal Columns")
print("-" * 70)

for column in df.columns:
    print(column)

# ============================================================================
# Save Feature Engineered Dataset
# ============================================================================

output_path = "../feature_engineered_data/crime_feature_engineered.csv"

df.to_csv(output_path, index=False)

print("\nFeature engineered dataset saved successfully.")

print(f"Location : {output_path}")

print("\nProcess Completed Successfully.")

print("=" * 70)
