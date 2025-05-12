#!/bin/bash
set -e

echo "Running Playwright tests..."
pytest e2e_tests/tests "$@"
