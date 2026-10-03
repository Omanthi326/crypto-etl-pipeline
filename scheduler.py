import schedule
import time
import logging
from etl import extract, transform, load

logger = logging.getLogger(__name__)

def run_pipeline():
    logger.info("=== Scheduled Run Started ===")
    try:
        raw = extract()
        clean = transform(raw)
        load(clean)
        logger.info("=== Scheduled Run Completed ===")
    except Exception as e:
        logger.critical(f"Scheduled run failed: {e}")

# run every 1 minute (for testing — we change to hourly later)
schedule.every(1).minutes.do(run_pipeline)

print("✅ Scheduler running... Press Ctrl+C to stop")
print("Pipeline will run every 1 minute")

while True:
    schedule.run_pending()
    time.sleep(1)