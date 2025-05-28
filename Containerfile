FROM fedora:latest
WORKDIR /app
RUN useradd -m appuser
# Install the libvirt-client package
USER root
RUN dnf install -y libvirt-client virt-install python3 python3-pip awk
USER appuser
COPY requirements.txt ./
RUN pip install --user --no-cache-dir -r requirements.txt
COPY mcp_server.py ./
CMD ["python", "mcp_server.py"]