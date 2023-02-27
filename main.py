from flask import Flask, request

from email_notify import GM_SMTP
from discord_notify import DC_Webhook

import os

def read_secret(name):
    f = open(os.path.join("/run/secrets", name))
    return f.read()

def main():
    app = Flask(__name__)

    @app.route('/send', methods = ['POST'])
    def send():
        if request.method == "POST":
            is_email = True
            try:
                sender = request.form["sender"]
                recipient = request.form["recipient"]
                subject = request.form["subject"]
            except KeyError:
                is_email = False

            try:
                method = request.form["send_method"]
                payload = request.form["payload"]
            except KeyError:
                return 'Method and/or payload not provided', 400

            method = method.split(",")

            if "discord" in method:
                dc_conn = DC_Webhook(read_secret("dc_webhook-pass"))
                dc_conn.send(payload)
            if "email" in method and is_email:
                em_conn = GM_SMTP(read_secret("g_app-pass"))
                em_conn.compose(subject, payload, sender, [recipient])
                em_conn.send_email()
            return 'Message sent via: '+"".join(method), 201
        else:
            return "Invalid Method"

    app.run(host='0.0.0.0', port=88)

if __name__ == "__main__":
    main()
