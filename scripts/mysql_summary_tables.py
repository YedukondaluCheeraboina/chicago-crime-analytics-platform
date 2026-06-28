"""
===============================================================================
Project    : Chicago Crime Data Analytics
Use Case   : 4 - MySQL Reporting & Integration
File       : mysql_summary_tables.py

Description:
This script creates summary reporting tables inside MySQL and populates
them using aggregated data from the crime table.

Summary Tables Created:

1. crime_yearly_summary
2. crime_category_summary

Author : Yedukondalu Cheeraboina(y.cheeraboina@accenture.com)
===============================================================================
"""

import mysql.connector

from mysql_connection import get_connection


print("=" * 70)
print("MYSQL SUMMARY TABLES")
print("=" * 70)

connection = get_connection()

cursor = connection.cursor()

print("\nDatabase Connected Successfully.")


cursor.execute("""

CREATE TABLE IF NOT EXISTS crime_yearly_summary(

    Year INT PRIMARY KEY,

    Crime_Count INT,

    Arrest_Count INT,

    Arrest_Rate DECIMAL(6,2)

)

""")


cursor.execute("""

INSERT INTO crime_yearly_summary

SELECT

Year,

COUNT(*) AS Crime_Count,

SUM(arrest) AS Arrest_Count,

ROUND((SUM(arrest)/COUNT(*))*100,2)

FROM crime

GROUP BY Year

ON DUPLICATE KEY UPDATE

Crime_Count=VALUES(Crime_Count),

Arrest_Count=VALUES(Arrest_Count),

Arrest_Rate=VALUES(Arrest_Rate)

""")


cursor.execute("""

CREATE TABLE IF NOT EXISTS crime_category_summary(

Primary_Type VARCHAR(100) PRIMARY KEY,

Crime_Count INT,

Crime_Percentage DECIMAL(6,2)

)

""")


cursor.execute("""

INSERT INTO crime_category_summary

SELECT

primary_type,

COUNT(*),

ROUND(COUNT(*)*100/(SELECT COUNT(*) FROM crime),2)

FROM crime

GROUP BY primary_type

ON DUPLICATE KEY UPDATE

Crime_Count=VALUES(Crime_Count),

Crime_Percentage=VALUES(Crime_Percentage)

""")


connection.commit()

print("\nSummary Tables Created Successfully.")


cursor.execute("SELECT COUNT(*) FROM crime_yearly_summary")

print(
    "Year Summary Records :",
    cursor.fetchone()[0]
)

cursor.execute("SELECT COUNT(*) FROM crime_category_summary")

print(
    "Category Summary Records :",
    cursor.fetchone()[0]
)


cursor.close()

connection.close()

print("\nDatabase Connection Closed.")