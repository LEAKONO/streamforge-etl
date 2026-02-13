from sqlalchemy import create_engine
import pandas as pd
import os
from config import DB_URI

def load_to_postgres(df: pd.DataFrame):
    engine = create_engine(DB_URI)
    df.to_sql(
        "exchange_rates",
        engine,
        if_exists="replace",  # or 'append' if you want historical data
        index=False
    )
    print("Loaded to PostgreSQL")

def save_backup(df: pd.DataFrame):
    os.makedirs("data/backups", exist_ok=True) 
    path = "data/backups/exchange_rates.parquet"
    df.to_parquet(path, index=False)
    print("Backup saved:", path)