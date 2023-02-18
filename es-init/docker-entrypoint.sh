#!/bin/sh

set -e
alias curles="curl -u $ELASTICSEARCH_USERNAME:$ELASTICSEARCH_PASSWORD"

#  Wait for ES to be ready
until curles $ELASTICSEARCH_HOST; do
  >&2 echo "Elasticsearch is unavailable - sleeping"
  sleep 1
done

# Create index
curles -XPUT $ELASTICSEARCH_HOST/elections

exec "$@"