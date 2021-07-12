#!/bin/sh

if [ -z $PORT ]; then PORT=8080; fi
. /.venv/bin/activate
uwsgi --yaml app.yaml