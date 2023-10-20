FROM python:3.9

WORKDIR /app
COPY app.py /app/app.py
RUN pip install prometheus_client

CMD ["python", "app.py"]
