#!/bin/bash

# Coverage script for bico_gtest_docker project
# Usage: ./coverage.sh

set -e

echo "=== Building project with coverage ==="

$(dirname "$0")/build.sh

echo ""
echo "=== Running coverage analysis ==="
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BUILD_DIR="$(dirname "$SCRIPT_DIR")/_build"
cd "$BUILD_DIR"
cmake --build . --target coverage

echo ""
echo -e "\e[33m=== Coverage Summary ===\e[0m"
lcov --summary coverage_filtered.info --rc lcov_branch_coverage=1

echo ""
echo -e "\e[35m=== Generating Test Summary Report with Coverage ===\e[0m"
cd "$SCRIPT_DIR/.."
python3 -B tool/generate_test_summary.py \
    --test-results-dir "_build/output/gtest" \
    --coverage-report "_build/coverage/index.html" \
    --output "_build/test_summary_report.html"
    