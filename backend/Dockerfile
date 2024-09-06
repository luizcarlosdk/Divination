ARG PYTHON_VERSION=3.8

FROM python:${PYTHON_VERSION} AS build

# Set working directory to /usr/src
WORKDIR /usr/src

# Copy all files into /usr/src
COPY . ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/usr/src/src
CMD ["python", "src/project/main.py"]
