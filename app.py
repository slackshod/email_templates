
from flask import Flask
from configparser import ConfigParser

CONFIG_PATH = './config/keys_config.cfg'

# app is an instance of a Python class named Flask
app = Flask(__name__)

config = ConfigParser()
config.read(CONFIG_PATH)
API_KEY = config.get('openweather', 'api_key')

# the decorator, @app.route(), modifies the function that follows it
@app.route('/')
def hello():
    greet = '<h1>Hello, Gators!</h1>'
    link = '<p><a href="user/Albert">Click me!</a></p>'
    return greet + link

@app.route('/user/<name>')
def user(name):
    personal = f'<h1>Hello, {name}!</h1>'
    # above - the curly braces {} hold a variable; when this runs,
    # the value will replace the braces and the variable name
    instruc = '<p>Change the name in the <em>browser address bar</em> \
        and reload the page.</p>'
    return personal + instruc

# Creates web server when running the python script
if __name__ == '__main__':
    app.run(debug=True)