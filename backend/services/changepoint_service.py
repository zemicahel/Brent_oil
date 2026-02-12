import pandas as pd
import numpy as np
from config import PRICE_FILE

def compute_change_point():
    df = pd.read_csv(PRICE_FILE)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    prices = df["Price"].values
    n = len(prices)

    best_tau = None
    best_score = -np.inf

    # Evaluate possible split points
    for tau in range(30, n - 30):
        mean1 = prices[:tau].mean()
        mean2 = prices[tau:].mean()

        # Likelihood score (sum of squared residuals)
        sse1 = np.sum((prices[:tau] - mean1) ** 2)
        sse2 = np.sum((prices[tau:] - mean2) ** 2)

        score = -(sse1 + sse2)

        if score > best_score:
            best_score = score
            best_tau = tau

    change_date = df.iloc[best_tau]["Date"]
    mean_before = prices[:best_tau].mean()
    mean_after = prices[best_tau:].mean()
    percent_change = ((mean_after - mean_before) / mean_before) * 100

    return {
        "change_point_date": str(change_date.date()),
        "mean_before": round(float(mean_before), 2),
        "mean_after": round(float(mean_after), 2),
        "percent_change": round(float(percent_change), 2)
    }
