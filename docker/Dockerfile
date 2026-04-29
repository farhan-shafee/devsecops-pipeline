FROM python:3.12-slim

WORKDIR /app

RUN adduser --disabled-password --gecos "" appuser

COPY src/example_app.py /app/src/example_app.py

USER appuser

EXPOSE 8000

CMD ["python", "/app/src/example_app.py"]
