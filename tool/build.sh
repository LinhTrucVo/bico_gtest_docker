cd /workspaces/bico-gtest-docker

cmake -B _build -S . -DENABLE_COVERAGE=ON
cmake --build _build