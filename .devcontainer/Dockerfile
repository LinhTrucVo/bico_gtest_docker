FROM ghcr.io/linhtrucvo/bico_gtest_docker:22.04_0.0.0

# Copy and set up entrypoint script (relative to .devcontainer/)
COPY entrypoint.sh /entrypoint.sh
RUN sudo chmod +x /entrypoint.sh
COPY postCreateCommand.sh /postCreateCommand.sh
RUN sudo chmod +x /postCreateCommand.sh

# Set the entry point for the container
CMD ["bash"]
