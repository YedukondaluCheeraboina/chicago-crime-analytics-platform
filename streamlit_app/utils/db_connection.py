"""
==========================================================
Database Connection Utility
==========================================================

Description:
Provides reusable database utilities for the
Chicago Crime Analytics Platform.

Features
--------
1. Loads credentials from .env
2. Creates reusable SQLAlchemy engine
3. Executes SQL queries
4. Returns Pandas DataFrames
5. Uses Streamlit caching

Author:
Yedukondalu Cheeraboina
"""

# ==========================================================
# Imports
# ==========================================================

import pandas as pd
import streamlit as st

from sqlalchemy import create_engine

from utils.database_config import get_database_url


# ==========================================================
# SQLAlchemy Engine
# ==========================================================

DATABASE_URL = get_database_url()

engine = create_engine(

    DATABASE_URL,

    pool_pre_ping=True,

    pool_recycle=3600,

    future=True

)


# ==========================================================
# Execute SQL Query
# ==========================================================

@st.cache_data(show_spinner=False)

def load_data(query):
    """
    Executes a SQL query and returns
    the result as a Pandas DataFrame.
    """

    return pd.read_sql(

        query,

        engine

    )


# ==========================================================
# Load Complete Crime Dataset
# ==========================================================

@st.cache_data(show_spinner=False)

def load_crime_data():
    """
    Loads the complete crime table.
    """

    query = """

        SELECT *

        FROM crime

    """

    return pd.read_sql(

        query,

        engine

    )


# ==========================================================
# Load Table Utility
# ==========================================================

@st.cache_data(show_spinner=False)

def load_table(table_name):
    """
    Loads any table from the database.
    """

    query = f"""

        SELECT *

        FROM {table_name}

    """

    return pd.read_sql(

        query,

        engine

    )


# ==========================================================
# Test Database Connection
# ==========================================================

def test_connection():
    """
    Tests database connectivity.
    """

    try:

        with engine.connect():

            return True

    except Exception:

        return False