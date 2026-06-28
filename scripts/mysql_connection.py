"""
===============================================================================
                    Chicago Crime Analytics Platform
===============================================================================

File        : mysql_connection.py

Description:
Provides a reusable MySQL database connection for the ETL pipeline.

Features
--------
1. Loads credentials from .env
2. Creates the database if it does not exist
3. Connects to the target database
4. Returns a reusable connection object

Author      : Yedukondalu Cheeraboina
===============================================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path
import sys

# ----------------------------------------------------------
# Add Project Root to Python Path
# ----------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import mysql.connector

from utils.database_config import get_database_config

# ==========================================================
# Database Connection
# ==========================================================

def get_connection():
    """
    Creates a MySQL connection and returns
    the connected database object.
    """

    config = get_database_config()

    try:

        print("=" * 70)
        print("CONNECTING TO MYSQL SERVER")
        print("=" * 70)

        # --------------------------------------------------
        # Connect to MySQL Server
        # --------------------------------------------------

        connection = mysql.connector.connect(

            host=config["host"],

            port=config["port"],

            user=config["user"],

            password=config["password"]

        )

        if connection.is_connected():

            print("✓ Connected to MySQL Server")

            cursor = connection.cursor()

            cursor.execute(

                f"CREATE DATABASE IF NOT EXISTS {config['database']}"

            )

            print(
                f"✓ Database '{config['database']}' verified."
            )

            cursor.close()

            connection.close()

        # --------------------------------------------------
        # Connect to Project Database
        # --------------------------------------------------

        db_connection = mysql.connector.connect(

            host=config["host"],

            port=config["port"],

            user=config["user"],

            password=config["password"],

            database=config["database"],

            charset=config["charset"]

        )

        if db_connection.is_connected():

            print(
                f"✓ Connected to '{config['database']}' successfully."
            )

        return db_connection

    except mysql.connector.Error as error:

        print("\n✗ Database Connection Failed")

        print(error)

        return None


# ==========================================================
# Test Connection
# ==========================================================

if __name__ == "__main__":

    connection = get_connection()

    if connection:

        print("\n✓ Connection Test Successful")

        connection.close()

        print("✓ Connection Closed")

    else:

        print("\n✗ Connection Test Failed")