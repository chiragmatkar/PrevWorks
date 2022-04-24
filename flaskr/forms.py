from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.pg_db_connect import get_db, string2bit

bp = Blueprint('forms', __name__, url_prefix='/forms')

@bp.route('/sendReport', methods=('GET', 'POST'))
def send_report():
    print("Report submitted")
    print(request.form)
    if request.form['problemType'] in ['1','3']:
        db = get_db()
        error = None
        print('Get here')
        if error is None:
            try:
                mycursor = db.cursor()
                mycursor.execute(
                    "INSERT INTO covidSurvey (userId, hadCovid, healthcare, fever, loss, pain, cough, breath, conjunctivitis, gi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (int(session['user_id']), string2bit(request.form['hadCovid']),
                        string2bit(request.form['healthcare']),string2bit(request.form['fever']),
                        string2bit(request.form['loss']),string2bit(request.form['pain']),
                        string2bit(request.form['cough']),string2bit(request.form['breath']),
                        string2bit(request.form['conjunctivitis']),string2bit(request.form['gi']),),
                )
                db.commit()
            except Exception as e:
                print(e)
    if request.form['problemType'] in ['2','3']:
        db = get_db()
        error = None
        print('Get here')
        if error is None:
            try:
                mycursor = db.cursor()
                mycursor.execute(
                    """INSERT INTO injury (userId, dateOccured, injuryType, 
                    at_work, reported, supervisor, supervisor_email, 
                    supervisor_relation, supervisor_phone, supervisor_date,
                     reported_before, reported_date, description) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (int(session['user_id']),
                     request.form['date_input'] + 'T' + request.form['time_input'],
                        request.form['injury_type'], string2bit(request.form['at_work']),
                        string2bit(request.form['reported']),
                        request.form['supervisor_name'], request.form['supervisor_email'], 
                        request.form['supervisor_relation'],request.form['supervisor_phone'],
                        request.form['supervisor_date'] + 'T' + request.form['supervisor_time'],
                        string2bit(request.form['reported_before']), request.form['reported_before_date'],
                        request.form['injury_description'],),
                )
                db.commit()
            except Exception as e:
                print(e)

    return render_template('userProfile.html')