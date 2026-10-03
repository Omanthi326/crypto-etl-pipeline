
---

## Tech Stack

- **Python 3.11**
- **pandas** — data transformation
- **requests** — API calls
- **sqlite3** — database storage
- **schedule** — automated scheduling
- **logging** — production-style logging

---

## How to Run

### 1. Install dependencies
```bash
pip install requests pandas schedule
```

### 2. Run pipeline once
```bash
python etl.py
```

### 3. Run on auto-schedule (every hour)
```bash
python scheduler.py
```

### 4. Query the database
```bash
python query.py
```

---

## What I Learned

- Building a production-style ETL pipeline from scratch
- API integration with error handling and timeouts
- Data transformation and quality checks with pandas
- Storing and querying time series data with SQLite
- Professional logging (INFO / ERROR / CRITICAL levels)
- Config management — separating settings from logic
- Automated scheduling without external tools

---

