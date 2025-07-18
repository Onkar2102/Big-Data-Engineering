import yaml
import argparse
from src.data_ingestion import run_data_ingestion
from src.data_cleaning import run_data_cleaning
from src.data_integration import run_data_integration
from src.optimization_serving import run_optimization_serving
from src.logger import logger

def main(config_path):
    """Orchestrates the full ETL pipeline"""
    logger.info("🚀 Starting the Credit Card Approval Pipeline...")

    logger.info("📥 Step 1: Data Ingestion")
    run_data_ingestion(config_path)

    logger.info("🛠️ Step 2: Data Cleaning")
    run_data_cleaning(config_path)

    logger.info("🔗 Step 3: Data Integration")
    run_data_integration(config_path)

    logger.info("🚀 Step 4: Optimization & Data Serving")
    run_optimization_serving(config_path)

    logger.info("✅ Pipeline Execution Completed Successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Credit Card Approval ETL Pipeline")
    parser.add_argument("--config", type=str, required=True, help="Path to config file (YAML)")
    args = parser.parse_args()

    main(args.config)
