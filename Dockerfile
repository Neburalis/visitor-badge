FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml .

RUN pip install uv

RUN uv sync

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
