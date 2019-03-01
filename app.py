from flask import Flask
app = Flask(__name__)


@app.route('/<string:username>/<decision>')
def show_user_profile(username, decision):
    return 'User{0} decision: {1}'.format(username, decision)


if __name__ == "__main__":
    app.run()