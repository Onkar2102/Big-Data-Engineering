import yaml  # ✅ Ensure YAML is imported
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from src.logger import logger
from src.data_integration import run_data_integration

# ==============================
# 1. LOAD CONFIGURATION
# ==============================

def load_config(config_path):
    """Loads configuration from a YAML file."""
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

# ==============================
# 2. SETUP SPARK SESSION
# ==============================

def get_spark_session(config):
    """Initializes and returns a Spark session."""
    spark = SparkSession.builder \
        .appName("CreditCardApproval_Optimization_Serving") \
        .config("spark.sql.shuffle.partitions", config["spark"]["shuffle_partitions"]) \
        .config("spark.executor.memory", config["spark"]["executor_memory"]) \
        .config("spark.executor.cores", config["spark"]["executor_cores"]) \
        .config("spark.sql.adaptive.enabled", "true") \
        .getOrCreate()

    logger.info("✅ Spark session initialized successfully.")
    return spark

# ==============================
# 3. DATA OPTIMIZATION
# ==============================

def optimize_data(df):
    """Optimizes data processing performance."""
    logger.info("🚀 Optimizing Data Processing...")

    # Cache dataset for improved performance
    df.cache()

    # Repartition to balance processing load
    df = df.repartition(10, "ID")

    # Predicate Pushdown: Filter unnecessary records
    df = df.filter(col("AMT_INCOME_TOTAL") > 10000)

    logger.info("✅ Optimization Completed.")
    return df

# ==============================
# 4. SAVE FINAL DATA TO GCS OR LOCAL
# ==============================

def save_data(df, config):
    """Saves processed data to GCS (Dataproc) or local storage."""
    logger.info("💾 Saving Optimized Data...")

    save_path = config["save_path"]

    if config["env"] == "local":
        output_path = os.path.join(save_path, "final_data")
        df.write.mode("overwrite").csv(output_path)
    else:
        output_path = f"{save_path}/final_data.parquet"
        df.write.mode("overwrite").parquet(output_path)

    logger.info(f"✅ Data Saved Successfully at {output_path}")

# ==============================
# 5. MAIN EXECUTION FUNCTION
# ==============================

def run_optimization_serving(config_path):
    """Executes optimization & final data serving."""
    config = load_config(config_path)
    spark = get_spark_session(config)

    # Load integrated data
    logger.info("📥 Loading Integrated Data...")
    df_final = run_data_integration(config_path)

    # Apply optimizations
    df_final = optimize_data(df_final)

    # Save final processed data
    save_data(df_final, config)
