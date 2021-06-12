# Base Image
FROM python:3.8.0-buster as base

# Current Directory Definition
WORKDIR /home/python/app

# Move Contents To Directory
COPY . ./

# Install Dependencies
RUN pip install --upgrade pip
RUN pip3 install --no-cache -r requirements.txt

COPY . .