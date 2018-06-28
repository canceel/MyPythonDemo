import threading,time
from time import sleep

print("Start of program")


def takeANap():
	time.sleep(5)
	print('wake up!')

threadObj=threading.Thread(target=takeANap)

threadObj.start()

print('End of program')


print('Start range')

def fun1():
	for i in range(5):
		sleep(3)
		print("fun1 "+str(i))

def fun2():
	for i in range(5):
		sleep(3)
		print('fun2 '+str(i))

thread1=threading.Thread(target=fun1)
thread2=threading.Thread(target=fun2)

thread1.start()
thread2. start()


print("Start demo2")

def funPrint(values):
	for i in values:
		print(str(i))

thread3=threading.Thread(target=funPrint,args=['a','b','c'],kwargs={'sep','a'})
thread3.start()

print("End demo2")