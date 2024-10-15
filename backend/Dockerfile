ARG PYTHON_VERSION=3.10

FROM python:${PYTHON_VERSION} AS build


ARG POETRY_VERSION=1.6.1


# Set working directory to /usr/src
WORKDIR /usr/src

COPY requirements.txt ./
COPY pyproject.toml ./

RUN pip install poetry==${POETRY_VERSION}
RUN poetry install

# Copy all files into /usr/src
COPY . ./


ENV PYTHONPATH=/usr/src/src
CMD ["poetry","run","python","-m", "project.main"]
