ARG image=alpine:3.14

FROM ${image} as builder
RUN    apk add                \
        build-base            \
        linux-headers         \
        pcre-dev              \
        python3-dev           \
    && python3 -m venv /.venv \
    && . /.venv/bin/activate  \
    && pip install            \
        flask                 \
        pytest                \
        uwsgi

FROM ${image}
COPY --from=builder /.venv /.venv
COPY content /app
RUN apk add pcre python3
WORKDIR /app
ENTRYPOINT [ "/app/entrypoint.sh" ]