FROM python:3.8.16-alpine3.17
WORKDIR /test
COPY . .
RUN pip install -r requirements.txt