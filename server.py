# load additional Python module
from flask import Flask, jsonify, request
import requests
import socket
import websockets
import asyncio
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import pyscreenshot as ImageGrab
from PIL import Image
import base64
from io import BytesIO
import json

app = Flask(__name__)

@app.route('/')
def root():
    return '/screenshot pls'

@app.route('/screenshot', methods=['POST'])
def screenshot():
    #CHANGE THIS ON UR COMP LATER
    my_id = '0'
    data = request.data
    x = data['x']
    y = data['y']
    uniq_id = data['uniq_id']

    if(my_id != uniq_id):
        return "lmao"

    # this clicks
    m = PyMouse()
    x_dim, y_dim = m.screen_size()
    m.click(x_dim * floatx, y_dim * float(y))

    #this gets image into base64
    img = ImageGrab.grab()
    img.save('screenshot.png')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    image_base64 = base64.b64encode(buffered.getvalue())

    payload = {"base64": image_base64.decode('utf-8')}
    return payload

if __name__ == "__main__":
    app.run(port=8000, debug=True)
