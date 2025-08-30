# official Python image
FROM python:3.11-slim

# working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the application code
COPY . .

# Expose the port your Flask app uses
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]