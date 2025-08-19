cmake_minimum_required(VERSION 3.22.2)

# Definition of test case executable and its dependencies
add_executable(test_simple_calculator
    ${CMAKE_CURRENT_SOURCE_DIR}/test_simple_calculator.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/mock/mock_simple_calculator.c
)

target_include_directories(test_simple_calculator
    PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/mock
    ${CMAKE_CURRENT_SOURCE_DIR}/../../inc
    ${CMAKE_CURRENT_SOURCE_DIR}/../../src  
    ${CMAKE_CURRENT_SOURCE_DIR}/../../config
)

# # Link with Google Test and FFF
# target_link_libraries(test_simple_calculator
#     gtest
#     gtest_main
#     gmock
#     gmock_main
# )

# Possibility to add preprocessor definitions and compiler options for the test case
target_compile_definitions(test_simple_calculator PRIVATE GTESTING)
# target_compile_options(test_simple_calculator PRIVATE)

# Make the test case discoverable by gtest
# the --gtest_shuffle causes the random of the order in which tests are executed
gtest_discover_tests(test_simple_calculator
    EXTRA_ARGS --gtest_shuffle
    XML_OUTPUT_DIR ${CMAKE_BINARY_DIR}/output/gtest)