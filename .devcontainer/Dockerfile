FROM ubuntu:22.04

LABEL name="bico-gtest"
LABEL version="1.0.0"
LABEL description="Gtest development environment with CMake, GTest, FFF and Code Coverage"
LABEL maintainer="bico"
LABEL org.opencontainers.image.title=name
LABEL org.opencontainers.image.version=version
LABEL org.opencontainers.image.description=description

ENV MY_PROXY_IP=rb-proxy-apac.bosch.com
ENV MY_PROXY_PORT=8080
ENV MY_PROXY_USER_NAME=vor5hc
ENV MY_PROXY_PASSWORD=%40Bico3852201

ENV DEBIAN_FRONTEND=noninteractive
ENV http_proxy=http://$MY_PROXY_IP:$MY_PROXY_PORT
ENV https_proxy=http://$MY_PROXY_IP:$MY_PROXY_PORT
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8
    
# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    wget \
    lcov \
    # Ubuntu 22.04 install CMake 3.22.1 by default, but we need 3.22.2, the 3.22.2 installation is done later
    # cmake \
    git \
    curl \
    python-is-python3 \
    python3-pip \
    python3-dev \
    vim \
    nano \
    g++-17 \
    gdb \
    tzdata

# g++-17 installation cannot be done by below command, it is done later
# RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-17 90
 
# Clean up apt cache to reduce image size
# RUN apt-get clean && \
    # rm -rf /var/lib/apt/lists/*

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

# Set the entry point for the container
CMD ["bash"]