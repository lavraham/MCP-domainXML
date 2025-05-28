FROM fedora:latest

WORKDIR /app

# Install the libvirt-client package
USER root
RUN sudo dnf update -y && \
    dnf install -y libvirt-client virt-install python3 python3-pip


COPY requirements.txt ./

RUN pip install --user fastmcp
RUN pip install --user --no-cache-dir -r requirements.txt


COPY mcp_server.py ./

ENTRYPOINT ["python3", "/app/mcp_server.py"]