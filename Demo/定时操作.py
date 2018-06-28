import datetime
from time import sleep


sleepTime=datetime.datetime(2018, 6, 27, 18, 12, 36, 000000)

while datetime.datetime.now()<sleepTime:
	sleep(1)
	print("sleep")



print("NoewTime:%s > sleepTime:%s stop sleep"%(datetime.datetime.now(),sleepTime))