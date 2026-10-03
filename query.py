import sqlite3
import pandas as pd
from config import DB_NAME, TABLE_NAME

conn = sqlite3.connect(DB_NAME)

# how many total rows do we have?
total = pd.read_sql(f"SELECT COUNT(*) as total_rows FROM {TABLE_NAME}", conn)
print("Total rows:", total["total_rows"][0])

# latest prices
latest = pd.read_sql(f"""
    SELECT name, symbol, price_usd, percent_change_24h, extracted_at
    FROM {TABLE_NAME}
    ORDER BY extracted_at DESC
    LIMIT 10
""", conn)
print("\nLatest prices:")
print(latest)

# top 5 by market cap
top5 = pd.read_sql(f"""
    SELECT name, symbol, market_cap_usd
    FROM {TABLE_NAME}
    ORDER BY market_cap_usd DESC
    LIMIT 5
""", conn)
print("\nTop 5 by Market Cap:")
print(top5)

conn.close()