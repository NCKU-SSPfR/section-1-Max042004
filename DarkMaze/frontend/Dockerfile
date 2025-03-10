# TODO: Install the frontend dependency package into the app folder inside the container.
FROM python:3.11-slim

RUN useradd --create-home appuser

WORKDIR /app

RUN chown -R appuser /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/

USER appuser

EXPOSE 8088

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]