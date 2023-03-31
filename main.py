from flask import Flask, request

from email_notify import GM_SMTP
from discord_notify import DC_Webhook

import os
import json

def read_secret(name):
    f = open(os.path.join("/run/secrets", name))
    return json.load(f)

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
                channel = request.form["channel"]
            except KeyError:
                return 'Method and/or payload not provided', 400

            method = method.split(",")

            if "discord" in method:
                dc_keys = read_secret("dc_webhook-pass")
                if channel+"_dc" in dc_keys.keys():
                    dc_conn = DC_Webhook(dc_keys[channel+"_dc"])
                    dc_conn.send(payload)
                else:
                    return "Invalid Method"
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
