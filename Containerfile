FROM fedora:latest

WORKDIR /app

# Install the libvirt-client package
USER root
RUN sudo dnf update -y && \
    dnf install -y libvirt-client virt-install python3 python3-pip

<<<<<<< HEAD

COPY requirements.txt ./

RUN pip install --user fastmcp
RUN pip install --user --no-cache-dir -r requirements.txt

=======
>>>>>>> a44c9069a8ddea94b40907e1b0e66ad346e28dce

COPY requirements.txt ./
RUN pip install --user --no-cache-dir -r requirements.txt
USER 1000

<<<<<<< HEAD
ENTRYPOINT ["python3", "/app/mcp_server.py"]
=======
COPY mcp_server.py ./
>>>>>>> a44c9069a8ddea94b40907e1b0e66ad346e28dce
