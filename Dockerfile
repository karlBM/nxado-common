# Use an official Spark base image
FROM apache/spark:3.4.0

# Install Python and dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set python3 as default
RUN ln -sf /usr/bin/python3 /usr/bin/python
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY ./config /tmp
COPY ./requirements.txt /tmp/requirements.txt
RUN chmod +x /tmp/build.sh
RUN ["/bin/bash", "-c", "source /tmp/build.sh"]


# Install required Python packages
RUN pip3 install -r requirements.txt

# Copy your application code into the image
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

# Set working directory
WORKDIR /app

# Optional: Set environment variables
ENV PYSPARK_PYTHON=python3

# Command to run your script (adjust as needed)
CMD ["python3", "main.py"]
