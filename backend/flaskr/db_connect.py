import mysql.connector
from flask import g


def get_db():
    if 'db' not in g:
        mydb = mysql.connector.connect(
            user='root',
            password='',
            host='127.0.0.1',
            port=3306,
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
