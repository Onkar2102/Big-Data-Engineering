import pytest
from src.data_cleaning import run_data_cleaning

def test_data_cleaning():
    """Test data cleaning module."""
    config_path = "configs/config_local.yaml"
    df_application, df_credit = run_data_cleaning(config_path)

    # Ensure null values are handled
    assert df_application.dropna().count() == df_application.count(), "Null values present in application data!"
    assert df_credit.dropna().count() == df_credit.count(), "Null values present in credit data!"
