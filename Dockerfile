# Dockerfile
FROM python:3.9

WORKDIR Docker

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest", "tests/test.py"]

