from flask import Flask
import config
import decisions_service


import time
import atexit
import datetime

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
    

def do_something():
    print("Doing something")
    decisions_service.reset()
    decisions_service.add_decision("krzysztof.tomkow@gmail.com", 1000)


scheduler = BackgroundScheduler()
scheduler.add_job(func=do_something, trigger="cron", hour = "11", minute = "31")
scheduler.start()

atexit.register(lambda: scheduler.shutdown)


if __name__ == "__main__":
    app.run(use_reloader=False)