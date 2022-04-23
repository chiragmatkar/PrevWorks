import os
from flask import Flask, render_template, request, redirect, session, url_for
from . import auth
from . import forms
from . import injuryReports
import sys
from . import companies
from flaskr.pg_db_connect import get_db
from datetime import datetime
from .compensation import calc_total_comp, calc_industry_premium
import pandas as pd


# def check_session():
#     try:
#         print(session['user_id'])
#         if session['user_id']:
#             return True
#         return False
#     except:
#         return False


# def check_session(session_type, target_render):
def check_session(*args):
    if args:
        session_type = args[0]
        target_render = args[1]
        try:
            if int(session['user_id']) > 0 and session['session_type'] == session_type:
                return target_render
        except:
            return render_template('auth/login.html')
    else:
        try:
            print(session['user_id'])
            if session['user_id']:
                return True
            return False
        except:
            return False


def create_app(test_config=True):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return render_template('auth/register.html')

    @app.route('/register')
    def register_home():
        return render_template('auth/register.html')

    @app.route('/login')
    def login_home():
        return render_template('auth/login.html')

    @app.route('/registerCompany')
    def register_company():
        class_df = pd.read_csv('data/raw/Employee_Classification_Rates.csv')
        industry_df = pd.read_excel('data/raw/labor_statistics/by_industry/rate/cd_r5_2019.xlsx')

        classifications = class_df['phrase'].tolist()
        industries = industry_df['Industry(1)'].tolist()
        industries.pop(0)
        industries.pop(0)
        classifications.pop(0)
        if request.method == 'POST':
            industry = request.args.get('industry')
            classification = request.args.get('classification')
            company = request.args.get('company')
            db = get_db()
            mycursor = db.cursor()
            print("company posted")
            mycursor.execute(
                "INSERT INTO companyToIndustry (companyName, industry, classification) "
                f"VALUES ('{company}','{industry}','{classification}');"
            )
        return render_template('auth/registerCompany.html', industries=industries, classifications=classifications)

    @app.route('/loginCompany')
    def login_company():
        return render_template('auth/loginCompany.html')

    # added to test
    @app.route('/covid')
    def covid():
        return render_template('covid.html')

    # added to test
    @app.route('/covid_info_page')
    def covid_info_page():
        return render_template('covid_info_page.html')

    # User routes
    @app.route('/profile')
    def profile():
        return check_session('user', render_template('userProfile.html'))

    @app.route('/assessment')
    def assessment():
        return check_session('user', render_template('assessment.html'))

    @app.route('/reportInjury')
    def report_injury():
        return check_session('user', render_template('ReportInjury.html'))

    @app.route('/companies')
    def companies():
        return check_session('user', render_template('companies.html'))

    @app.route('/table')
    def table():
        return check_session('user', render_template('table.html'))

    #body part routes
    @app.route('/shoulder')
    def shoulder():
        return check_session('user', render_template('bodyparts/shoulder.html'))
    @app.route('/ankle')
    def ankle():
        return check_session('user', render_template('bodyparts/ankle.html'))
    @app.route('/head')
    def head():
        return check_session('user', render_template('bodyparts/head.html'))
    @app.route('/chest')
    def chest():
        return check_session('user', render_template('bodyparts/chest.html'))
    @app.route('/knee')
    def knee():
        return check_session('user', render_template('bodyparts/knee.html'))
    @app.route('/leg')
    def leg():
        return check_session('user', render_template('bodyparts/leg.html'))
    @app.route('/neck')
    def neck():
        return check_session('user', render_template('bodyparts/neck.html'))
    @app.route('/stomach')
    def stomach():
        return check_session('user', render_template('bodyparts/stomach.html'))
    @app.route('/elbow')
    def elbow():
        return check_session('user', render_template('bodyparts/elbow.html'))
    @app.route('/arm')
    def arm():
        return check_session('user', render_template('bodyparts/arm.html'))
    @app.route('/wrist')
    def wrist():
        return check_session('user', render_template('bodyparts/wrist.html'))
    @app.route('/hand')
    def hand():
        return check_session('user', render_template('bodyparts/hand.html'))
    @app.route('/foot')
    def foot():
        return check_session('user', render_template('bodyparts/foot.html'))
    @app.route('/hips')
    def hip():
        return check_session('user', render_template('bodyparts/hips.html'))
    @app.route('/back')
    def back():
        return check_session('user', render_template('bodyparts/back.html'))

    # Company Routes
    @app.route('/companyProfile')
    def companyProfile():
        return check_session('company', render_template('companyProfile.html'))

    # Simpulation
    @app.route('/simulation')
    def simulation():
        return render_template('simulation.html')

    @app.route('/analytics')
    def analytics():
        if check_session():
            # get necessary data
            db = get_db()
            mycursor = db.cursor()
            mycursor.execute(
                '''SELECT * FROM company c
                INNER JOIN user2company u2c ON c.companyId = u2c.companyId
                LEFT JOIN feature2user f2u ON f2u.userId = f2u.userId = u2c.userId and f2u.featureId = 3'''
            )
            payroll = 0
            num_workers = 0
            # calculate the total employee payroll (assume average of $50k if no salary listed)
            # calculate number of workers
            for row in mycursor:
                salary = row[15]
                companyName = row[1]
                if salary:
                    payroll += row[15]
                else:
                    payroll += 50000
                num_workers += 1
            payroll = 10000000
            mycursor.execute(f"SELECT * FROM PrevWorks.companyToIndustry WHERE companyName = '{companyName}';")
            row = mycursor.fetchall()

            industry = row[0][1]
            classification = row[0][2]

            # assume each worker works 40 hours/week with 2 weeks vacation per year
            hours_worked = num_workers * 40 * 50

            mycursor.execute(
                "SELECT * FROM PrevWorks.injury;"
            )
            currentYear = datetime.now().year
            num_injuries = 0
            # find number of injuries this year
            for row in mycursor:
                if row[1].year == currentYear:
                    num_injuries += 1
            current_premium = str(calc_total_comp(classification, industry, payroll, hours_worked, num_injuries))

            # get industry premium
            industry_premium = str(calc_industry_premium(classification, industry, payroll))

        return check_session('company', render_template('analytics.html', current_premium=current_premium,
                                                        industry_premium=industry_premium, num_injuries=num_injuries))

    @app.route('/employees')
    def employees():
        return check_session('company', render_template('employees.html'))

    @app.route('/injuries')
    def injuries():
        # print('This is error output', file=sys.stderr)
        # return render_template('injuries.html')
        return injuryReports.getFrequencyOfInjuries()
        # return check_session('company', render_template('companyProfile.html'))



    app.register_blueprint(auth.bp)
    app.register_blueprint(forms.bp)
    app.register_blueprint(injuryReports.bp)

    return app
