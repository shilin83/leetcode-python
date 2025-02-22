#!/usr/bin/env bash

set -e

if ! command -v uv >/dev/null 2>&1; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    uv add pytest pytest-cov
fi

uv run pytest --cov --cov-report=html --cov-config=.coveragerc

open ./htmlcov/index.html
