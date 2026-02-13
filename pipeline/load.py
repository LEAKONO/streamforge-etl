from sqlalchemy import create_engine
import pandas as pd
from config import DB_URI

def load_to_postgres(df: pd.DataFrame):
    engine = create_engine(DB_URI)

    df.to_sql(
        "exchange_rates",
        engine,
        if_exists="replace",
        index=False
    )

    print("Loaded to PostgreSQL")


def save_backup(df: pd.DataFrame):
    path = "data/backups/exchange_rates.parquet"
    df.to_parquet(path, index=False)
    print("Backup saved:", path)
