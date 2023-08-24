# syntax=docker/dockerfile:1

# set base image (host OS)
From python:3.8-slim-buster

# set the working directory in the container
WORKDIR /ipypass

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy the content of the local directory to the working directory
Copy ..

CMD [ "python3 ipypass.py" ]
