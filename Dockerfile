# Bissmillahirrahmanirraheem
FROM ubuntu:20.04 as build-stage

ARG GPG_PRIVATE_KEY_PART_1
ARG GPG_PRIVATE_KEY_PART_2

ENV GPG_PRIVATE_KEY_PART_1=${GPG_PRIVATE_KEY_PART_1}
ENV GPG_PRIVATE_KEY_PART_2=${GPG_PRIVATE_KEY_PART_2}
ENV GPG_TTY=/dev/console

RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    gpg \
    wget && \
    sh -c "echo 'deb https://gitsecret.jfrog.io/artifactory/git-secret-deb git-secret main' >> /etc/apt/sources.list" \
    && wget -qO - 'https://gitsecret.jfrog.io/artifactory/api/gpg/key/public' | apt-key add - && \
    apt-get update && apt-get install -y --no-install-recommends git-secret


WORKDIR /app
COPY . .
RUN echo $GPG_PRIVATE_KEY_PART_1$GPG_PRIVATE_KEY_PART_2 | tr -d "\n" | base64 -d | gpg --import - && git secret reveal

# production stage
FROM python:3.8 as production-stage

ENV PYTHONUNBUPYTHONUNBUFFERED="TRUE"
ENV PORT=8000

WORKDIR /app

COPY --from=build-stage /app .
RUN pip install --no-cache-dir -r requirements.txt
RUN alembic upgrade head

CMD uvicorn main:app --port $PORT --host 0.0.0.0

