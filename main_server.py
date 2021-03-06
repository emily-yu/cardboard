from flask import Flask, jsonify, request
from PIL import Image
import requests
import base64
from io import BytesIO
import json

app = Flask(__name__)
image_base64 = ''
ngrok_urls = {
	'0':'http://b936e13e.ngrok.io',
	'1':'http://a43e7038.ngrok.io',
	'2':'http://cd816011.ngrok.io',
	'3':'http://b936e13e.ngrok.io'
}

#add a constant with ngrok urls as a dictionary and use that to decide 'temp'
def connect_device(x, y, uniq_id):
	data = {'x': x, 'y': y, 'uniq_id': uniq_id}
	url = ngrok_urls[uniq_id] + '/screenshot'
	jdata = json.dumps(data)
	print (jdata, url)
	response = requests.post(url, data=jdata)
	return response.json()

@app.route('/')
def root():
	return 'Backend for Remote Devices'

@app.route('/get_coordinates', methods=['POST'])
def get_coordinates():
	data = json.loads(request.data.decode('utf-8'))
	base64 = connect_device(data['coordinates'][0], data['coordinates'][1], data['uniq_id'])
	return jsonify({"base64":base64})


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
