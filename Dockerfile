# Use official Python image
FROM python:3.12-slim

# ✅ Install system dependencies for mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config

# Set work directory
WORKDIR /app

# Copy your project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Start your Django app with Gunicorn
CMD ["gunicorn", "hireahero.wsgi:application", "--bind", "0.0.0.0:8000"]
