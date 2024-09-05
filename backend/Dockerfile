ARG PYTHON_VERSION=3.8

FROM python:${PYTHON_VERSION} AS build

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install python-dotenv

CMD ["python","main.py"]