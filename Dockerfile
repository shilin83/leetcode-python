FROM python:3.13.1-alpine

WORKDIR /app

COPY . .

RUN pip install pytest

CMD ["pytest"]
