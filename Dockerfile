FROM python:3.10

RUN mkdir -p /app/sql_app

WORKDIR /app/sql_app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app
