# syntax=docker/dockerfile:1
FROM python:3.8
WORKDIR /pythonProject2
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python3", "app.py", "--host=0.0.0.0"]


