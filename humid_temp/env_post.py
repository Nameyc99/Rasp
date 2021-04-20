import requests as rq
import json 
import Adafruit_DHT
from datetime import datetime
import time
import getpass
import ast
import json


sensorId = getpass.getuser()
sensor = Adafruit_DHT.DHT11

GPIO = 14



while True:
	seconds = 600
	current = int(time.time())
	while True:
		created = datetime.today()
		created_str = created.strftime("%Y/%m/%d %H:%M:%S")
		print(created_str)
		timer = int(time.time())
		humidity, temperature = Adafruit_DHT.read_retry(sensor,GPIO)
		data = {
			"value" : humidity,
			"sensorId" : sensorId,
			"created" : created_str,
			}
		print(data)
		with open("log.json","r+") as jfile :
			try :
				datas = json.load(jfile)
				if type(datas) is dict :
					datas = [datas]
				datas.append(data)
				jfile.seek(0)
				json.dump(datas,jfile)
			except:
				json.dump(data,jfile)
		if timer >= current + seconds:
			break
		time.sleep(10)
	
	files = open("log.json","r")
	data = json.load(files)
	if type(data) is dict:
		url = "http://140.117.71.98:8000/api/humidity/"
		res = rq.post(url,data)
		print(res)
	else :
		for datas in data :
			url = "http://140.117.71.98:8000/api/humidity/"
			res = rq.post(url,datas)
			print(res)
	files.close()

	files = open("log.json","r+")
	files.truncate(0)
	files.close()