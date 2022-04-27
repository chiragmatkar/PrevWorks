from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.pg_db_connect import get_db,close_db, string2bit

bp = Blueprint('forms', __name__, url_prefix='/forms')

@bp.route('/sendReport', methods=('GET', 'POST'))
def sendReport():
    print("Report submitted")
    print(request.form)
    dateOccured =  request.form['date_input'] or None
    timeOccured = request.form['time_input'] or None

    if dateOccured == None or timeOccured == None:
        datetimeOccured=None
    else:
        datetimeOccured=request.form['date_input']+" "+request.form['time_input']


    if request.form['problemType'] in ['1','3'] and request.method == 'POST':
        error = None
        print('Get here for covid')
        if error is None:
            try:
                db = get_db()
                mycursor = db.cursor()
                mycursor.execute(
                    "INSERT INTO covidSurvey (userId, hadCovid, healthcare, fever, loss, pain, cough, breath, conjunctivitis, gi , dateoccured) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (int(session['user_id']), request.form['hadCovid'],request.form['healthcare'],request.form['fever'],
                        request.form['loss'],request.form['pain'],request.form['cough'],request.form['breath'],request.form['conjunctivitis'],request.form['gi'],datetimeOccured))
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
                db.commit()
                close_db
            except Exception as e:
                print(e)

    return render_template('covid.html')



@bp.route('/contactTracing',methods=('GET','POST'))
def contactTracing():
    print("contactTracing Report submitted")
    print(request.form)
    #
    # test_type= request.form.get('test_type') or None
    # vaccine_type =request.form.get('vaccine') or None
    # booster =request.form.get('booster') or None
    # booster_date= request.form.get('booster_date_input') or None
    #
    # diagnosis_date = request.form.get('diagnosis_date_input') or None
    # diagnosis_time = request.form.get('diagnosis_time_input') or None
    #
    # if diagnosis_date == None or diagnosis_time == None:
    #     diagnosis_timestamp = None
    # else:
    #     diagnosis_timestamp = diagnosis_date + " " + diagnosis_time
    #
    # vaccine_date = request.form.get('vaccine_date_input') or None
    # vaccine_time = request.form.get('vaccine_time_input') or None
    #
    # if vaccine_date == None or vaccine_time == None:
    #     vaccine_timestamp = None
    # else:
    #     vaccine_timestamp = vaccine_date + " " + vaccine_time
    #
    # booster_date = request.form.get('booster_date_input') or None
    # booster_time = request.form.get('booster_time_input') or None
    #
    # if booster_date == None or booster_time == None:
    #     booster_timestamp = None
    # else:
    #     booster_timestamp = booster_date + " " + booster_time
    #
    # contact1 = request.form['contact1_name'] or None
    # contact1_email= request.form['contact1_email'] or None
    # contact1_rel = request.form['contact1_relation']  or None
    # contact1_phone = request.form['contact1_phone'] or None
    # contact1_date = request.form['contact1_date'] or None
    # contact1_time = request.form['contact1_time'] or None
    #
    # contact1_timestamp = None
    # if contact1_date == None or contact1_time == None:
    #     contact1_timestamp = None
    # else:
    #     contact1_timestamp = contact1_date + " " + contact1_time
    #
    #
    #
    # contact2 = request.form['contact2_name'] or None
    # contact2_email = request.form['contact2_email'] or None
    # contact2_rel = request.form['contact2_relation'] or None
    # contact2_phone = request.form['contact2_phone'] or None
    # contact2_date = request.form['contact2_date'] or None
    # contact2_time = request.form['contact2_time'] or None
    #
    # contact2_timestamp = None
    # if contact2_date == None or contact2_time == None:
    #     contact2_timestamp = None
    # else:
    #     contact2_timestamp = contact2_date + " " + contact2_time
    #
    #
    # contact3 = request.form['contact3_name'] or None
    # contact3_email = request.form['contact3_email'] or None
    # contact3_rel = request.form['contact3_relation'] or None
    # contact3_phone = request.form['contact3_phone'] or None
    # contact3_date = request.form['contact3_date'] or None
    # contact3_time = request.form['contact3_time'] or None
    #
    # contact3_timestamp = None
    # if contact3_date == None or contact3_time == None:
    #     contact3_timestamp = None
    # else:
    #     contact3_timestamp = contact3_date + " " + contact3_time
    #
    # contact4 = request.form['contact4_name'] or None
    # contact4_email = request.form['contact4_email'] or None
    # contact4_rel = request.form['contact4_relation'] or None
    # contact4_phone = request.form['contact4_phone'] or None
    # contact4_date = request.form['contact4_date'] or None
    # contact4_time = request.form['contact4_time'] or None
    #
    # contact4_timestamp = None
    # if contact1_date == None or contact4_time == None:
    #     contact4_timestamp = None
    # else:
    #     contact4_timestamp = contact4_date + " " + contact4_time
    #
    # contact5 = request.form['contact5_name'] or None
    # contact5_email = request.form['contact5_email'] or None
    # contact5_rel = request.form['contact5_relation'] or None
    # contact5_phone = request.form['contact5_phone'] or None
    # contact5_date = request.form['contact5_date'] or None
    # contact5_time = request.form['contact5_time'] or None
    #
    # contact5_timestamp = None
    # if contact5_date == None or contact5_time == None:
    #     contact5_timestamp = None
    # else:
    #     contact5_timestamp = contact1_date + " " + contact1_time
    #
    # location1 = request.form['location1_name'] or None
    # location1_email = request.form['location1_email'] or None
    # location1_add1= request.form['location1_add1'] or None
    # location1_add2 = request.form['location1_add2']  or None
    # location1_date = request.form['location1_date'] or None
    # location1_time = request.form['location1_time'] or None
    #
    #
    # location1_timestamp = None
    # if location1_date == None or location1_time == None:
    #     contact5_timestamp = None
    # else:
    #     contact5_timestamp = contact1_date + " " + contact1_time
    #
    # location2 = request.form['location2_name'] or None
    # location2_email = request.form['location2_email'] or None
    # location2_add1 = request.form['location2_add1'] or None
    # location2_add2 = request.form['location2_add2'] or None
    # location2_date = request.form['location1_date'] or None
    # location2_time = request.form['location1_time'] or None
    #
    # location3 = request.form['location3_name'] or None
    # location3_email = request.form['location3_email'] or None
    # location3_add1 = request.form['location3_add1'] or None
    # location3_add2 = request.form['location3_add2'] or None
    # location3_date = request.form['location1_date'] or None
    # location3_time = request.form['location1_time'] or None
    #
    #
    # location4 = request.form['location4_name'] or None
    # location4_email = request.form['location4_email'] or None
    # location4_add1 = request.form['location4_add1'] or None
    # location4_add2 = request.form['location4_add2'] or None
    # location4_date = request.form['location4_date'] or None
    # location4_time = request.form['location4_time'] or None
    #
    #
    # location5 = request.form['location5_name'] or None
    # location5_email = request.form['location5_email'] or None
    # location5_add1 = request.form['location5_add1'] or None
    # location5_add2 = request.form['location5_add2'] or None
    # location5_date = request.form['location5_date'] or None
    # location5_time = request.form['location5_time'] or None
    #
    # description = request.form['injury_description'] or None

    if request.method == 'POST':
        error = None
        if error is None:
            try:
                db = get_db()
                # mycursor = db.cursor()
                #
                # cols = ('userId' , 'test_type', 'diagnosis_date', 'vaccine' , vaccine_date, booster, booster_date,
                #      contact1 , contact1_email , contact1_rel, contact1_phone ,contact1_date ,
                #      contact2 , contact2_email , contact2_rel, contact2_phone ,contact2_date ,
                #      contact3 , contact3_email , contact3_rel, contact3_phone ,contact3_date ,
                #      contact4 , contact4_email , contact4_rel, contact4_phone ,contact4_date ,
                #      contact5 , contact5_email , contact5_rel, contact5_phone ,contact5_date ,
                #      location1 , location1_email , location1_add1 ,location1_add2, location1_date ,
                #      location2 , location2_email , location2_add1 ,location2_add2 , location2_date ,
                #      location3 , location3_email , location3_add1 ,location3_add2 , location3_date ,
                #      location4 , location4_email , location4_add1 ,location4_add2 , location4_date ,
                #      location5 , location5_email , location5_add1 ,location5_add2 , location5_date ,
                #      description)
                 #vals = (

                # )
                 #query = f"INSERT INTO contacttracing {cols} values {vals}"


                #print(query)
                #mycursor.execute(query)
                #db.commit()
                #close_db()
                print("--Here1---")
            except Exception as e:
                print(e)

    return render_template('covid_info_page.html')


