from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import generate_password_hash,check_password_hash
from flaskr.pg_db_connect import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')



@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['email']
        password = generate_password_hash(request.form['password'])
        fname = request.form['first_name']
        lname = request.form['last_name']

        db = get_db()
        error = None
        print('Data:',username)
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif len(password) < 8:
            error = 'Password must be at least 8 characters long.'
        elif not (lambda x: any(map(str.isdigit, x)))(password):
            error = 'Password must contain at least one number.'

        if error is None:
            try:
                mycursor = db.cursor()
                mycursor.execute(
                    "INSERT INTO users (email, fname, lname, password) VALUES (%s, %s, %s, %s)",
                    (username, fname, lname, password),
                )
                db.commit()
            except Exception as e:
                print(e)
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']

        db = get_db()
        error = None
        mycursor = db.cursor()
        mycursor.execute(
            "SELECT * FROM users WHERE email = %s", (username,)
        )
        user = mycursor.fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user[4], password):
             error = 'Incorrect password.'
        print(error)

        if error is None:
            print('in')
            session.clear()
            session['user_id'] = user[0]
            session['session_type'] = 'user'
            return redirect(url_for('profile'))

        flash(error)

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return render_template('auth/login.html')

@bp.route('/registerCompany', methods=('GET', 'POST'))
def register_company():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        company = request.form['company']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif len(password) < 8:
            error = 'Password must be at least 8 characters long.'
        elif not (lambda x: any(map(str.isdigit, x)))(password):
            error = 'Password must contain at least one number.'

        if error is None:
            try:
                mycursor = db.cursor()
                mycursor.execute(
                    "INSERT INTO company (companyName, loginName, password) VALUES (%s, %s, %s)",
                    (company, username, password),
                )
                db.commit()
            except Exception as e:
                print(e)
            else:
                return redirect(url_for("auth.login_company"))

        flash(error)

    return render_template('auth/registerCompany.html')

@bp.route('/loginCompany', methods=('GET', 'POST'))
def login_company():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        mycursor = db.cursor()
        mycursor.execute(
            "SELECT * FROM company WHERE loginName = %s", (username,)
        )
        user = mycursor.fetchone()
        if user is None:
            error = 'Incorrect username.'
        # elif not check_password_hash(user[7], password):
        #     error = 'Incorrect password.'
        print(error)
        if error is None:
            session.clear()
            session['user_id'] = user[0]
            session['session_type'] = 'company'
            return redirect(url_for('companyProfile'))

        flash(error)

    return render_template('auth/loginCompany.html')


@bp.route('/covid', methods=('GET', 'POST'))
def covid():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        mycursor = db.cursor()
        mycursor.execute(
            "SELECT * FROM company WHERE loginName = %s", (username,)
        )
        user = mycursor.fetchone()
        if user is None:
            error = 'Incorrect username.'
        # elif not check_password_hash(user[7], password):
        #     error = 'Incorrect password.'
        print(error)
        if error is None:
            session.clear()
            session['user_id'] = user[0]
            session['session_type'] = 'company'
            return redirect(url_for('companyProfile'))

        flash(error)

    return render_template('covid.html')


@bp.route('/vaxInfo', methods=('GET', 'POST'))
def vaxInfo():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        mycursor = db.cursor()
        mycursor.execute(
            "SELECT * FROM company WHERE loginName = %s", (username,)
        )
        user = mycursor.fetchone()
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user[7], password):
            error = 'Incorrect password.'
        print(error)
        if error is None:
            session.clear()
            session['user_id'] = user[0]
            session['session_type'] = 'company'
            return redirect(url_for('companyProfile'))

        flash(error)

    return render_template('vaxInfo.html')

@bp.route('/covid_info_page', methods=('GET', 'POST'))
def covid_info_page():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        mycursor = db.cursor()
        mycursor.execute(
            "SELECT * FROM company WHERE loginName = %s", (username,)
        )
        user = mycursor.fetchone()
        if user is None:
            error = 'Incorrect username.'
        # elif not check_password_hash(user[7], password):
        #     error = 'Incorrect password.'
        print(error)
        if error is None:
            session.clear()
            session['user_id'] = user[0]
            session['session_type'] = 'company'
            return redirect(url_for('companyProfile'))

        flash(error)

    return render_template('covid_info_page.html')
