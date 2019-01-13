from flask import Flask, jsonify, request
from PIL import Image
import requests
import base64
from io import BytesIO
import json

app = Flask(__name__)
image_base64 = ''

#add a constant with ngrok urls as a dictionary and use that to decide 'temp'
def connect_device(x, y, uniq_id):
	data = urllib.urlencode({'x': x, 'y': y, 'uniq_id': uniq_id})
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	h.request('POST', 'temp', data, headers)
	r = h.getresponse()
	return r

@app.route('/')
def root():
	return 'Backend for Remote Devices'

@app.route('/get_coordinates', methods=['POST'])
def get_coordinates():
	data = json.loads(request.data.decode('utf-8'))
	base64 = connect_device(data['coordinates'][0], data['coordinates'][1], data['uniq_id'])
	return base64


# @app.route('/receive_screenshot', methods=['POST'])
# def receive_screenshot():
# 	# print(type(request.files['screenshot']))
# 	img = Image.open(request.files['screenshot'])
# 	# img.show()

# 	buffered = BytesIO()
# 	img.save(buffered, format="JPEG")
# 	global image_base64
# 	image_base64 = base64.b64encode(buffered.getvalue())

# 	return jsonify({"Status": "Received Image"})

# 	 # use some vision API?  https://stackoverflow.com/questions/47511021/passing-image-data-to-flask-server
# 	 # img = cv2.imread(data)
# 	 # fact_resp= model.predict(img)

# @app.route('/get_base64', methods=['GET'])
# def get_base64():
# 	# img = screenshot_data['screenshot']
# 	# print(type(img))

# 	return jsonify({"base64": image_base64.decode('utf-8')}) #image_base64 # json.dumps(image_base64)

if __name__ == "__main__":
    app.run(debug=True)
