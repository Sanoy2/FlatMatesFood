from flask import Flask
import config
app = Flask(__name__)


@app.route('/<string:username>/<decision>')
def register_user_decision(username, decision):
    return 'User{0} decision: {1}'.format(username, decision)


@app.route('/config')
def print_config():
    conf = config.config_data.load_config()
    print(conf)
    return conf.print_as_html()


if __name__ == "__main__":
    app.run()