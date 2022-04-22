import psycopg2
from flask import g
import os

pg_host=os.environ['DB_HOST']
pg_db=os.environ['DB_NAME']
pg_user=os.environ['DB_USER']
pg_password=os.environ['DB_PASSWORD']
DATABASE_URL=os.environ['DATABASE_URL']

def get_db():
    if 'db' not in g:
        mydb = psycopg2.connect(DATABASE_URL, sslmode='require')
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
