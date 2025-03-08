from flask import Flask, request
import os

from discordwebhook import Discord

def main():
    app = Flask(__name__)

    @app.route('/send', methods = ['POST'])
    def send():
        if request.method == "POST":
            try:
                payload = request.form["payload"]
                channel = request.form["channel"]
            except KeyError:
                return 'payload/channel not provided', 400

            dc_keys = {k: v for k, v in dict(os.environ).items() if "_dc" in k}

            if channel+"_dc" in dc_keys.keys():
                discord = Discord(url = dc_keys[channel+"_dc"])
                discord.post(content = payload)
                return "Notification sent to Discord channel", 200
            else:
                return "Invalid Method", 400
        else:
            return "Invalid Method"

    app.run(host='0.0.0.0', port=88)

if __name__ == "__main__":
    main()
