import psycopg2
from flask import g

def get_db():
    if 'db' not in g:
        mydb = psycopg2.connect(
            user='postgres',
            password='',
            host='127.0.0.1',
            port=5432,
            database='prevworks'
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
