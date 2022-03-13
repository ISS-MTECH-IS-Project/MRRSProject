from flask import Flask
from flask import render_template
from conversation import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/greeting')
def greeting():
    covControl = Conversation()
    return covControl.getGreeting()