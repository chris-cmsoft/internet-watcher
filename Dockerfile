FROM python:3.7

ENV PYTHONUNBUFFERED=TRUE
RUN mkdir -p /opt/internet-watcher
WORKDIR /opt/internet-watcher

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./watcher ./watcher

EXPOSE 8005

CMD  ["python3","./watcher/main.py"]