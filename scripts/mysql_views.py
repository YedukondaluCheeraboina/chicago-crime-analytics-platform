"""
===============================================================================
Project    : Chicago Crime Data Analytics
Use Case   : 4 - MySQL Reporting & Integration
File       : mysql_views.py

Description:
This script creates MySQL views for reporting purposes.

Views Created:
1. vw_crime_yearly
2. vw_crime_by_category

Author : Yeduondalu Cheeraboina(y.cheeraboina@accentue.com)
===============================================================================
"""


# ============================================================================
# Import Required Libraries
# ============================================================================

import mysql.connector

from mysql_connection import get_connection


# ============================================================================
# Connect to Database
# ============================================================================

print("=" * 70)
print("MYSQL REPORTING VIEWS")
print("=" * 70)

connection = get_connection()

cursor = connection.cursor()

print("\nDatabase Connected Successfully.")


# ============================================================================
# Create Yearly Crime View
# ============================================================================

cursor.execute("""

CREATE OR REPLACE VIEW vw_crime_yearly AS

SELECT

Year,
Crime_Count,
Arrest_Count,
Arrest_Rate

FROM crime_yearly_summary

""")

print("\nView 'vw_crime_yearly' created successfully.")


# ============================================================================
# Create Crime Category View
# ============================================================================

cursor.execute("""

CREATE OR REPLACE VIEW vw_crime_by_category AS

SELECT

Primary_Type,
Crime_Count,
Crime_Percentage

FROM crime_category_summary

""")

print("View 'vw_crime_by_category' created successfully.")


# ============================================================================
# Commit Changes
# ============================================================================

connection.commit()


# ============================================================================
# Verify Views
# ============================================================================

cursor.execute("""

SHOW FULL TABLES
WHERE Table_type='VIEW'

""")

views = cursor.fetchall()

print("\nAvailable Views")
print("-" * 70)

for view in views:
    print(view[0])


# ============================================================================
# Close Connection
# ============================================================================

cursor.close()

connection.close()

print("\nDatabase Connection Closed.")

print("\nProcess Completed Successfully.")

print("=" * 70)


