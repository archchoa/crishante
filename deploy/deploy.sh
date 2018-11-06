#!/bin/sh
cd /var/apps/crishante && python manage.py migrate && python manage.py collectstatic --noinput -i debug_toolbar && supervisord -n -c /etc/supervisor/conf.d/supervisor-gunicorn.conf
