# Run tests
./calculator_tests

# Generate coverage data
lcov --directory . --capture --output-file coverage.info

# Filter out system files and test files
lcov --remove coverage.info '/usr/*' '*/googletest/*' '*/tests/*' --output-file coverage.info.cleaned

# Generate HTML report
genhtml -o coverage_html coverage.info.cleaned
genhtml -o coverage_html coverage.info