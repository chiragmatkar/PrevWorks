from flask import (
    Blueprint, session, render_template, url_for, current_app
)
from flask_mail import Mail, Message
from smtplib import  SMTPException

bp = Blueprint('mail', __name__, url_prefix='/mail')


@bp.route('/sendMail', methods=('GET', 'POST'))
def sendMail():
    current_app.config.update(dict(
        DEBUG=True,
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_TLS=False,
        MAIL_USE_SSL=True,
        MAIL_USERNAME='prevworks1@gmail.com',
        MAIL_PASSWORD='prevworks@123',
    ))
    mail = Mail(current_app)
    msg = Message(
        'Message from PrevWorks Support Team',
        sender='prevworks1@gmail.com',
        recipients=[session['user_email']]
    )
    msg.body = '''Unfortunately, one of your colleagues has contracted COVID-19 and reported you as someone they have been in contact with recently.
                  But don't panic! If you have not been tested, please do as asap and make sure to quarantine for at least 14 days.
                  More information about quarantine and vaccination info can be found at VaxInfo section in the Covid Info Page.
               '''
    mail.send(msg)


    return render_template('covid_info_page.html')

