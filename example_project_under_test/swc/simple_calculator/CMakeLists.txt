cmake_minimum_required(VERSION 3.22.2)

# Simple Calculator Library
add_library(simple_calculator STATIC
    src/simple_calculator.c
)

target_include_directories(simple_calculator PUBLIC
    inc
    config
)

target_link_libraries(simple_calculator PUBLIC
    calculation_check
    debug_logging
)

# Add tests subdirectory
add_subdirectory(test/gtest)
