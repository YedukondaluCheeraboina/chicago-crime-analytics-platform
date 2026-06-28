import os
from pathlib import Path

from dotenv import load_dotenv

try:
    import streamlit as st
except ImportError:
    st = None


# ----------------------------------------------------------
# Load local .env (for local development)
# ----------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")


def get_env(key, default=None):
    """
    Read configuration from Streamlit Secrets first,
    then fall back to local .env.
    """

    if st is not None:
        try:
            if key in st.secrets:
                return st.secrets[key]
        except Exception:
            pass

    return os.getenv(key, default)


def get_database_config():

    return {
        "host": get_env("DB_HOST"),
        "port": int(get_env("DB_PORT", 3306)),
        "database": get_env("DB_NAME"),
        "user": get_env("DB_USER"),
        "password": get_env("DB_PASSWORD"),
        "charset": get_env("DB_CHARSET", "utf8mb4")
    }


def get_database_url():

    config = get_database_config()

    return (
        f"mysql+mysqlconnector://"
        f"{config['user']}:{config['password']}"
        f"@{config['host']}:{config['port']}"
        f"/{config['database']}"
    )