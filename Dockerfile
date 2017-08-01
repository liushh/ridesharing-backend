# Use an official Python runtime as a parent image the one Bot team is using now
FROM gcr.io/google-appengine/python

MAINTAINER Liusha

ARG PROJECT_DIR=/app
ARG VENV_DIR=.venv

# Set the working directory to /app
WORKDIR ${PROJECT_DIR}

# Copy the current directory contents into the container at /app
ADD . /app

RUN virtualenv ${VENV_DIR} -p python3.6

ARG BIN_DIR=${VENV_DIR}/bin
ENV BIN_DIR=${BIN_DIR}

# Install any needed packages specified in requirements.txt
RUN ${BIN_DIR}/pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ./start-services.sh
