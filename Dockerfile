FROM python:3.11 AS poetry

RUN pip install poetry

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry export --output requirements.txt

FROM python:3.11-slim-buster
WORKDIR /app
COPY --from=poetry /app/requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python3", "serve.py"]