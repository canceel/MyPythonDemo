import time,datetime

print('按ENTER按钮开始\n输入exit退出计时')
value=input()
if value=='exit':
	exit()
print('开始')

startTime=time.time()
lastTime=startTime
rounds=1

try:
	while True:
		value=input()
		nowTime=time.time()
		print('现在时间:%s'%(datetime.datetime.fromtimestamp(nowTime)))
		lapTime=round(nowTime-lastTime,2)
		lastTime=nowTime
		print('回合%s:%s'%(rounds,lapTime))
		print('开始时间:%s 总计:%s'%(datetime.datetime.fromtimestamp(startTime),(nowTime-startTime)))
		rounds+=1
		if value=="exit":
			break

except KeyboardInterrupt:
	print('\nDone')