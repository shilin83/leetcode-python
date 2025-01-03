FROM python:3.13-alpine3.21

WORKDIR /app

COPY . .

RUN pip install pytest

CMD ["pytest"]
