# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files to the container
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-root

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 5000 for the app
EXPOSE 5000

# Run the application
CMD ["poetry", "run", "uvicorn", "punkapi.app:app", "--host", "0.0.0.0", "--port", "5000"]