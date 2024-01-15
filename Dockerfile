
# Use the official Python image from DockerHub as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Specify the command to run when the container starts
CMD ["uvicorn", "modified_fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]
