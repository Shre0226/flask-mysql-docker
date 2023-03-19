FROM python:3.8.5-alpine
COPY . .
WORKDIR .
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
RUN pip install -r requirements.txt
EXPOSE 5000