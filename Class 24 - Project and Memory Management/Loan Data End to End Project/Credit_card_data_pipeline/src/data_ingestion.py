import yaml
from pyspark.sql import SparkSession
from src.logger import loggerdata

def load_config(config_path):
    """Loads configuration from a YAML file."""
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def get_spark_session(config):
    """Initializes and returns a Spark session."""
    spark = SparkSession.builder \
        .appName("CreditCardApproval_Ingestion") \
        .config("spark.sql.shuffle.partitions", config["spark"]["shuffle_partitions"]) \
        .config("spark.executor.memory", config["spark"]["executor_memory"]) \
        .config("spark.executor.cores", config["spark"]["executor_cores"]) \
        .getOrCreate()
    
    logger.info("✅ Spark session initialized successfully.")
    return spark

def run_data_ingestion(config_path):
    """Executes data ingestion."""
    config = load_config(config_path)
    spark = get_spark_session(config)

    logger.info("📥 Loading data...")
    if config["env"] == "local":
        df_application = spark.read.option("header", "true").csv(config["data_path"])
        df_credit = spark.read.option("header", "true").csv(config["credit_data_path"])
    else:
        df_application = spark.read.parquet(config["data_path"])
        df_credit = spark.read.parquet(config["credit_data_path"])

    logger.info("✅ Data Ingestion Completed.")
    return df_application, df_credit
