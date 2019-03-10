from flask import Flask, current_app
from flask_mail import Mail, Message
import config


def create_asking_mail(user_email: str) -> Message:
    app = current_app
    host_address = get_host()
    message = Message(subject="FlatMatesFood asking mail",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[user_email],
                      html="""
                    <div>
                    <h2>
                        Hey, would you like to order food today?
                    </h2>
                    
                    <p>
                    <a href="{host}/{email}/1" style="padding: 15px 25px; border-radius: 10px; text-align:center;text-decoration: none;display:inline-block; color: white; background-color:#4dff4d; font-size:1.2em; min-width:10em">
                        Oh yeah!
                    </a>
                    </p>
                    
                    <p>
                    <a href="{host}/{email}/0" style="padding: 15px 25px;  border-radius: 10px; text-align:center;text-decoration: none;display:inline-block; color: white; background-color:#ff4d4d; font-size:1.2em; min-width:10em">
                        No, thanks
                    </a>
                    </p>
                    </div>""".format(host=host_address, email=user_email))
    return message


def create_list_of_asking_mails(user_emails: list) -> list:
    messages = []
    for email in user_emails:
        messages.append(create_asking_mail(email))

    return messages


def create_summary_mail(users_decisions: dict) -> Message:
    app = current_app
    message = Message(subject="FlatMatesFood summary",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=list(users_decisions.keys()),
                      html="""
                    <div>
                    <h1>
                        I have summary for today:
                    </h1>
                    <div>
                        {0}
                    <div>
                    </div>""".format(get_html_summary(users_decisions)))
    return message


def get_html_summary(users_decisions: dict) -> str:
    html = ""
    for user in users_decisions.keys():
        decision = "?"
        if users_decisions[user] == "1":
            decision = "I want to order food!"
        else:
            decision = "I don't want to order food :("
        line = "<p> {0} : {1} </p>".format(user, decision)
        html = html + line

    return html


def get_host():
    conf = config.config_data.load_config()
    return conf.host