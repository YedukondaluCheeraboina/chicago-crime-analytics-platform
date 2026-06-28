/******************************************************************************
===============================================================================
                    CHICAGO CRIME ANALYTICS PLATFORM
===============================================================================

File        : database_schema.sql

Description :
Creates the complete database schema required for the
Chicago Crime Analytics Platform.

The schema includes:

1. Database Creation
2. Primary Crime Table
3. Analytical Summary Tables
4. Performance Indexes
5. Reporting Views
6. Verification Queries

Author      : Yedukondalu Cheeraboina

Database    : MySQL 8.x

===============================================================================
******************************************************************************/

-- ============================================================================
-- Remove Existing Database (Optional)
-- ============================================================================

DROP DATABASE IF EXISTS chicago_crime_db;


-- ============================================================================
-- Create Database
-- ============================================================================

CREATE DATABASE chicago_crime_db;


-- ============================================================================
-- Use Database
-- ============================================================================

USE chicago_crime_db;


-- ============================================================================
-- Database Information
-- ============================================================================

SELECT DATABASE() AS Current_Database;


-- ============================================================================
-- Main Crime Table
-- ============================================================================

CREATE TABLE crime (

    id BIGINT PRIMARY KEY,

    case_number VARCHAR(30) NOT NULL,

    date DATETIME,

    block VARCHAR(255),

    iucr_code VARCHAR(20),

    primary_type VARCHAR(120),

    description VARCHAR(255),

    location_desc VARCHAR(255),

    arrest BOOLEAN,

    domestic BOOLEAN,

    beat_num INT,

    district_code INT,

    ward_no INT,

    community_code INT,

    fbi_code VARCHAR(20),

    x_coordinate DOUBLE,

    y_coordinate DOUBLE,

    date_of_update DATETIME,

    latitude DOUBLE,

    longitude DOUBLE,

    location VARCHAR(120),

    Year INT,

    Month INT,

    MonthName VARCHAR(20),

    DayOfWeek VARCHAR(20),

    Hour INT

);

/******************************************************************************
===============================================================================
                        ANALYTICAL SUMMARY TABLES
===============================================================================
These tables are populated after the ETL process and are used by
the Streamlit dashboards and reporting modules.
===============================================================================
******************************************************************************/


-- ============================================================================
-- Yearly Crime Summary
-- ============================================================================

CREATE TABLE crime_yearly_summary (

    Year INT PRIMARY KEY,

    Crime_Count INT NOT NULL,

    Arrest_Count INT NOT NULL,

    Arrest_Rate DECIMAL(8,2) NOT NULL

);


-- ============================================================================
-- Crime Category Summary
-- ============================================================================

CREATE TABLE crime_category_summary (

    Primary_Type VARCHAR(120) PRIMARY KEY,

    Crime_Count INT NOT NULL,

    Crime_Percentage DECIMAL(8,2) NOT NULL

);


-- ============================================================================
-- Community Crime Summary
-- ============================================================================

CREATE TABLE crime_community_summary (

    Community_Code INT PRIMARY KEY,

    Crime_Count INT NOT NULL,

    Arrest_Count INT NOT NULL,

    Arrest_Rate DECIMAL(8,2) NOT NULL

);


-- ============================================================================
-- District Crime Summary
-- ============================================================================

CREATE TABLE crime_district_summary (

    District_Code INT PRIMARY KEY,

    Crime_Count INT NOT NULL,

    Arrest_Count INT NOT NULL,

    Arrest_Rate DECIMAL(8,2) NOT NULL

);


-- ============================================================================
-- Monthly Crime Summary
-- ============================================================================

CREATE TABLE crime_monthly_summary (

    Month INT PRIMARY KEY,

    MonthName VARCHAR(20),

    Crime_Count INT NOT NULL,

    Arrest_Count INT NOT NULL,

    Arrest_Rate DECIMAL(8,2) NOT NULL

);


-- ============================================================================
-- Day of Week Summary
-- ============================================================================

CREATE TABLE crime_day_summary (

    DayOfWeek VARCHAR(20) PRIMARY KEY,

    Crime_Count INT NOT NULL,

    Arrest_Count INT NOT NULL,

    Arrest_Rate DECIMAL(8,2) NOT NULL

);


-- ============================================================================
-- Hourly Crime Summary
-- ============================================================================

CREATE TABLE crime_hourly_summary (

    Hour INT PRIMARY KEY,

    Crime_Count INT NOT NULL,

    Arrest_Count INT NOT NULL,

    Arrest_Rate DECIMAL(8,2) NOT NULL

);

/******************************************************************************
===============================================================================
                            PERFORMANCE INDEXES
===============================================================================
Indexes improve query performance for dashboards, reports,
filtering, grouping and statistical analysis.
===============================================================================
******************************************************************************/


-- ============================================================================
-- Primary Filtering Indexes
-- ============================================================================

CREATE INDEX idx_crime_year
ON crime (Year);

CREATE INDEX idx_crime_month
ON crime (Month);

CREATE INDEX idx_crime_day
ON crime (DayOfWeek);

CREATE INDEX idx_crime_hour
ON crime (Hour);

CREATE INDEX idx_crime_type
ON crime (primary_type);

CREATE INDEX idx_crime_arrest
ON crime (arrest);

CREATE INDEX idx_crime_domestic
ON crime (domestic);


-- ============================================================================
-- Location Indexes
-- ============================================================================

CREATE INDEX idx_crime_district
ON crime (district_code);

CREATE INDEX idx_crime_community
ON crime (community_code);

CREATE INDEX idx_crime_ward
ON crime (ward_no);

CREATE INDEX idx_crime_beat
ON crime (beat_num);


-- ============================================================================
-- Geographic Indexes
-- ============================================================================

CREATE INDEX idx_crime_latitude
ON crime (latitude);

CREATE INDEX idx_crime_longitude
ON crime (longitude);


-- ============================================================================
-- Composite Indexes
-- ============================================================================

CREATE INDEX idx_year_type
ON crime (Year, primary_type);

CREATE INDEX idx_year_district
ON crime (Year, district_code);

CREATE INDEX idx_year_community
ON crime (Year, community_code);

CREATE INDEX idx_month_type
ON crime (Month, primary_type);

CREATE INDEX idx_arrest_type
ON crime (arrest, primary_type);

CREATE INDEX idx_location
ON crime (district_code, community_code);


-- ============================================================================
-- Summary Table Indexes
-- ============================================================================

CREATE INDEX idx_category_count
ON crime_category_summary (Crime_Count);

CREATE INDEX idx_year_count
ON crime_yearly_summary (Crime_Count);

CREATE INDEX idx_community_count
ON crime_community_summary (Crime_Count);

CREATE INDEX idx_district_count
ON crime_district_summary (Crime_Count);

CREATE INDEX idx_month_count
ON crime_monthly_summary (Crime_Count);

CREATE INDEX idx_hour_count
ON crime_hourly_summary (Crime_Count);

/******************************************************************************
===============================================================================
                              REPORTING VIEWS
===============================================================================
These analytical views simplify SQL reporting and improve
maintainability by centralizing frequently used aggregations.
===============================================================================
******************************************************************************/


-- ============================================================================
-- Yearly Crime Summary View
-- ============================================================================

CREATE OR REPLACE VIEW vw_crime_yearly AS

SELECT

    Year,

    COUNT(*) AS Crime_Count,

    SUM(arrest = TRUE) AS Arrest_Count,

    ROUND(AVG(arrest) * 100, 2) AS Arrest_Rate

FROM crime

GROUP BY Year

ORDER BY Year;


-- ============================================================================
-- Crime Category View
-- ============================================================================

CREATE OR REPLACE VIEW vw_crime_category AS

SELECT

    primary_type,

    COUNT(*) AS Crime_Count,

    ROUND(
        COUNT(*) * 100 /
        (SELECT COUNT(*) FROM crime),
        2
    ) AS Crime_Percentage

FROM crime

GROUP BY primary_type

ORDER BY Crime_Count DESC;


-- ============================================================================
-- Arrest Summary View
-- ============================================================================

CREATE OR REPLACE VIEW vw_arrest_summary AS

SELECT

    Year,

    SUM(arrest = TRUE) AS Arrest_Count,

    COUNT(*) AS Total_Crimes,

    ROUND(

        AVG(arrest) * 100,

        2

    ) AS Arrest_Rate

FROM crime

GROUP BY Year

ORDER BY Year;


-- ============================================================================
-- Community Crime View
-- ============================================================================

CREATE OR REPLACE VIEW vw_community_summary AS

SELECT

    community_code,

    COUNT(*) AS Crime_Count,

    SUM(arrest = TRUE) AS Arrest_Count,

    ROUND(

        AVG(arrest) * 100,

        2

    ) AS Arrest_Rate

FROM crime

GROUP BY community_code

ORDER BY Crime_Count DESC;


-- ============================================================================
-- District Crime View
-- ============================================================================

CREATE OR REPLACE VIEW vw_district_summary AS

SELECT

    district_code,

    COUNT(*) AS Crime_Count,

    SUM(arrest = TRUE) AS Arrest_Count,

    ROUND(

        AVG(arrest) * 100,

        2

    ) AS Arrest_Rate

FROM crime

GROUP BY district_code

ORDER BY Crime_Count DESC;


-- ============================================================================
-- Monthly Crime View
-- ============================================================================

CREATE OR REPLACE VIEW vw_monthly_summary AS

SELECT

    Month,

    MonthName,

    COUNT(*) AS Crime_Count,

    SUM(arrest = TRUE) AS Arrest_Count,

    ROUND(

        AVG(arrest) * 100,

        2

    ) AS Arrest_Rate

FROM crime

GROUP BY

    Month,

    MonthName

ORDER BY Month;


-- ============================================================================
-- Hourly Crime View
-- ============================================================================

CREATE OR REPLACE VIEW vw_hourly_summary AS

SELECT

    Hour,

    COUNT(*) AS Crime_Count,

    SUM(arrest = TRUE) AS Arrest_Count,

    ROUND(

        AVG(arrest) * 100,

        2

    ) AS Arrest_Rate

FROM crime

GROUP BY Hour

ORDER BY Hour;

/******************************************************************************
===============================================================================
                    DATABASE VERIFICATION & VALIDATION
===============================================================================
The following queries help verify that all database objects have been
created successfully and that the ETL process loaded the expected data.
===============================================================================
******************************************************************************/


-- ============================================================================
-- Verify Current Database
-- ============================================================================

SELECT DATABASE() AS Current_Database;


-- ============================================================================
-- Verify Tables
-- ============================================================================

SHOW TABLES;


-- ============================================================================
-- Verify Views
-- ============================================================================

SHOW FULL TABLES
WHERE TABLE_TYPE = 'VIEW';


-- ============================================================================
-- Verify Crime Table Structure
-- ============================================================================

DESCRIBE crime;


-- ============================================================================
-- Verify Summary Tables
-- ============================================================================

DESCRIBE crime_yearly_summary;

DESCRIBE crime_category_summary;

DESCRIBE crime_community_summary;

DESCRIBE crime_district_summary;

DESCRIBE crime_monthly_summary;

DESCRIBE crime_day_summary;

DESCRIBE crime_hourly_summary;


-- ============================================================================
-- Verify Total Records
-- ============================================================================

SELECT
    COUNT(*) AS Total_Crime_Records
FROM crime;


-- ============================================================================
-- Verify Distinct Years
-- ============================================================================

SELECT
    COUNT(DISTINCT Year) AS Total_Years
FROM crime;


-- ============================================================================
-- Verify Crime Categories
-- ============================================================================

SELECT
    COUNT(DISTINCT primary_type) AS Total_Crime_Categories
FROM crime;


-- ============================================================================
-- Verify Districts
-- ============================================================================

SELECT
    COUNT(DISTINCT district_code) AS Total_Districts
FROM crime;


-- ============================================================================
-- Verify Communities
-- ============================================================================

SELECT
    COUNT(DISTINCT community_code) AS Total_Communities
FROM crime;


-- ============================================================================
-- Verify Arrest Statistics
-- ============================================================================

SELECT

    COUNT(*) AS Total_Crimes,

    SUM(arrest = TRUE) AS Total_Arrests,

    ROUND(

        AVG(arrest) * 100,

        2

    ) AS Arrest_Rate

FROM crime;


-- ============================================================================
-- Verify Yearly View
-- ============================================================================

SELECT *
FROM vw_crime_yearly
LIMIT 10;


-- ============================================================================
-- Verify Category View
-- ============================================================================

SELECT *
FROM vw_crime_category
LIMIT 10;


-- ============================================================================
-- Verify Community View
-- ============================================================================

SELECT *
FROM vw_community_summary
LIMIT 10;


-- ============================================================================
-- Verify District View
-- ============================================================================

SELECT *
FROM vw_district_summary
LIMIT 10;


-- ============================================================================
-- Verify Monthly View
-- ============================================================================

SELECT *
FROM vw_monthly_summary
LIMIT 12;


-- ============================================================================
-- Verify Hourly View
-- ============================================================================

SELECT *
FROM vw_hourly_summary
LIMIT 24;


-- ============================================================================
-- Verify Database Size
-- ============================================================================

SELECT

    table_name,

    table_rows

FROM information_schema.tables

WHERE table_schema = 'chicago_crime_db'

ORDER BY table_name;


-- ============================================================================
-- Verify Indexes
-- ============================================================================

SHOW INDEXES
FROM crime;


-- ============================================================================
-- Database Setup Completed
-- ============================================================================

SELECT

'Chicago Crime Analytics Platform Database Successfully Created'
AS Status;

/******************************************************************************
===============================================================================
                        DATABASE SETUP COMPLETED
===============================================================================

The Chicago Crime Analytics Platform database has been successfully
configured.

The following database objects are now available:

Tables
------
1. crime
2. crime_yearly_summary
3. crime_category_summary
4. crime_community_summary
5. crime_district_summary
6. crime_monthly_summary
7. crime_day_summary
8. crime_hourly_summary

Views
-----
1. vw_crime_yearly
2. vw_crime_category
3. vw_arrest_summary
4. vw_community_summary
5. vw_district_summary
6. vw_monthly_summary
7. vw_hourly_summary

Indexes
-------
Optimized indexes have been created to improve:

• Dashboard performance
• Crime Analysis
• Statistical Analysis
• MySQL Reports
• Filtering
• Aggregation
• Grouping
• Reporting queries

===============================================================================
Recommended Project Execution Order
===============================================================================

Step 1
-------
Execute this script

database_schema.sql

Step 2
-------
Run the ETL Pipeline

python main.py

OR execute individual modules

load_data.py
data_cleaning.py
feature_engineering.py
load_to_mysql.py

Step 3
-------
Launch the Streamlit Application

streamlit run streamlit_app/app.py

===============================================================================
Compatibility
===============================================================================

Database Engine
---------------
MySQL 8.x or later

Python
------
Python 3.13+

Framework
---------
Streamlit 1.58+

===============================================================================
Future Database Enhancements
===============================================================================

Planned improvements include:

• Stored Procedures
• SQL Functions
• Database Triggers
• Event Scheduler
• Materialized Summary Tables
• Geospatial Crime Analysis
• Machine Learning Prediction Tables
• User Authentication Tables
• Audit Logging
• Historical Data Archiving

===============================================================================
Project Information
===============================================================================

Project Name

Chicago Crime Analytics Platform

Project Type

End-to-End Data Engineering &
Business Intelligence Platform

Modules

• ETL Pipeline
• MySQL Data Warehouse
• Interactive Streamlit Dashboard
• Statistical Analysis
• MySQL Reporting
• PDF Report Generation
• Excel Export
• CSV Export

Author

Yedukondalu Cheeraboina

Version

1.0.0

License

MIT License

===============================================================================
End of File
===============================================================================
******************************************************************************/