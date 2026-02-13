import requests
import pandas as pd
from config import API_URL

def extract_data() -> pd.DataFrame:
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()

    data = response.json()

    rates = data["rates"]
    base = data["base"]
    date = data["date"]

    df = pd.DataFrame(list(rates.items()), columns=["currency", "rate"])
    df["base_currency"] = base
    df["date"] = date

    return df
