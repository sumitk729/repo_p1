FROM python:3.11-slim

# Installing System dependencies
RUN apt-get update && \
    apt-get install -y git make && \
    rm -rf /var/lib/apt/lists/*

# upgrade pip permanently
RUN python -m pip install --upgrade pip



WORKDIR /workspace


# Installing python dependencies
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

# Copy project
COPY . .
