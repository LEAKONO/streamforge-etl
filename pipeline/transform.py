import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = df.columns.str.lower()

    df = df.drop_duplicates()
    df = df.dropna()

    df["rate"] = df["rate"].astype(float)

    return df
