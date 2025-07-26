
import yaml
from src.logger import get_logger
from src.utils.utils import load_config, spark_session,get_logger_for_project

from pyspark.sql.functions import trim, col, upper, lower, round


def run_data_ingestion(spark,config,logger):
    if(config['env']=='local'):
        print("Data Ingestion started",config)
        application = spark.read.csv(config['data_path'], header=True, inferSchema=True)
        credit = spark.read.csv(config['credit_data_path'], header=True, inferSchema=True)
        logger.info("Data loaded successfully")
        application = application.withColumn("CODE_GENDER_2", upper(col("CODE_GENDER")))
        print(application.show())
    return application,credit


if __name__ == '__main__':
    local_config = 'configs/config_local.yaml'
    
    config = load_config(local_config)
    logger = get_logger_for_project()
    spark = spark_session(config,logger)
    run_data_ingestion(spark, config, logger)