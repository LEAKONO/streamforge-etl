from pipeline.extract import extract_data
from pipeline.transform import transform_data
from pipeline.validate import validate_data
from pipeline.load import load_to_postgres, save_backup

def run_pipeline():
    print("Starting pipeline...")

    df = extract_data()
    df = transform_data(df)
    validate_data(df)

    load_to_postgres(df)
    save_backup(df)

    print("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
