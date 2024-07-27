from flask import Flask, request, render_template
import requests
import psycopg2
import config
import os
import endpoints
import datetime
from init_db import init_db

def create_app():
    app = Flask(__name__)
    # init_db()
    return app
app = create_app()


def addTimestamp(dir, timestamp):
    URL = config.url + '/dataAll'
    PARAMS = {'dir':dir, 'timestamp': timestamp}
    r = requests.post(url = URL, params=PARAMS)
    print(r)
    return r.json()

def fetchData():
    date = datetime.date.today()
    URL = config.url + '/dataDate'
    PARAMS = {'date': date}
    r = requests.get(url = URL, params=PARAMS)
    print(r.json())

#Routing to Backend
@app.route('/user', methods=["GET", "POST", "DELETE"])
def userEnpoint():
    username = str(request.args.get('username'))
    password = str(request.args.get('password'))
    method = request.method
    acc = endpoints.user(username, password, method)
    return acc

@app.route('/dataAll', methods=["GET", "POST", "DELETE"])
def fetchAll():
    dir = str(request.args.get('dir'))
    timestamp = str(request.args.get('timestamp'))
    method = request.method
    acc = endpoints.dataAll(dir, timestamp, method)
    return acc

@app.route('/dataOnDate', methods=["GET"])
def fetchDataOnDate():
    date = str(request.args.get('date'))
    method = request.method
    acc = endpoints.dataOnDate(date,method)
    return acc

# Frontend Routing
@app.route('/')
def homePage():
    ct = datetime.datetime.now()
    dir = False
    addTimestamp(dir, ct)
    return render_template('index.html')

@app.route('/DataAnalysis/')
def dataPage():
    return render_template('DataAnalysis.html' )

@app.route('/Settings/')
def settingsPage():
    return render_template('Settings.html')
# if __name__ == "__main__":
#     app.run(host='0.0.0.0')