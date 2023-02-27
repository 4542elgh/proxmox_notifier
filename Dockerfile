FROM python:3.11.2-alpine3.16

RUN pip install flask discordwebhook

WORKDIR ./app

COPY main.py discord_notify.py email_notify.py ./

CMD python -u main.py
