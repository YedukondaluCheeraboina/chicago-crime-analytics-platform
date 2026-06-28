"""
===============================================================================
Project    : Chicago Crime Data Analytics
Use Case   : 1 - Load and Explore Chicago Crime Dataset
File       : load_data.py

Description:
This script performs the initial exploration of the Chicago Crime Dataset.

Tasks Performed:
1. Load the crime dataset from CSV
2. Display sample records
3. Display dataset dimensions
4. Display column names
5. Display data types
6. Display dataset information
7. Identify missing values
8. Identify duplicate records
9. Display statistical summary
10. Explore categorical columns

Author     : Yedukondalu Cheeraboina(y.cheeraboina@accenture.com)
===============================================================================
"""

# ============================================================================
# Import Required Libraries
# ============================================================================

import pandas as pd

# ============================================================================
# Load Dataset
# ============================================================================

print("=" * 70)
print("CHICAGO CRIME DATASET EXPLORATION")
print("=" * 70)

# Read CSV file into a Pandas DataFrame
df = pd.read_csv("../datasets/chicago_crime_dataset.csv")

print("\nDataset loaded successfully.")

# ============================================================================
# Display Sample Records
# ============================================================================

print("\nFirst 10 Records")
print("-" * 70)

print(df.head(10))

# ============================================================================
# Dataset Shape
# ============================================================================

print("\nDataset Shape")
print("-" * 70)

rows, columns = df.shape

print(f"Total Rows    : {rows}")
print(f"Total Columns : {columns}")

# ============================================================================
# Column Names
# ============================================================================

print("\nColumn Names")
print("-" * 70)

for column in df.columns:
    print(column)

# ============================================================================
# Data Types
# ============================================================================

print("\nData Types")
print("-" * 70)

print(df.dtypes)

# ============================================================================
# Dataset Information
# ============================================================================

print("\nDataset Information")
print("-" * 70)

print(df.info())

# ============================================================================
# Missing Values
# ============================================================================

print("\nMissing Values")
print("-" * 70)

missing_values = df.isnull().sum()

print(missing_values)

# ============================================================================
# Duplicate Records
# ============================================================================

print("\nDuplicate Records")
print("-" * 70)

duplicates = df.duplicated().sum()

print(f"Duplicate Rows : {duplicates}")

# ============================================================================
# Numerical Statistics
# ============================================================================

print("\nNumerical Statistics")
print("-" * 70)

print(df.describe())

# ============================================================================
# Categorical Statistics
# ============================================================================

print("\nCategorical Statistics")
print("-" * 70)

print(df.describe(include="object"))

# ============================================================================
# Inspect Important Text Columns
# ============================================================================

print("\nInspecting Important Categorical Columns")
print("-" * 70)

text_columns = [
    "primary_type",
    "description",
    "location_desc",
    "block"
]

for column in text_columns:
    print(f"\nColumn : {column}")
    print(df[column].dropna().head())

# ============================================================================
# Dataset Exploration Summary
# ============================================================================

print("\n" + "=" * 70)
print("DATASET EXPLORATION SUMMARY")
print("=" * 70)

print(f"Total Records       : {rows}")
print(f"Total Columns       : {columns}")
print(f"Missing Values      : {missing_values.sum()}")
print(f"Duplicate Records   : {duplicates}")
print(f"Unique Crime Types  : {df['primary_type'].nunique()}")
print(f"Year Range          : {df['year'].min()} - {df['year'].max()}")

print("\nDataset exploration completed successfully.")

print("=" * 70)