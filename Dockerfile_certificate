# Use an official Python runtime as a parent image
FROM python:3.10.6
USER root 
ENV SVC_USER svc_user
ENV GROUP_ID 100
ENV USER_ID 3333   
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN useradd -m -u ${USER_ID} -g ${GROUP_ID} ${SVC_USER}
USER ${SVC_USER}

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

USER root

# Make port 80 and 443 available to the world outside this container
EXPOSE 80
EXPOSE 443

# Copy the SSL certificate and key files into the container
# COPY ssl/server.crt ssl/server.crt
# COPY ssl/server.key ssl/server.key
RUN chmod 644 ssl/server.crt && chmod 644 ssl/server.key

# Define environment variables
ENV FLASK_APP=hello_world.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80

# Enable HTTPS redirection using flask-talisman
ENV TALISMAN_FORCE_HTTPS=True

USER ${SVC_USER}
# Run hello_world.py when the container launches
CMD ["python3","-m","flask", "run", "--port", "80", "--cert", "ssl/server.crt", "--key", "ssl/server.key"]