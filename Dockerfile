FROM python:3.8-slim

# Install dependencies needed for venv
RUN apt-get update && apt-get install -y python3-venv && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY ./requirements.txt /app/requirements.txt

# Install Python packages
RUN pip3 install -r ./requirements.txt

# Copy app files
COPY main.py /app/main.py
COPY nxado/* /app/nxado/

WORKDIR /app
ENV PYSPARK_PYTHON=python3

CMD ["python3", "main.py"]
