FROM python:3.8

ARG APP_DIR=/app
WORKDIR ${APP_DIR}

ADD . .

RUN pip install -r requirements.txt

ENV APP_PORT=3000
EXPOSE ${APP_PORT}
HEALTHCHECK --interval=30s --retries=3 --timeout=30s --start-period=5s \
    CMD curl -s -f http://localhost:${APP_PORT}/healthz > /dev/null || exit 1

ENV PORT=${APP_PORT}
ENV INSTANCE_NAME=xuyangbo
ENTRYPOINT [ "python", "main.py" ]