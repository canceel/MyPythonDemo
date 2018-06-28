#小说搜索下载 百度搜索
#http://zhannei.baidu.com/cse/search?s=5541116575338011306&p=0&q=

import requests,os
from bs4 import BeautifulSoup

searchUrl="http://zhannei.baidu.com/cse/search?s=5541116575338011306&p=0&q=%s"

booksBaseUrl="http://www.apporapp.cc"

print("输入你要查的小说:")

keyworld=input()

url=searchUrl%(str(keyworld))

response=requests.get(url)

response.raise_for_status()

response.encoding = 'utf-8'

soup=BeautifulSoup(response.text,'html.parser')

resultList=soup.select('a[cpos="title"]')

booksInfo=[]
for resultItem in resultList:
	bookName=resultItem.get('title')
	bookUrl=resultItem.get('href')
	print("BookName is %s and url is %s"%(bookName,bookUrl))