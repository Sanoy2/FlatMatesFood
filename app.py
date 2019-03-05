from flask import Flask
import config
import decisions_service


import time
import atexit
import datetime
import random
import string

from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)


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
    

def send_question_email():
    return


def send_summary_mail():
    return


def question_action():
    decisions_service.reset()
    send_question_email()


def summary_action():
    return


scheduler = BackgroundScheduler()
scheduler.add_job(func=question_action, trigger="cron", hour = "13")
scheduler.add_job(func=summary_action, trigger="cron", hour = "15")
scheduler.start()

atexit.register(lambda: scheduler.shutdown)


if __name__ == "__main__":
    app.run(use_reloader=False)