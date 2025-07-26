#!/bin/bash

# Activate Virtual Environment (if used)
#source credit_card_env/bin/activate

# Set PYTHONPATH so that src/ is recognized
export PYTHONPATH=$(pwd)

# Run the pipeline locally
python src/main.py --config configs/config_local.yaml
