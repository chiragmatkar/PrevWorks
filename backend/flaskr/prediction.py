from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('predict', __name__, url_prefix='/predict')


@bp.route('/predict', methods=('GET', 'POST'))
def predict_company():
    db = get_db()
    mycursor = db.cursor()
    mycursor.execute(
        "INSERT INTO user (email, fname, lname, password) VALUES (%s, %s, %s, %s)",
        (username, fname, lname, generate_password_hash(password)),
    )
    db.commit()