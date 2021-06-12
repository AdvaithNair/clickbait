# Base Image
FROM python:3.8.0-buster

# Current Directory Definition
WORKDIR /server

# Move Contents To Directory
ADD . /server

# Install Dependencies
# RUN pip3 install --pre numpy
RUN pip install --upgrade pip
RUN pip3 install --no-cache -r requirements.txt

# Start Container
CMD ["python3", "app.py"]