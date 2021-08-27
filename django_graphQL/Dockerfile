# pull the official base image
FROM python:3.9.5

# set work directory
WORKDIR /django

# set environment variables
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . ./
