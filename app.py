from flask import Flask
app = Flask(__name__)


@app.route('/<string:username>/<decision>')
def register_user_decision(username, decision):
    return 'User{0} decision: {1}'.format(username, decision)


if __name__ == "__main__":
    app.run()