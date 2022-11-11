FROM amancevice/superset:latest
USER root

#Install the plugins for your database
RUN pip install clickhouse-driver clickhouse-sqlalchemy psycopg2

RUN superset superset db upgrade
RUN superset superset init

