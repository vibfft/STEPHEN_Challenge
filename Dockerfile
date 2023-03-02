# Use an official Python runtime as a parent image
FROM python:3.10.6
USER root 
ENV SVC_USER svc_user
ENV GROUP_ID 100
ENV USER_ID 3333   
# Set the working directory to /app
WORKDIR /app
RUN mkdir templates

# Copy the current directory contents into the container at /app
COPY templates/index.html /app/templates
COPY README.md /app
COPY hello_world.py /app
COPY requirements.txt /app

RUN useradd -m -u ${USER_ID} -g ${GROUP_ID} ${SVC_USER}

# Make port 80 and 443 available to the world outside this container
EXPOSE 80
EXPOSE 443

# Define environment variables
ENV FLASK_APP=hello_world.py
ENV FLASK_RUN_HOST=127.0.0.1
ENV FLASK_RUN_PORT=80

USER ${SVC_USER}
RUN pip3 install -r requirements.txt
# Run hello_world.py when the container launches
CMD ["python3","-m","flask", "run", "--port", "80"]