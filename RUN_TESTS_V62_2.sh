#!/usr/bin/env bash
set -euo pipefail
python -m py_compile planetary_restoration_model_v62_2.py test_planetary_restoration_model_v62_2.py
python planetary_restoration_model_v62_2.py --tests
