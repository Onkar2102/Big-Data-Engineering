import yaml
import argparse
from Credit_card_Project.src.utils.utils import load_config, spark_session,get_logger_for_project
from data_ingestion import run_data_ingestion
from data_cleaning import clean_data




def main(spark, config, logger):
    logger.info('Data Ingestion started')
    application_df , credit_df  = run_data_ingestion(spark,config,logger)    
    logger.info('Data Ingestion completed')

    logger.info('Data Cleaning started')
    application_df,credit_df = clean_data(spark,config,logger,application_df,credit_df)
    logger.info('Data Cleaning completed')

    logger.info('Data Integration started')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Credit Card Default Prediction")
    parser.add_argument('--config', '-c', default='configs/config_local.yaml', help='path to yaml file with configurations')
    args = parser.parse_args()
    print(args.config)

    spark = spark_session(load_config(args.config))
    logger = get_logger_for_project()
    main(spark, load_config(args.config), logger)