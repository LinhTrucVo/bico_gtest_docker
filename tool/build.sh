cd /workspaces/bico_gtest_docker

cmake -B _build -S . -DENABLE_COVERAGE=ON
cmake --build _build