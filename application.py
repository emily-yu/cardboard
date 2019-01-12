from flask import Flask, jsonify, request
from PIL import Image
import requests
import base64
from io import BytesIO
import json

application = Flask(__name__)
image_base64 = ''

@application.route('/')
def root():
	return 'Backend for Remote Devices'

@application.route('/receive_screenshot', methods=['POST'])
def receive_screenshot():
	# print(type(request.files['screenshot']))
	# print(request.json)
	img = Image.open(request.files['screenshot'])
	# img.show()	

	buffered = BytesIO()
	img.save(buffered, format="JPEG")
	global image_base64
	image_base64 = base64.b64encode(buffered.getvalue())
	
	return jsonify({"Status": "Received Image"})

	 # use some vision API?  https://stackoverflow.com/questions/47511021/passing-image-data-to-flask-server
	 # img = cv2.imread(data)
	 # fact_resp= model.predict(img)

@application.route('/get_base64', methods=['GET'])
def get_base64():
	# img = screenshot_data['screenshot']
	# print(type(img))

	return jsonify({"base64": image_base64.decode('utf-8')}) #image_base64 # json.dumps(image_base64) 

if __name__ == "__main__":  
    application.run(debug=True)