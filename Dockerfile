# Pull base image
FROM python:3.11.0-alpine as builder

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /server

RUN apk add --no-cache \
    gcc \
    libpq-dev \
    musl-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    mariadb-dev \
    ffmpeg

RUN pip install poetry==1.8.1

RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* ./

# Stage 2: Production Stage
FROM builder AS production

RUN poetry install --no-interaction --no-ansi --no-root --no-directory --without dev

COPY . .

CMD python manage.py runserver 0.0.0.0:8000

# Stage 3: Development Stage
FROM builder AS development

ENV ENVIRONMENT=development

RUN poetry install --no-interaction --no-ansi --no-root --no-directory

COPY . .

CMD python manage.py runserver_with_migrate 0.0.0.0:8080
