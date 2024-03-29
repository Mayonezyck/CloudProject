# start by pulling the python image
FROM python:3.9.7-alpine

# switch working directory
WORKDIR /app

# copy the requirements file into the image
COPY requirements.txt .

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY folders/ ./

COPY main.py .

# configure the container to run in an executed manner
CMD [ "python", "main.py" ]