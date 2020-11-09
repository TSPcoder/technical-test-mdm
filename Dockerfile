# Set base image
FROM python:3.7

MAINTAINER <belghiti.ali@gmail.com>

# Creating directory app
RUN mkdir /app

# Set working directory in the container
WORKDIR /app

# Copying project to the working directory in the container
COPY ./ .

# Install dependencies: Flask and flask_restplus
RUN pip install -r requirements.txt

# Set environment variables
ENV STRINGS_ARRAY "ab,bc,b,h,o"
ENV FLASK_APP=main.py

# Expose port 5000 for the Swagger UI
EXPOSE 5000

# Command to run when container starts
ENTRYPOINT ["python", "main.py"]