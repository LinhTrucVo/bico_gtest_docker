cmake_minimum_required(VERSION 3.22.2)

project(bico_gtest_docker 
    VERSION 1.0.0
    DESCRIPTION "Calculator modules with GTest framework"
    LANGUAGES C CXX
)

# Set C standard
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Set C++ standard for tests
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(REPOSITORY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/project_under_test)

# Enable testing
enable_testing()

include(GoogleTest)
# Add GTest from local installation
add_subdirectory(/workspaces/googletest ${CMAKE_BINARY_DIR}/googletest)
add_subdirectory(/workspaces/fff ${CMAKE_BINARY_DIR}/fff)
include_directories(/workspaces/googletest/googletest/include)
include_directories(/workspaces/googletest/googlemock/include)
include_directories(/workspaces/fff)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/project_under_test/build_environment/gtest)

add_compile_options(-Dmemcpy_s\(a,b,c,d\)=memcpy\(a,c,d\))
add_compile_options(-Dmemset_s\(a,b,c,d\)=memset\(a,c,d\))

# specifies libraries that should be linked to all targets defined after this command
link_libraries(GTest::gtest GTest::gtest_main GTest::gmock GTest::gmock_main)

# Set output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# Debug configuration
set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS_DEBUG "-g -O0 -DDEBUG")
set(CMAKE_C_FLAGS_DEBUG "-g -O0 -DDEBUG")

# Coverage configuration
option(ENABLE_COVERAGE "Enable code coverage" OFF)

if(ENABLE_COVERAGE)
    # Add coverage compiler flags for branch coverage
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --coverage -g -O0 -DDEBUG -fprofile-arcs -ftest-coverage -fno-inline -fno-inline-small-functions -fno-default-inline")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --coverage -g -O0 -DDEBUG -fprofile-arcs -ftest-coverage -fno-inline -fno-inline-small-functions -fno-default-inline")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} --coverage -lgcov")
    
    # Find required programs
    find_program(LCOV_PATH lcov)
    find_program(GENHTML_PATH genhtml)
    
    if(NOT LCOV_PATH)
        message(FATAL_ERROR "lcov not found! Install with: apt-get install lcov")
    endif()
    
    if(NOT GENHTML_PATH)
        message(FATAL_ERROR "genhtml not found! Install with: apt-get install lcov")
    endif()
    
    # Create coverage target
    add_custom_target(coverage
        # Cleanup lcov
        COMMAND ${LCOV_PATH} --directory . --zerocounters --rc lcov_branch_coverage=1
        
        # Run tests
        COMMAND ${CMAKE_CTEST_COMMAND} --verbose --output-on-failure || true
        
        # Capture lcov counters and generate report with branch coverage
        COMMAND ${LCOV_PATH} --directory . --capture --output-file coverage.info --rc lcov_branch_coverage=1
        
        # Remove external files from coverage
        COMMAND ${LCOV_PATH} --remove coverage.info '/usr/*' '/workspaces/googletest/*' '*/test/*' --output-file coverage_filtered.info --rc lcov_branch_coverage=1
        
        # Generate HTML report with full paths and branch coverage
        COMMAND ${GENHTML_PATH} coverage_filtered.info --prefix ${CMAKE_BINARY_DIR} --output-directory coverage --config-file ${CMAKE_SOURCE_DIR}/tool/.lcovrc --rc genhtml_branch_coverage=1
        
        # Show summary with branch coverage
        COMMAND ${LCOV_PATH} --summary coverage_filtered.info --rc lcov_branch_coverage=1
        
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
        COMMENT "Generating code coverage report with branch coverage"
    )
    
    # Make sure tests are built before coverage
    # add_dependencies(coverage test_simple_calculator test_programmer_calculator)
endif()

# Add subdirectories
add_subdirectory(project_under_test/6_ut)