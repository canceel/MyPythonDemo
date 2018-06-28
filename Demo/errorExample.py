from Demo01.removePackage import *

print(__name__)
aa()
bb()


def methodFun(mony,day):
	if int(day)<28:
		return 0
	else:
		total=int(mony)*(0.085-0.042)/365*28+int(day)*0.042/365*int(mony) 
		return total


print('input day,day must more than the 28,else total is 0')
day=input()
print('input mony')
mony=input()

result=methodFun(mony,day)

print('total result is '+str(result))