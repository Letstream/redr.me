#!/bin/sh

echo Starting Gunicorn.

rm -f /home/docker_deploy_user/pids/*.pid

gunicorn app.wsgi:application \
    --name app \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --threads 4 \
    --log-level=debug \
    --log-file=/home/docker_deploy_user/applogs/gunicorn.log \
    --access-logfile=/home/docker_deploy_user/applogs/access.log 
