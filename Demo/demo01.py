import logging

logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug('start program')

def factorial(n):
	logging.debug('start of factorial(%s%%)'%(n))
	total=1
	for i in range(n+1):
		total*=i
		logging.info('i is '+str(i)+',total is '+str(total))
	logging.debug('End of factorial(%s%%'%(n))
	return total

print(factorial(5))
logging.debug('End of program')