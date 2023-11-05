#!/bin/bash
###########

sh -c "nginx_reloader.sh &"
exec usr/local/bin/entrypoint.sh "$@"