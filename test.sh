#!/bin/bash

set -e

if ! command -v pytest /dev/null 2>&1; then
    pip install pytest pytest-cov
fi

pytest --cov=src --cov-report=html

if [ -d htmlcov ]; then
    open htmlcov/index.html
fi
