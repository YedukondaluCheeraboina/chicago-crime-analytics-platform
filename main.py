"""
===============================================================================
Project    : Chicago Crime Data Analytics
File       : main.py

Description:
This script executes the complete Chicago Crime Analytics Pipeline.

Execution Flow

1. Load Dataset
2. Data Cleaning
3. Feature Engineering
4. Load Data into MySQL
5. Exploratory Data Analysis
6. Statistical Analysis
7. Create Summary Tables
8. Create MySQL Views
9. Generate Reports
10. Generate Visualizations

Author : Yedukondalu Cheeraboina(y.cheeraboina@accenture.com)
===============================================================================
"""

# ============================================================================
# Import Required Libraries
# ============================================================================

import subprocess
import sys
import time

# ============================================================================
# List of Project Modules
# ============================================================================

modules = [
    "load_data.py",
    "data_cleaning.py",
    "feature_engineering.py",
    "load_to_mysql.py",
    "exploratory_analysis.py",
    "statistical_analysis.py",
    "mysql_summary_tables.py",
    "mysql_views.py",
    "mysql_reporting.py",
    "mysql_visualization.py"
]

# ============================================================================
# Start Pipeline
# ============================================================================

print("=" * 80)
print("CHICAGO CRIME DATA ANALYTICS PIPELINE")
print("=" * 80)

start_time = time.time()

success = True

# ============================================================================
# Execute Modules One by One
# ============================================================================

for module in modules:

    print("\n" + "=" * 80)
    print(f"Running Module : {module}")
    print("=" * 80)

    result = subprocess.run(
        [sys.executable, module],
        cwd="scripts"
    )

    if result.returncode == 0:

        print(f"\n{module} executed successfully.")

    else:

        print(f"\nError while executing {module}")

        success = False

        break

# ============================================================================
# Pipeline Summary
# ============================================================================

end_time = time.time()

execution_time = end_time - start_time

print("\n" + "=" * 80)
print("PIPELINE EXECUTION SUMMARY")
print("=" * 80)

print(f"Total Modules           : {len(modules)}")

if success:
    print("Execution Status        : SUCCESS")
else:
    print("Execution Status        : FAILED")

print(f"Total Execution Time    : {execution_time:.2f} seconds")

# ============================================================================
# Final Message
# ============================================================================

print("\n" + "=" * 80)

if success:

    print("CHICAGO CRIME DATA ANALYTICS PROJECT COMPLETED SUCCESSFULLY")

else:

    print("PROJECT EXECUTION TERMINATED DUE TO ERRORS")

print("=" * 80)