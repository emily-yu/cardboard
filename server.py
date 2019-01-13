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
from phoneshortcuts import PhoneShortCuts

app = Flask(__name__)

@app.route('/')
def root():
    return '/screenshot pls'

@app.route('/screenshot', methods=['POST'])
def screenshot():
    #CHANGE THIS ON EACH COMP LATER
    my_id = '2'
    data = json.loads(request.data.decode('utf-8'))
    x = data['x']
    y = data['y']
    uniq_id = data['uniq_id']
    print (uniq_id, x, y)
    if(uniq_id == '3'):
        print ("The actual fuck")
        same = PhoneShortCuts()
        same.touch(x, y)
        same.home()
        return jsonify({"same":"same"})
    elif(uniq_id == '1'):
        # this clicks
        m = PyMouse()
        x_dim, y_dim = m.screen_size()
        m.click(x_dim * x, y_dim * y)

        #this gets image into base64
        img = ImageGrab.grab()
        img.save('screenshot.png')
        time.sleep(0.2)

        buffered = BytesIO()
        img.save(buffered, format="PNG")
        image_base64 = base64.b64encode(buffered.getvalue())

        payload = {"base64": image_base64.decode('utf-8')}
        return jsonify(payload)
    else:
        return jsonify({"somethingr ealy ufkced up happened":"lol"})


if __name__ == "__main__":
    app.run(port=8000, debug=True)
