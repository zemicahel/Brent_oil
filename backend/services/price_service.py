import pandas as pd
from config import PRICE_FILE

def get_prices(start_date=None, end_date=None):
    df = pd.read_csv(PRICE_FILE)
    df["Date"] = pd.to_datetime(df["Date"])

    if start_date:
        df = df[df["Date"] >= start_date]
    if end_date:
        df = df[df["Date"] <= end_date]

    return df.sort_values("Date").to_dict(orient="records")
