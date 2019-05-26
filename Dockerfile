FROM python:3.6

LABEL Name=src Version=0.0.1
EXPOSE 3000

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY . .

