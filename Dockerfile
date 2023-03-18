# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

# Set working directory
WORKDIR / MonitorQueue

#copy source data from working directory
COPY requirements.txt requirements.txt

#install dependencies
RUN pip3 install -r requirements.txt

# port on which the app is running
EXPOSE 5000

COPY . .

# run the commad to start the app
CMD ["python", "app.py"]


