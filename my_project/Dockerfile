FROM python:3.8

# Install system dependencies
RUN apt-get update && apt-get install -y libcairo2-dev libjpeg-dev libgif-dev pkg-config python3-apt

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install additional dependencies
RUN apt-get install -y python3-apt

# Copy and install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Install daphne
RUN pip install daphne

# Copy the rest of the application code
COPY . /app/

# Expose the port
EXPOSE 8000

# Command to run the application using daphne
CMD ["daphne", "my_project.asgi:application", "--bind", "0.0.0.0", "--port", "8000"]
