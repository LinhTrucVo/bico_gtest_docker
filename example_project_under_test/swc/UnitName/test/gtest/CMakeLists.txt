cmake_minimum_required(VERSION 3.22.1)

add_executable(test_UnitName
    "./test_UnitName.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/mock/mock_UnitName.c"
)

target_include_directories(test_UnitName
        PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/../../../lib
        ${CMAKE_CURRENT_SOURCE_DIR}/../../inc
        ${CMAKE_CURRENT_SOURCE_DIR}/../../src
        ${CMAKE_CURRENT_SOURCE_DIR}/mock
)

# Make the test case aware
gtest_discover_tests(test_UnitName
                    EXTRA_ARGS --gtest_shuffle
                    XML_OUTPUT_DIR ${CMAKE_BINARY_DIR}/output/gtest)
