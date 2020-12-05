from . import app
from flask import render_template, send_from_directory, request, redirect, url_for, jsonify
import string

def read():
    with open('color_state','r') as ff:
        return ff.read()

def save(color):
    #data sanitation
    check_hex = [n in string.hexdigits for n in color[1:6]]
    if len(color) == 7 and color[0] == '#' and all(check_hex):
        with open('color_state','w+') as ff:
            ff.write(color)

@app.route('/')
def index():
    COLOR_STATE = read()
    return render_template('index.html',hexcolor=COLOR_STATE)

@app.route('/set', methods=['POST'])
def set_value():
    data = request.form.to_dict(flat=False)
    save(data['color'][0])
    COLOR_STATE = read()
    return render_template('index.html',hexcolor=COLOR_STATE)

@app.route('/get', methods=['GET'])
def get_value():
    COLOR_STATE = read()
    hex_color = COLOR_STATE.lstrip('#')
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    data = {
        'hex_color':COLOR_STATE,
        'rgb_color':rgb_color
    }
    return jsonify(data)

# @app.route('/farbtastic.css')
# def farbcss():
#     return send_from_directory('farbtastic.css')

# @app.route('/farbtastic.js')
# def farbjs():
#     return send_from_directory('farbtastic.js')