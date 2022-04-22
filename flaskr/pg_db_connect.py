import psycopg2
from flask import g
import os


DATABASE_URL=os.environ['DATABASE_URL']

def get_db():
    if 'db' not in g:
        if os.environ['ENVIRONMENT'] == "DEVELOPMENT":
            mydb = psycopg2.connect(DATABASE_URL, sslmode='require')
        elif os.environ['ENVIRONMENT'] == "LOCAL":
            mydb = psycopg2.connect(DATABASE_URL)
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
