import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go one level up from backend/
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# RAW DATA
PRICE_FILE = os.path.join(PROJECT_ROOT, "data", "raw", "BrentOilPrices.csv")

# EVENTS
EVENT_FILE = os.path.join(PROJECT_ROOT, "events", "oil_market_events.csv")
