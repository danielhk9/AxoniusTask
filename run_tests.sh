#!/bin/bash
set -e

echo "Running Playwright tests with args: $@"
pytest e2e_tests/tests "$@"