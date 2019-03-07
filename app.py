from flask import Flask
import config
import decisions_service


import message_former
import mail_sender

import time
import atexit
import datetime
import random
import string

from apscheduler.schedulers.background import BackgroundScheduler

conf = config.config_data.load_config()
app = Flask(__name__)
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": conf.email_box_username,
    "MAIL_PASSWORD": conf.email_box_password
}

app.config.update(mail_settings)


@app.route("/<string:email>/<decision>")
def register_user_decision(email, decision):
    decision_saved = decisions_service.add_decision(email, decision)
    if decision_saved:
        return "User {0} decision: {1} registered".format(email, decision)
    else:
        return "User {0} decision has already been registered today".format(email)


@app.route("/config")
def print_config():
    conf = config.config_data.load_config()
    print(conf)
    return conf.print_as_html()


@app.route("/dict")
def print_dictionary_with_decisions():
    dictionary = decisions_service.get_dictionary()
    return dictionary.__str__()


@app.route("/datetime")
def print_server_datetime():
    return datetime.datetime.now().__str__()
    

def question_action():
    decisions_service.reset()
    with app.app_context():
        messages = message_former.create_list_of_asking_mails(conf.addresses)
        mail_sender.send_many(messages)


def summary_action():
    with app.app_context():
        message = message_former.create_summary_mail(
            decisions_service.get_dictionary())
        mail_sender.send(message)


scheduler = BackgroundScheduler()
scheduler.add_job(func=question_action, trigger="cron", hour = "13")
scheduler.add_job(func=summary_action, trigger="cron", hour = "15")
scheduler.start()

atexit.register(lambda: scheduler.shutdown)


if __name__ == "__main__":
    app.run(use_reloader=False)
