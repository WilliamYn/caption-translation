FROM python:3.8-slim-buster

WORKDIR /app
COPY translation.py /app

RUN pip install deep_translator requests Flask==2.2.2 Flask-Cors==3.0.10

EXPOSE 5000

CMD ["python", "translation.py"]
