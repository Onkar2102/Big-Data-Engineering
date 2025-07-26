import pytest

from data_ingestion import run_data_ingestion
from utils.utils import load_config, spark_session, get_logger_for_project
from pyspark.sql import SparkSession

@pytest.fixture(scope='module')
def get_spark():
    print("Setting up Spark  session")
    config = load_config('tests/config_local.yaml')
    logger = get_logger_for_project()
    spark = spark_session(config, logger)
    print("Spark session created")

    return spark, config, logger

def test_data_ingestion(get_spark):
    print("Testing data")
    # spark, config, logger = get_spark()
    config = load_config('tests/config_local.yaml')
    print(config)
    spark = SparkSession.builder.getOrCreate()
    application, credit = run_data_ingestion(spark, config, get_logger_for_project())
    assert(application.count() == 438553)
    assert(application.columns == ['SK_ID_CURR', 'TARGET', 'NAME_CONTRACT_TYPE'])

    spark.stop()
