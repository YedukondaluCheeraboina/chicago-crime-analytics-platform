"""
==========================================================
Database Configuration Utility
==========================================================

Loads database credentials from the .env file.

This module acts as the single source of truth for
database configuration across the entire project.

Project:
Chicago Crime Analytics Platform

Author:
Yedukondalu Cheeraboina
"""

# ==========================================================
# Imports
# ==========================================================

import os
from pathlib import Path

from dotenv import load_dotenv


# ==========================================================
# Load Environment Variables
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[1]

load_dotenv(BASE_DIR / ".env")


# ==========================================================
# Database Configuration
# ==========================================================

def get_database_config():
    """
    Returns the database configuration as a dictionary.
    """

    return {

        "host": os.getenv("DB_HOST"),

        "port": int(os.getenv("DB_PORT", 3306)),

        "database": os.getenv("DB_NAME"),

        "user": os.getenv("DB_USER"),

        "password": os.getenv("DB_PASSWORD"),

        "charset": os.getenv("DB_CHARSET", "utf8mb4")

    }


# ==========================================================
# Helper Functions
# ==========================================================

def get_database_url():
    """
    Returns SQLAlchemy connection URL.
    """

    config = get_database_config()

    return (

        f"mysql+mysqlconnector://"

        f"{config['user']}:{config['password']}"

        f"@{config['host']}:{config['port']}"

        f"/{config['database']}"

    )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    print(get_database_config())

    print(get_database_url())