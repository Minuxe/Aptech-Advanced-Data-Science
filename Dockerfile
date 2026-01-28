# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirement.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirement.txt && \
    pip install --no-cache-dir jupyter notebook jupyterlab

# Copy all project files
COPY . .

# Expose Jupyter port
EXPOSE 8888

# Create a startup script
RUN echo '#!/bin/bash\njupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root' > /app/start.sh && \
    chmod +x /app/start.sh

# Set the default command to start Jupyter
CMD ["/app/start.sh"]
