import pytest
from src.data_integration import run_data_integration

def test_data_integration():
    """Test data integration module."""
    config_path = "configs/config_local.yaml"
    df_final = run_data_integration(config_path)

    # Check if integrated data is not empty
    assert df_final.count() > 0, "Data integration failed!"
