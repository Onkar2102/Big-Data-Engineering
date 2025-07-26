from pyspark.sql import SparkSession
from logger import get_logger
import yaml

def load_config(config_path):
    with open(config_path) as file:
        config = yaml.safe_load(file)
        print(config)
    return config


def spark_session(config,logger):
    spark = SparkSession.builder \
        .appName(config['spark']['app_name']) \
        .config('shuffle.partitions', config['spark']['shuffle_partitions']) \
        .getOrCreate()
    logger.info('Spark session created')
    return spark

def get_logger_for_project():
    return get_logger()
