# Pull base image
FROM python:3.11.0-alpine as builder

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /server

# Install necessary packages and Rust
RUN apk add --no-cache \
    gcc \
    libpq-dev \
    musl-dev \
    libffi-dev \
    openssl-dev \
    mariadb-dev \
    ffmpeg \
    curl \
    build-base \
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && /root/.cargo/bin/rustup default stable \
    && /root/.cargo/bin/rustup install 1.64.0 \
    && /root/.cargo/bin/rustup target add x86_64-unknown-linux-musl

# Set the PATH for Rust
ENV PATH="/root/.cargo/bin:${PATH}"

# Check if rustc is installed correctly
RUN rustc --version


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
