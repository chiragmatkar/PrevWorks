from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.pg_db_connect import get_db, close_db

bp = Blueprint('covid', __name__, url_prefix='/covid')


@bp.route('/active_covid')
def active_covid():
    print("Report submitted")
    print(request.form)

    try:
        db = get_db()
        mycursor = db.cursor()
        query = """select covidsurvey.surveyid, users.fname , users.lname , covidsurvey.dateoccured
                            from covidsurvey
                            INNER JOIN users on covidsurvey.userid = users.userid 
                        """
        mycursor.execute(query)
        data = mycursor.fetchall()

    except Exception as e:
        print(e)


    return render_template('active_covids.html', covid_patients=data)
