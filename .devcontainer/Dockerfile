FROM ghcr.io/linhtrucvo/bico_gtest_docker:22.04_0.0.0

ENV MY_PROXY_IP=10.195.223.48
ENV MY_PROXY_PORT=3128
ENV HTTP_PROXY=http://$MY_PROXY_IP:$MY_PROXY_PORT
ENV HTTPS_PROXY=http://$MY_PROXY_IP:$MY_PROXY_PORT
ENV http_proxy=http://$MY_PROXY_IP:$MY_PROXY_PORT
ENV https_proxy=http://$MY_PROXY_IP:$MY_PROXY_PORT
ENV NO_PROXY="localhost,127.0.0.1,::1,*.local"
ENV no_proxy="$NO_PROXY"

# Copy and set up entrypoint script (relative to .devcontainer/)
COPY entrypoint.sh /entrypoint.sh
RUN sudo chmod +x /entrypoint.sh
COPY postCreateCommand.sh /postCreateCommand.sh
RUN sudo chmod +x /postCreateCommand.sh

# Set the entry point for the container
CMD ["bash"]
