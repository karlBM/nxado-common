FROM python:3.8-slim

# Install dependencies needed for venv
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Create your virtual environment (if you need one)
RUN python3 -m venv /opt/venv


# Install required Python packages
RUN pip3 install -r requirements.txt

# Copy your application code into the image
COPY main.py /app/main.py
COPY nxado/* /app/nxado/
COPY requirements.txt /app/requirements.txt

# Set working directory
WORKDIR /app

# Optional: Set environment variables
ENV PYSPARK_PYTHON=python3

# Command to run your script (adjust as needed)
CMD ["python3", "main.py"]
