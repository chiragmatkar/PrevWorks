from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.pg_db_connect import get_db

import math

import sys
from flask import jsonify

bp = Blueprint('injuries', __name__, url_prefix='/injuries')

# return the companies that an employee works at
@bp.route('/getFrequencyOfInjuries', methods=('GET', 'POST'))
def getFrequencyOfInjuries():
    if request.method == 'POST' or request.method == 'GET':
        user_id = session['user_id']
        # user_id = 1
        db = get_db()
        error = None
        mycursor = db.cursor()
        query = """SELECT injuryType, COUNT(*) 
            FROM injury
            WHERE injury.companyId=%d
            GROUP BY injuryType 
            ORDER BY COUNT(*) DESC;""" % user_id
        mycursor.execute(query, (0))
        injuries = {}
        injuriesColors = {}
        # g is in range of 0 255
        r = 255
        g = 0
        b = 0
       
        minAmount = 0
        maxAmount = 0
        # find largest injury frequency, that should be g = 0
        # f(x) = ( ((b-a)(x - min)) / (max - min) ) + a
        firstItFlag = False
        for injury in mycursor:
            injuryType = str(injury[0]).replace('-left','').replace('-right','')
            if(injuryType in injuries):
                injuries[injuryType] = injuries[injuryType] + int(injury[1])
            else:
                injuries[injuryType] = int(injury[1])
        allValues = injuries.values()
        maxAmount = max(allValues)
        minAmount = min(allValues)
        divider = maxAmount - minAmount
        if divider == 0:
            divider = 1


        # set most common colors
        injuriesColors['mostCommonColor'] = (r,g,b)
        injuriesColors['leastCommonColor'] = (r,255,b)
        
        for injuryName in injuries:
            g = math.floor(((255)*(int(injuries[injuryName]) - minAmount)) / (divider))
            g = 255 - g
            color = '#%02x%02x%02x' % (r, g, b)
            injuriesColors[injuryName] = color

        # retreieve data for injury reports table
        mycursor.execute(
            """SELECT injury.injuryId, injury.injuryType, injury.reported_date, fname, lname, injury.userId, injury.companyId
            FROM injury
            INNER JOIN user ON injury.userId = user.userId
            WHERE injury.companyId=%d;""" % user_id
        )
        # TODO(karalee): add "WHERE PrevWorks.injury.companyId = 1;" to query
        injuryList = mycursor.fetchall()

        flash(error)

    return render_template('injuries.html',frequencyOfInjuries=injuriesColors, listOfInjuries=injuryList)

@bp.route('/bodyPartClicked/<body_part>')
def bodyPartClicked(body_part):
    user_id = session['user_id']
    print(body_part, file=sys.stdout)

    db = get_db()
    error = None
    mycursor = db.cursor()
    query = """SELECT injury.injuryId, injury.reported_date, fname, lname, injury.userId, injury.companyId
            FROM injury
            INNER JOIN user ON injury.userId = user.userId
            WHERE injury.companyId =%d AND
            injury.injuryType LIKE '%s';""" % (user_id, body_part)
    print(body_part)
    mycursor.execute(query, (0))
    # TODO(karalee): add "WHERE PrevWorks.injury.companyId = 1;" to query
    injuries = mycursor.fetchall()
    return(jsonify(allInjuries=injuries))