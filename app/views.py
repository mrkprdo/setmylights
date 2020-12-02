from . import app
from flask import render_template, send_from_directory


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/farbtastic.css')
# def farbcss():
#     return send_from_directory('farbtastic.css')

# @app.route('/farbtastic.js')
# def farbjs():
#     return send_from_directory('farbtastic.js')