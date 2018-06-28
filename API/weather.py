import requests,json


defaultLanguage="zh_cn"

APIKEYS="f20341d7259c0d4140ca5bdc2d9c8e42"

weatherApi="http://api.openweathermap.org/data/2.5/weather?q=%s&lang=%s&APPID=%s"


def getWeather(location):
	if location=="":
		print("Pleaese input location")
	else:
		url=weatherApi%(location,defaultLanguage,APIKEYS)
		print("request Url is:"+url)
		#请求网络
		response=requests.get(url)
		response.raise_for_status()

		weatherJsonData=json.loads(response.text)

		# w=weatherJsonData['weather'][0]['main']+"-"+weatherJsonData['weather'][0]['description']
		# print(w)
		# w=weatherJsonData['weather'][0]
		# result=w['main']+"---"+w['description']
		# print(result)

		return weatherJsonData

getWeather('beijing')
