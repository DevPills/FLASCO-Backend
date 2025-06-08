FROM python:3.12-slim

WORKDIR /app

RUN echo "precedence ::ffff:0:0/96  100" > /etc/gai.conf

COPY pyproject.toml poetry.lock ./

RUN pip install poetry

COPY . .

RUN poetry install

EXPOSE 8000

CMD ["uvicorn flasco.main:app --host 0.0.0.0 --port 8000"]