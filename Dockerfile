FROM python:3.12.0a5-alpine3.17 AS base

WORKDIR /web/html

COPY init.py /web/init.python

EXPOSE 8080

CMD [ "python3", "-u" , "/web/init.py" ]