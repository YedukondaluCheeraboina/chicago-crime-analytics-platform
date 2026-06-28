"""
===============================================================================
Project    : Chicago Crime Data Analytics
Use Case   : 1 - Load and Clean Chicago Crime Data
File       : data_cleaning.py

Description:
This script performs data cleaning on the Chicago Crime Dataset.

Tasks Performed:
1. Load the dataset
2. Display initial dataset information
3. Convert date columns to datetime
4. Validate date conversion
5. Standardize categorical columns
6. Handle missing values
7. Calculate missing percentage using NumPy
8. Identify columns having >50% missing values
9. Validate cleaned dataset
10. Display cleaning summary
11. Save cleaned dataset

Author     : Yedukondalu Cheeraboina(y.cheeraboina@accenture.com)
===============================================================================
"""

# ============================================================================
# Import Required Libraries
# ============================================================================

import pandas as pd
import numpy as np

# ============================================================================
# Load Dataset
# ============================================================================

print("=" * 70)
print("CHICAGO CRIME DATA CLEANING")
print("=" * 70)

df = pd.read_csv("../datasets/chicago_crime_dataset.csv")

print("\nDataset loaded successfully.")

# ============================================================================
# Initial Dataset Information
# ============================================================================

print("\nInitial Dataset Information")
print("-" * 50)

print("Shape :", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# ============================================================================
# Convert Date Columns
# ============================================================================

print("\nConverting Date Columns...")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["date_of_update"] = pd.to_datetime(df["date_of_update"], errors="coerce")

print("Date columns converted successfully.")

# ============================================================================
# Validate Date Conversion
# ============================================================================

print("\nChecking Invalid Dates")

print("Invalid values in 'date' column          :", df["date"].isna().sum())
print("Invalid values in 'date_of_update' column:",
      df["date_of_update"].isna().sum())

# ============================================================================
# Verify Data Types
# ============================================================================

print("\nData Types After Date Conversion")
print(df.dtypes)

# ============================================================================
# Standardize Text Columns
# ============================================================================

print("\nStandardizing Categorical Columns...")

text_columns = [
    "primary_type",
    "description",
    "location_desc",
    "block"
]

for col in text_columns:
    df[col] = (
        df[col]
        .astype("string")
        .str.strip()
        .str.upper()
    )

print("Categorical columns standardized.")

# ============================================================================
# Handle Missing Values
# ============================================================================

print("\nHandling Missing Values...")

# Replace missing location descriptions
df["location_desc"] = df["location_desc"].fillna("UNKNOWN")

# Fill numeric categorical values using median
df["ward_no"] = df["ward_no"].fillna(df["ward_no"].median())
df["community_code"] = df["community_code"].fillna(df["community_code"].median())

# Fill coordinate columns using mean
coordinate_columns = [
    "x_coordinate",
    "y_coordinate",
    "latitude",
    "longitude"
]

for col in coordinate_columns:
    df[col] = df[col].fillna(df[col].mean())

# Fill missing location
df["location"] = df["location"].fillna("UNKNOWN")

print("Missing values handled successfully.")

# ============================================================================
# Verify Missing Values
# ============================================================================

print("\nMissing Values After Cleaning")

print(df.isnull().sum())

# ============================================================================
# Duplicate Check
# ============================================================================

print("\nDuplicate Rows :", df.duplicated().sum())

# ============================================================================
# Missing Percentage Using NumPy
# ============================================================================

print("\nMissing Percentage Per Column")

missing_percentage = np.round(
    (df.isnull().sum() / len(df)) * 100,
    2
)

print(missing_percentage)

# ============================================================================
# Columns Having More Than 50% Missing Values
# ============================================================================

columns_to_drop = missing_percentage[missing_percentage > 50].index.tolist()

print("\nColumns with More Than 50% Missing Values")

if len(columns_to_drop) == 0:
    print("No columns need to be dropped.")
else:
    print(columns_to_drop)

# ============================================================================
# Unique Crime Types
# ============================================================================

print("\nUnique Crime Types")

print("Number of Crime Types :", df["primary_type"].nunique())

# ============================================================================
# Date Range
# ============================================================================

print("\nDate Range")

print("Earliest Crime :", df["date"].min())
print("Latest Crime   :", df["date"].max())

# ============================================================================
# Coordinate Validation
# ============================================================================

print("\nCoordinate Validation")

invalid_latitude = (df["latitude"] < 0).sum()

invalid_longitude = (df["longitude"] > 0).sum()

print("Invalid Latitude  :", invalid_latitude)

print("Invalid Longitude :", invalid_longitude)

# ============================================================================
# Final Dataset Information
# ============================================================================

print("\nFinal Dataset Information")

print(df.info())

# ============================================================================
# Data Cleaning Summary
# ============================================================================

print("\n" + "=" * 70)
print("DATA CLEANING SUMMARY")
print("=" * 70)

print(f"Total Records           : {len(df)}")
print(f"Total Columns           : {len(df.columns)}")
print(f"Remaining Missing Values: {df.isnull().sum().sum()}")
print(f"Duplicate Records       : {df.duplicated().sum()}")
print(f"Unique Crime Types      : {df['primary_type'].nunique()}")
print(f"Date Range              : {df['date'].min()} to {df['date'].max()}")

print("\nData Cleaning Completed Successfully.")

# ============================================================================
# Save Cleaned Dataset
# ============================================================================

output_path = "../cleaned_data/crime_cleaned_stage1.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully.")

print(f"Location : {output_path}")

print("\nProcess Completed Successfully.")

print("=" * 70)