from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.pg_db_connect import get_db,close_db, string2bit

bp = Blueprint('forms', __name__, url_prefix='/forms')

@bp.route('/sendReport', methods=('GET', 'POST'))
def sendReport():
    print("Report submitted")
    print(request.form)

    if request.form['problemType'] in ['1','3'] and request.method == 'POST':
        error = None
        print('Get here for covid')
        if error is None:
            try:
                db = get_db()
                mycursor = db.cursor()
                mycursor.execute(
                    "INSERT INTO covidSurvey (userId, hadCovid, healthcare, fever, loss, pain, cough, breath, conjunctivitis, gi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (int(session['user_id']), request.form['hadCovid'],request.form['healthcare'],request.form['fever'],
                        request.form['loss'],request.form['pain'],request.form['cough'],request.form['breath'],request.form['conjunctivitis'],request.form['gi']))
                db.commit()
                close_db()
            except Exception as e:
                print(e)

    if request.form['problemType'] in ['2','3'] and request.method == 'POST':
        error = None
        print('Get here for injury')
        print(error)

        if error is None:
            try:
                db = get_db()
                print('herer1')
                mycursor = db.cursor()
                print('here2')
                mycursor.execute(
                    "INSERT INTO injury (userId, dateOccured ,injuryType, at_work, reported, supervisor, supervisor_email,  supervisor_relation, supervisor_phone, supervisor_date, reported_before, reported_date, description)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ",
                    (int(session['user_id']),
                     request.form['date_input'] + ' ' + request.form['time_input'],
                        request.form['injury_type'], request.form['at_work'],
                        request.form['reported'],
                        request.form['supervisor_name'], request.form['supervisor_email'], 
                        request.form['supervisor_relation'],request.form['supervisor_phone'],
                        request.form['supervisor_date'] + ' ' + request.form['supervisor_time'],
                        request.form['reported_before'], request.form['reported_before_date'],
                        request.form['injury_description']))
                print('here3')
                db.commit()
                print('here4')
                close_db
            except Exception as e:
                print(e)

    return render_template('covid.html')