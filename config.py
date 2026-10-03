# config.py
API_URL = "https://api.coinlore.net/api/tickers/?limit=20"
DB_NAME = "crypto.db"
TABLE_NAME = "crypto_prices"
COLUMNS = ["id", "name", "symbol", "price_usd", "percent_change_24h", "market_cap_usd"]