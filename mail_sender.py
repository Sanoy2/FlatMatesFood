from flask import Flask, current_app
from flask_mail import Mail, Message


def send(message: Message):
    app = current_app
    mail = Mail(app)
    mail.send(message)
    return


def send_many(messages: list):
    app = current_app
    mail = Mail(app)
    with mail.connect() as conn:
        for message in messages:
            conn.send(message)