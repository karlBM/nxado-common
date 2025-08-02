FROM python:3.8-slim

# Install dependencies needed for venv
RUN apt-get update && apt-get install -y --no-install-recommended \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt before installing
COPY requirements.txt /app/requirements.txt

# Now install Python packages
RUN pip3 install -r requirements.txt

# Copy application code
COPY main.py /app/main.py
COPY nxado/* /app/nxado/
# ... (any other files you need)

# Set working directory
WORKDIR /app

# Optional environment vars, etc.
ENV PYSPARK_PYTHON=python3

# Command to run your script
CMD ["python3", "main.py"]
