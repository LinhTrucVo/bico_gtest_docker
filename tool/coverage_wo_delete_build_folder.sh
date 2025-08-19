#!/bin/bash

# Coverage script for bico-gtest-docker project
# Usage: ./coverage.sh

set -e

echo "=== Building project with coverage ==="

$(dirname "$0")/build.sh

echo ""
echo "=== Running coverage analysis ==="
cd _build
cmake --build . --target coverage

echo ""
echo -e "\e[33m=== Coverage Summary ===\e[0m"
lcov --summary coverage_filtered.info

echo ""
echo -e "\e[35m=== Generating Test Summary Report with Coverage ===\e[0m"
cd /workspaces/bico-gtest-docker
python3 -B tool/generate_test_summary.py \
    --test-results-dir "_build/output/gtest" \
    --coverage-report "_build/coverage/index.html" \
    --output "_build/test_summary_report.html"
    