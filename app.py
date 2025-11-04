# https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html#walkthrough-of-the-presidents-app

from flask import Flask, render_template
from configparser import ConfigParser
import requests

CONFIG_PATH = './config/keys_config.cfg'

# app is an instance of a Python class named Flask
app = Flask(__name__)


# ================================================
# Presidents
# the decorator, @app.route(), modifies the function that follows it
@app.route('/user/<name>')
def user(name):
    link = '<p><a href="/Sydney">Click me for Sydney weather!</a></p>'
    return render_template('hello.html', name=name, phone="0490553150")

# ================================================
# Weather api testing
config = ConfigParser()
config.read(CONFIG_PATH)
API_KEY = config.get('weatherapi', 'api_key')
API_URL = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={{}}'

def query_api(location):
    try:
        data = requests.get(API_URL.format(location)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data

@app.route('/weather/<location>')
def weather(location):
    response = query_api(location)
    try:
        text = response["location"]["name"] + "'s temperature is " + str(response["current"]["temp_c"]) + " degrees"
    except:
        text = "There was an error. Did you include a valid location?"
    return text

# ================================================
# Creates web server when running the python script
if __name__ == '__main__':
    app.run(debug=True)