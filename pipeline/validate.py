import pandas as pd

def validate_data(df: pd.DataFrame):
    if df.empty:
        raise ValueError("Dataset is empty")

    if df["rate"].lt(0).any():
        raise ValueError("Negative exchange rate detected")

    if df.duplicated().any():
        raise ValueError("Duplicate rows detected")

    print("Validation passed")
