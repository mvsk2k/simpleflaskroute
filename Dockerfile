# Use a Python 3.10 base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY app.py .

# Copy the templates folder to the container
COPY templates ./templates

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set the entry point to run the Flask app
CMD ["python", "app.py"]
