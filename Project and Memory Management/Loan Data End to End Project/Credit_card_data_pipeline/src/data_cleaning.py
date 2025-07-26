from pyspark.sql.functions import col, when, trim
from src.logger import logger
from src.data_ingestion import run_data_ingestion

def clean_data(df_application, df_credit):
    """Performs data cleaning operations."""
    logger.info("🛠️ Cleaning Data...")

    # Standardize categorical values
    df_application = df_application.withColumn("CODE_GENDER", trim(col("CODE_GENDER")))

    # Handle missing values
    df_application = df_application.fillna({"OCCUPATION_TYPE": "Unknown"})
    df_credit = df_credit.fillna({"STATUS": "X"})

    logger.info("✅ Data Cleaning Completed.")
    return df_application, df_credit

def run_data_cleaning(config_path):
    """Executes data cleaning pipeline."""
    df_application, df_credit = run_data_ingestion(config_path)
    df_application, df_credit = clean_data(df_application, df_credit)

    return df_application, df_credit
