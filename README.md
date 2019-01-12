# Cardboard-Service

## Endpoints

> Post: raspberry pi sends screenshot
- `/receive_screenshot`

> Get: returns base64 conversion 
- `/get_base64/`

Set up 

1. activate env: `source virtual-env/bin/activate`
1. startup backend: `python application.py`
1. localhost webhook: `./ngrok http 5000` 
1. Test
	- `curl -F "screenshot=@ipad_image.jpg" http://localhost:5000/receive_screenshot`
	- `curl -F "screenshot=@ipad_image.jpg" http://remote-device-service.xagtw3nxx2.us-west-1.elasticbeanstalk.com//receive_screenshot`

---

To do
1. [Figure out how to update deployment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html)
	- `eb config` & `subl .elasticbeanstalk` to make sure configs are set to right environments
	- `eb create some-env`, `eb open`
	- https://us-west-1.console.aws.amazon.com/elasticbeanstalk 
1. Set up Identity and Access Management [(IAM) users](https://console.aws.amazon.com/iam/home?region=us-west-1#/security_credential)
1. [Full stack web deployment demo](https://medium.freecodecamp.org/lessons-learned-from-deploying-my-first-full-stack-web-application-34f94ec0a286)

[Deploying flask app to AWS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)
1. Establish dependencies `pip freeze > requirements.txt`
1. Create env with `virtualenv virtual-env` 
1. [AWS Access key](https://help.bittitan.com/hc/en-us/articles/115008255268-How-do-I-find-my-AWS-Access-Key-and-Secret-Access-Key-)
1. `eb init -p python-3.6 remote-device-backend --region us-west-1`


Your identification has been saved in /Users/mdong/.ssh/aws-eb.
Your public key has been saved in /Users/mdong/.ssh/aws-eb.pub.
The key fingerprint is:
SHA256:0Zfg9aDundOHF/A8COuBYR4hy0Y63z/FPB1N0qilWp8 aws-eb



