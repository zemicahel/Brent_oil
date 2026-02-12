import pandas as pd
from config import EVENT_FILE

def get_events():
    df = pd.read_csv(EVENT_FILE)
    df["Date"] = pd.to_datetime(df["Date"])

    return df.sort_values("Date").to_dict(orient="records")
