# Use the official Python image as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Explicitly copy the app directory into the container
COPY app /app

# Copy the .env file into the container
COPY .env .env

# Expose the port the app will run on
EXPOSE 8000

# Set the PYTHONPATH environment variable to include the app directory
ENV PYTHONPATH=/app

# Command to run the application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
