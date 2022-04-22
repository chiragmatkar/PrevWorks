import psycopg2
from flask import g
import os

pg_host=os.environ['DB_HOST']
pg_db=os.environ['DB_NAME']
pg_user=os.environ['DB_USER']
pg_password=os.environ['DB_PASSWORD']


def get_db():
    if 'db' not in g:
        mydb = psycopg2.connect(
            user=pg_user,
            password=pg_password,
            host=pg_host,
            port=5432,
            database=pg_db,
            sslmode='require'
        )
        g.db = mydb
    return mydb


def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()


def string2bit(imp_string):
    if imp_string == 'false':
        return 0
    return 1
