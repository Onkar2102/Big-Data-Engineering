
import yaml
from src.logger import get_logger
from Credit_card_Project.src.utils.utils import load_config, spark_session,get_logger_for_project

from pyspark.sql.functions import trim, col, upper, lower, round
from Credit_card_Project.src.utils.dataset_utils import drop_na



def application_df_cleaning(application_df):
    application_df = drop_na(how="all")
    application_df = application_df.fillna({"OCCUPATION_TYPE": "Unknown"})
    application_df = application_df.select([trim(col(c)).alias(c) for c in application_df.columns])
    # Standardize categorical values
    application_df = application_df.withColumn("CODE_GENDER", upper(col("CODE_GENDER")))
    application_df = application_df.withColumn("NAME_FAMILY_STATUS", lower(col("NAME_FAMILY_STATUS")))

    # Convert amount fields to float & round to 2 decimals
    application_df = application_df.withColumn("AMT_INCOME_TOTAL", round(col("AMT_INCOME_TOTAL"), 2))
    # Age in years
    application_df = application_df.withColumn("AGE", round(col("DAYS_BIRTH") / 365, 0))

    # Employment length in years
    application_df = application_df.withColumn("EMPLOYMENT_YEARS", round(col("DAYS_EMPLOYED") / 365, 0))





def clean_data(spark,config,logger,application_df,credit_df):
    logger.info('Cleaning application data')
    application_df = application_df_cleaning(application_df)
    logger.info('Cleaning credit data')
    return application_df,credit_df

    

if __name__ == '__main__':
    local_config = 'configs/config_local.yaml'
    
    config = load_config(local_config)
    logger = get_logger_for_project()
    spark = spark_session(config,logger)
    run_data_ingestion(spark, config, logger)