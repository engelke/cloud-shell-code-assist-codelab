# Use a slim Python base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port your app listens on (default is 5000)
EXPOSE 5000

# Define the command to run your app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
