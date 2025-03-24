import flask
from flask import render_template, send_from_directory

from challenge import app, forms


@app.route('/', methods=['GET'])
def index() -> str:
    return render_template("index.html")

@app.route('/image', methods=['GET'])
def ch1():
    return send_from_directory('static', 'will_steg.dmg', as_attachment=True)

@app.route('/DaveIsAGoatedWebmaster', methods=['GET'])
def step1():
    return render_template("step1.html")

@app.route('/DaveIsAGoatedWebmaster/percy2.bmp', methods=['GET'])
def step2():
    return send_from_directory('static', 'percy2.bmp')

@app.route('/crypto', methods=['GET'])
def ch2():
    return send_from_directory('static','skeleton.py')

@app.route('/bob.jpg', methods=['GET'])
def bob():
    return send_from_directory('static','bob.jpg')

@app.route('/gru.jpg', methods=['GET'])
def gru():
    return send_from_directory('static','gru.jpg')