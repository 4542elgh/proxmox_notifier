FROM python:3.11.2-bullseye

RUN apt update -y && apt dist-upgrade -y
RUN pip install flask discordwebhook

WORKDIR ./app

COPY main.py discord_notify.py email_notify.py ./

CMD python -u main.py
