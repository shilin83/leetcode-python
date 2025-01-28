#!/usr/bin/env bash

set -e

if ! command -v pytest >/dev/null 2>&1; then
    pip install -r requirements.txt
fi

pytest --cov=src --cov-report=html --cov-config=.coveragerc

open ./htmlcov/index.html
