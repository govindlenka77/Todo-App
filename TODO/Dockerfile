# Use the official Python image as the base image
FROM python:3.12.1

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file first (to leverage Docker cache)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run database migrations
RUN python manage.py migrate

# Start the Django app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "TODO.wsgi:application"]
