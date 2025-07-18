import pytest
from pyspark.sql import SparkSession
from src.data_ingestion import run_data_ingestion

# fixtures are used to test the preconditions of tests. they are function decorators 

@pytest.fixture(scope="module")
def spark():
    """Create a Spark session for testing."""
    return SparkSession.builder.appName("TestSession").getOrCreate()

def test_data_ingestion(spark):
    """Test data ingestion module."""
    config_path = "configs/config_local.yaml"
    df_application, df_credit = run_data_ingestion(config_path)

    # Check if dataframes are not empty
    assert df_application.count() > 0, "Application data ingestion failed!"
    assert df_credit.count() > 0, "Credit data ingestion failed!"

    # Check for required columns
    assert "ID" in df_application.columns, "Column 'ID' missing in application data!"
    assert "STATUS" in df_credit.columns, "Column 'STATUS' missing in credit data!"
