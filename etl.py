import requests
import pandas as pd
import sqlite3
import logging
from datetime import datetime
from config import API_URL, DB_NAME, TABLE_NAME, COLUMNS
# --- LOGGING SETUP ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("etl.log"),  # saves log to file
        logging.StreamHandler()           # also prints to terminal
    ]
)
logger = logging.getLogger(__name__)

# --- EXTRACT ---
def extract():
    try:
        
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()  # catches HTTP errors
        data = response.json()["data"]
        logger.info(f"Extracted {len(data)} records from API")
        return data
    except requests.exceptions.Timeout:
        logger.error("API request timed out")
        raise
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        raise

# --- TRANSFORM ---
def transform(data):
    try:
        df = pd.DataFrame(data)
        df = df[COLUMNS]
        df["price_usd"] = pd.to_numeric(df["price_usd"])
        df["percent_change_24h"] = pd.to_numeric(df["percent_change_24h"])
        df["market_cap_usd"] = pd.to_numeric(df["market_cap_usd"])
        df["extracted_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # data quality check
        assert df["price_usd"].notna().all(), "Missing price values!"
        assert len(df) > 0, "Empty dataframe!"

        logger.info(f"Transformed {len(df)} rows successfully")
        return df
    except AssertionError as e:
        logger.error(f"Data quality check failed: {e}")
        raise
    except Exception as e:
        logger.error(f"Transform failed: {e}")
        raise

# --- LOAD ---
def load(df):
    try:
        conn = sqlite3.connect(DB_NAME)
        df.to_sql(TABLE_NAME, conn, if_exists="append", index=False)
        conn.close()
        logger.info("Loaded data to SQLite — crypto.db")
    except Exception as e:
        logger.error(f"Load failed: {e}")
        raise

# --- RUN ---
if __name__ == "__main__":
    logger.info("=== ETL Pipeline Started ===")
    try:
        raw = extract()
        clean = transform(raw)
        load(clean)
        logger.info("=== ETL Pipeline Completed Successfully ===")
    except Exception as e:
        logger.critical(f"Pipeline failed: {e}")