from discordwebhook import Discord

class DC_Webhook:
    def __init__(self, webhookurl):
        self.discord = Discord(url=webhookurl)
    def send(self, payload):
        self.discord.post(content=payload)
