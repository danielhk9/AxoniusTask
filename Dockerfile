# Dockerfile
FROM mcr.microsoft.com/playwright/python:v1.52.0-jammy

WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Ensure test script is executable
RUN chmod +x run_tests.sh

ENTRYPOINT ["./run_tests.sh"]
