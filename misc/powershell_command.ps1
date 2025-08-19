# Run the container before executing this file.
# Hint: if the container is not yet created, you can use .devcontainer to create the container.
docker exec -w /workspaces/bico-gtest-docker -it bico-gtest-container bash -c "./tool/coverage.sh"