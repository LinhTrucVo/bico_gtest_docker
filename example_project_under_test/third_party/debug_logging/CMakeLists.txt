cmake_minimum_required(VERSION 3.22.2)

# Debug Logging Library - Using pre-built static library
# Create an interface library to wrap the pre-built .a file
add_library(debug_logging INTERFACE)

# Link the pre-built library
target_link_libraries(debug_logging INTERFACE
    ${CMAKE_CURRENT_SOURCE_DIR}/src/libdebug_logging.a
)

# Export the include directory
target_include_directories(debug_logging INTERFACE
    inc
)
