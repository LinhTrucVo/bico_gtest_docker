FROM ghcr.io/volinhtruc/bico_ubuntu:22.04_0.0.0

LABEL name="bico-gtest"
LABEL version="0.0.0"
LABEL description="Gtest development environment with CMake, GTest, FFF and Code Coverage"
LABEL maintainer="bico"
LABEL org.opencontainers.image.title=name
LABEL org.opencontainers.image.version=version
LABEL org.opencontainers.image.description=description

USER root

RUN apt-get update
RUN apt-get install -y lcov

# Create a directory for the project
WORKDIR /workspaces
 
RUN git clone --branch v1.17.0 --depth 1 https://github.com/google/googletest.git /workspaces/googletest
RUN git clone https://github.com/meekrosoft/fff.git /workspaces/fff \
    && cd fff && git checkout 5111c61e1ef7848e3afd3550044a8cf4405f4199 && cd ..

# CMake 3.22.2 installation
RUN wget -P /workspaces/cmake_3.22.2 https://github.com/Kitware/CMake/releases/download/v3.22.2/cmake-3.22.2-linux-x86_64.tar.gz && \
    mkdir -p /opt/cmake && \
    tar -zxvf /workspaces/cmake_3.22.2/cmake-3.22.2-linux-x86_64.tar.gz -C /opt/cmake && \
    ln -s /opt/cmake/cmake-3.22.2-linux-x86_64/bin/cmake /usr/local/bin/cmake
 
USER developer

# Copy and set up entrypoint script (relative to .devcontainer/)
COPY entrypoint.sh /entrypoint.sh
RUN sudo chmod +x /entrypoint.sh
COPY postCreateCommand.sh /postCreateCommand.sh
RUN sudo chmod +x /postCreateCommand.sh

# Set the entry point for the container
CMD ["bash"]
