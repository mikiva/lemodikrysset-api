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

CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080
#CMD ["python3", "serve.py"]