# Set base image
FROM python:3.7

MAINTAINER <belghiti.ali@gmail.com>

# Creating directory app
RUN mkdir /app

# Set working directory in the container
WORKDIR /app

# Copying project to the working directory in the container
COPY ./ .

# Command to run when container starts
ENTRYPOINT ["python", "main.py"]