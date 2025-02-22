FROM python:alpine

WORKDIR /app

COPY . .

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN uv add pytest

CMD ["uv", "run", "pytest"]
