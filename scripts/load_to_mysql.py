"""
===============================================================================
Project    : Chicago Crime Data Analytics
Use Case   : 1 - Load Feature Engineered Data into MySQL
File       : load_to_mysql.py

Description:
This script loads the feature-engineered Chicago Crime Dataset into
the MySQL Data Warehouse.

Tasks Performed:
1. Load feature engineered dataset
2. Connect to MySQL
3. Create crime table
4. Insert all records
5. Verify inserted records
6. Close database connection

Input  :
    ../feature_engineered_data/crime_feature_engineered.csv

Output :
    Crime table populated in chicago_crime_db

Author : Yedukondalu Cheeraboina(y.cheeraboina@accenture.com)
===============================================================================
"""

# ============================================================================
# Import Required Libraries
# ============================================================================

import pandas as pd
import mysql.connector

from mysql_connection import get_connection


# ============================================================================
# Load Feature Engineered Dataset
# ============================================================================

print("=" * 70)
print("LOADING FEATURE ENGINEERED DATASET")
print("=" * 70)

df = pd.read_csv(
    "../feature_engineered_data/crime_feature_engineered.csv"
)

print("\nDataset loaded successfully.")

print(f"Total Records : {len(df)}")
print(f"Total Columns : {len(df.columns)}")


# ============================================================================
# Establish MySQL Connection
# ============================================================================

print("\nConnecting to MySQL Database...")
print("-" * 70)

connection = get_connection()

if connection is None:
    print("Failed to establish database connection.")
    exit()

cursor = connection.cursor()

print("Database connection established successfully.")


# ============================================================================
# Create Crime Table
# ============================================================================

print("\nCreating Crime Table...")
print("-" * 70)

create_table_query = """
CREATE TABLE IF NOT EXISTS crime (

    id BIGINT PRIMARY KEY,

    case_number VARCHAR(20),

    date DATETIME,

    block VARCHAR(100),

    iucr_code INT,

    primary_type VARCHAR(100),

    description VARCHAR(255),

    location_desc VARCHAR(150),

    arrest BOOLEAN,

    domestic BOOLEAN,

    beat_num INT,

    district_code INT,

    ward_no INT,

    community_code INT,

    fbi_code VARCHAR(10),

    x_coordinate DOUBLE,

    y_coordinate DOUBLE,

    date_of_update DATETIME,

    latitude DOUBLE,

    longitude DOUBLE,

    location VARCHAR(100),

    Year INT,

    Month INT,

    MonthName VARCHAR(20),

    DayOfWeek VARCHAR(20),

    Hour INT

)
"""

cursor.execute(create_table_query)

connection.commit()

print("Crime table created successfully.")


# ============================================================================
# Insert Records into Crime Table
# ============================================================================

print("\nInserting Records into Crime Table...")
print("-" * 70)

# Optional: Clear existing records before inserting
cursor.execute("TRUNCATE TABLE crime")

insert_query = """
INSERT INTO crime (
    id,
    case_number,
    date,
    block,
    iucr_code,
    primary_type,
    description,
    location_desc,
    arrest,
    domestic,
    beat_num,
    district_code,
    ward_no,
    community_code,
    fbi_code,
    x_coordinate,
    y_coordinate,
    date_of_update,
    latitude,
    longitude,
    location,
    Year,
    Month,
    MonthName,
    DayOfWeek,
    Hour
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s
)
"""

records = list(df.itertuples(index=False, name=None))

cursor.executemany(insert_query, records)

connection.commit()

print(f"{cursor.rowcount} records inserted successfully.")


# ============================================================================
# Verify Inserted Records
# ============================================================================

print("\nVerifying Inserted Records...")
print("-" * 70)

cursor.execute("SELECT COUNT(*) FROM crime")

record_count = cursor.fetchone()[0]

print(f"Total Records Available in Database : {record_count}")


# ============================================================================
# Close Database Connection
# ============================================================================

cursor.close()
connection.close()

print("\nDatabase connection closed successfully.")

print("\n" + "=" * 70)
print("DATA LOADING COMPLETED SUCCESSFULLY")
print("=" * 70)