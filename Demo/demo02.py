#Search From Google and open top5 Links

import webbrowser
import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug('start program')

print('input keyworld:')

keyworld = input()

print('keyworld is ' + str(keyworld))
print('start search from google ....')

res = requests.get('https://www.google.com.hk/search?&q='+keyworld)

res.raise_for_status()

soup=BeautifulSoup(res.text,'html.parser')


linkElems=soup.select('.r a')

numOpen=min(5,len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com'+linkElems[i].get('href'))
	logging.debug(str(linkElems))
