FROM python:3.12.9-slim AS base

RUN useradd --create-home appuser
USER appuser

ENV PATH="/home/appuser/.local/bin:$PATH" \
    HOST="0.0.0.0" \
    PORT=8000

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir pip==25.0.1 && \
    pip install --no-cache-dir poetry==2.1.3 && \
    poetry install --no-root
    
FROM base AS dev
USER root

# hadolint ignore=DL3008
RUN apt-get update && apt-get install -y --no-install-recommends curl && \
    curl -sSL https://github.com/hadolint/hadolint/releases/latest/download/hadolint-Linux-x86_64 \
    -o /usr/local/bin/hadolint && chmod +x /usr/local/bin/hadolint

USER appuser

FROM base AS prod
COPY . .
EXPOSE 8000
ENTRYPOINT ["poetry", "run"]
CMD ["python", "src/main.py"]
