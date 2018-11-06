FROM python:3.5

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y

RUN groupadd webapps
RUN useradd crishante -G webapps
RUN mkdir -p /var/log/crishante/ && chown -R crishante /var/log/crishante/ && chmod -R u+rX /var/log/crishante/
RUN mkdir -p /var/run/crishante/ && chown -R crishante /var/run/crishante/ && chmod -R u+rX /var/run/crishante/

RUN apt-get install -y supervisor
RUN mkdir -p /var/log/supervisord && chown -R crishante /var/log/supervisord/ && chmod -R u+rX /var/log/supervisord/
ADD ./deploy/supervisor-gunicorn.conf /etc/supervisor/conf.d/supervisor-gunicorn.conf

RUN pip install gunicorn

ADD requirements.txt /tmp/requirements.txt
RUN cd /tmp && pip install -r requirements.txt

RUN mkdir -p /var/apps/crishante
ADD /static /var/apps/crishante/staticfiles

RUN mkdir -p /var/www/media && chown -R crishante /var/www/media/ && chmod -R u+rX /var/www/media/

RUN groupadd varwwwusers
RUN adduser www-data varwwwusers
RUN chgrp -R varwwwusers /var/www/media/
RUN chmod -R 760 /var/www/media/

WORKDIR /var/apps/crishante

ADD . /var/apps/crishante

CMD ["sh", "./deploy/deploy.sh"]

EXPOSE 5000
