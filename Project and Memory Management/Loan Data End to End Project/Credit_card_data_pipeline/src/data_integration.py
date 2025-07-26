from src.logger import logger
from src.data_cleaning import run_data_cleaning

def integrate_data(df_application, df_credit):
    """Joins the application & credit datasets."""
    logger.info("🔗 Integrating Data...")

    df_final = df_application.join(df_credit, on='ID', how='inner')

    logger.info("✅ Data Integration Completed.")
    return df_final

def run_data_integration(config_path):
    """Executes data integration pipeline."""
    df_application, df_credit = run_data_cleaning(config_path)
    df_final = integrate_data(df_application, df_credit)

    return df_final
