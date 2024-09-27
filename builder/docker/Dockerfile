FROM python:3.11.1-slim-bullseye as base

FROM base AS builder
COPY ./builder/requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

FROM base AS release

COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
WORKDIR /app
COPY . /app
ENV PYTHONPATH=/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
