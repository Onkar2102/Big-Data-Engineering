import pytest
from src.optimization_serving import run_optimization_serving

def test_optimization_serving():
    """Test optimization and data serving module."""
    config_path = "configs/config_local.yaml"

    # Run optimization and serving
    try:
        run_optimization_serving(config_path)
        success = True
    except Exception:
        success = False

    assert success, "Optimization & data serving failed!"
