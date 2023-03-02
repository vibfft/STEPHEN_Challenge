# Use an official Python runtime as a parent image
FROM python:3.10.6
    
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 and 443 available to the world outside this container
EXPOSE 80
EXPOSE 443

# Copy the SSL certificate and key files into the container
COPY ssl/server.crt /etc/ssl/certs/server.crt
COPY ssl/server.key /etc/ssl/private/server.key

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80

# Enable HTTPS redirection using flask-talisman
ENV TALISMAN_FORCE_HTTPS=True

# Run app.py when the container launches
CMD ["flask", "run", "--port", "80", "--cert", "/etc/ssl/certs/server.crt", "--key", "/etc/ssl/private/server.key"]
