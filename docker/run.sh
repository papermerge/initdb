#!/bin/sh

CMD="$1"

INIT="/app/venv/bin/python -m initdb"

case $CMD in
    init)
        $INIT  # will wait until database is ready
    ;;
    *)
        echo "Unkown command: '${CMD}'. Bye."
esac