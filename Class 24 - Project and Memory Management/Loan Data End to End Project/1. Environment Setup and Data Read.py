import logging
from pyspark.sql import SparkSession
from google.cloud import storage
import mysql.connector

# ==============================
# 1. SETUP SPARK SESSION
# ==============================

spark = SparkSession.builder \
    .appName("CreditCardApprovalPipeline") \
    .getOrCreate()

logging.info("✅ Spark session initialized.")

# ==============================
# 2. LOAD DATA FROM GOOGLE CLOUD STORAGE (GCS)
# ==============================

gcs_bucket = "dataproc-staging-us-central1-458263062208-tw36mmqt"
gcs_data_path = f"gs://{gcs_bucket}/notebooks/jupyter/Data/loan_prediction_data/application_record.csv"

# Read CSV file from GCS
application_df = spark.read.option("header", "true").option("inferSchema", "true").csv(gcs_data_path)

logging.info(f"✅ Loaded application record data from GCS: {gcs_data_path}")

# ==============================
# 3. LOAD DATA FROM MYSQL DATABASE
# ==============================

mysql_config = {
    "host": "34.46.229.160",
    "user": "root",
    "password": "b)p[/&GH-o|B]6u+",
    "database": "loan_data",
    "table": "credit_record"
}

# Read data from MySQL
jdbc_url = f"jdbc:mysql://{mysql_config['host']}/{mysql_config['database']}?user={mysql_config['user']}&password={mysql_config['password']}"
credit_df = spark.read.format("jdbc").option("url", jdbc_url).option("dbtable", mysql_config["table"]).load()

logging.info("✅ Loaded credit record data from MySQL.")

# ==============================
# 4. DATA EXPLORATION
# ==============================

# Display schema
application_df.printSchema()
credit_df.printSchema()

# Show sample data
application_df.show(5)
credit_df.show(5)

# Check row counts
logging.info(f"Application Records: {application_df.count()}")
logging.info(f"Credit Records: {credit_df.count()}")

# Basic statistics
application_df.describe().show()
credit_df.describe().show()
