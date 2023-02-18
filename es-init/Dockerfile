FROM alpine:latest

RUN apk add --no-cache curl

COPY docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.sh"]