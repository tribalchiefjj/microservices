# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements (if you have a requirements.txt, otherwise install Flask directly)
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose port 5000 for the service
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
