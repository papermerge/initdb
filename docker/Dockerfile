FROM python:3.7-buster as build

RUN apt-get update \
    && apt-get install -y \
    build-essential python3-dev gcc \
    && apt-get -y clean

RUN python -m venv /venv
RUN /venv/bin/pip install --no-cache-dir -U pip
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --no-cache-dir -r /requirements.txt

FROM python:3.7-slim
ENV PATH="/venv/bin/:$PATH"

COPY --from=build /venv /venv

RUN apt-get update && apt-get install -y \
    build-essential python3-dev gcc libpq5 postgresql-client \
    && apt-get -y clean

COPY docker/run.sh /run.sh
COPY src /src
RUN chmod +x /run.sh

WORKDIR /src


CMD ["/venv/bin/python", "-m", "initdb"]