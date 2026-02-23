#!/bin/bash

# Coverage script for bico_gtest_docker project
# Usage: ./coverage.sh

set -e

$(dirname "$0")/remove_build_but_googletest_and_fff.sh
$(dirname "$0")/coverage_wo_delete_build_folder.sh
