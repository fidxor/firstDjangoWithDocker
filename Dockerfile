# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./requirements.txt /code/
COPY ./wait-for-it.sh /code/
RUN apt-get update && \
apt-get install -y pkg-config default-libmysqlclient-dev build-essential && pip3 install mysqlclient && pip3 install gunicorn
RUN pip3 install -r requirements.txt
RUN chmod 755 /code/wait-for-it.sh