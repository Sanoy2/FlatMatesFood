from flask import Flask
import config
import decisions_service
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


if __name__ == "__main__":
    app.run()