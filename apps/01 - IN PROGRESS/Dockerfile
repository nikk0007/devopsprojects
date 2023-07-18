# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file
COPY ./python-app/requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files to the container
COPY ./python-app/ .

# Expose the port the app runs on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
