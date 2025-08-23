#!/bin/bash

set -e

cover="coverage"

if ! command -v uv &>/dev/null; then
    brew install uv
fi

if [ ! -f uv.lock ]; then
    uv sync
fi

if [ -n "$1" ]; then
    if [ "$1" = "$cover" ]; then
        uv run pytest --cov --cov-report=html --cov-config=.coveragerc
        open ./htmlcov/index.html
    else
        printf "Invalid argument: %s\nUsage: /bin/bash test.sh %s\n" "$1" "$cover"
    fi
else
    uv run pytest
fi
