from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.pg_db_connect import get_db

bp = Blueprint('companies', __name__, url_prefix='/companies')


# return the companies that an employee works at
@bp.route('/getEmployeesCompanies', methods=('GET', 'POST'))
def getEmployeesCompanies():
    if request.method == 'POST':
        user_id = session['user_id']
        db = get_db()
        error = None
        mycursor = db.cursor()
        mycursor.execute(
            "SELECT position, user2companyId, companyName "
            "FROM user2company, company "
            "WHERE userId = %d AND user2company.companyId = company.companyId", user_id
        )
        # companyData = [{}]
        data = mycursor.fetchall()
        # while user2company is not None:
        #     dict = {'position':user2company[0], 'user2companyId':user2company[1], 'companyName':user2company[2]}
        #     companyData.append(dict)
        #     user2company = mycursor.fetchone()

        flash(error)

    return render_template('profile.html', data=data)
