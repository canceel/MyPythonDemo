from flask import Flask,render_template,make_response,request
import json
from weather import *
from MyNovel import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_tasks():
    return "jsonify({'tasks': tasks})"

@app.route('/getWeather',methods=['GET'])
def weather():
	if request=="":
		result="request must not null"
	else:
		location=request.args.get('location')
		if location=="[]":
			result="location is must not null"
		else:
			result=getWeather(location)
	return str(result)

@app.route('/getNovel',methods=['GET'])
def novel():
	if request=="":
		result="request must not null"
	else:
		keyworld=request.args.get('keyworld')
		result=getBooksInfo(0,keyworld)
	return json.dumps(str(result.data))

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)