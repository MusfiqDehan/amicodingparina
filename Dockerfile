# Official Python runtime
FROM python:3.10

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /codes

# Set the working directory to /codes
WORKDIR /codes

# Copy the current directory contents into the container at /codes/
ADD . /codes/

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt
