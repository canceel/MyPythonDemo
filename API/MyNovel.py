#小说搜索下载 百度搜索
#http://zhannei.baidu.com/cse/search?s=5541116575338011306&p=0&q=

import requests,os,json,sys
from bs4 import BeautifulSoup

searchUrl="http://zhannei.baidu.com/cse/search?s=5541116575338011306&p=%s&q=%s"

booksBaseUrl="http://www.apporapp.cc"

print("输入你要查的小说:")

booksName=input()

page=0

class Book(object):
	"""docstring for Book"""
	def __init__(self, name,author,linkUrl):
		super(Book, self).__init__()
		self.name = name
		self.author = author
		self.linkUrl = linkUrl
		

#查找图书方法
def getBooksInfo(page,booksName):
	url=searchUrl%(str(page),str(booksName))
	data=parserSearchResponse(getResponse(url))
	return data

#根据请求地址,获取返回信息
def getResponse(url):
	print("Request Url is "+url)

	response=requests.get(url)

	response.raise_for_status()

	response.encoding = 'utf-8'

	return response


#解析搜索返回的数据
def parserSearchResponse(response):
	
	soup=BeautifulSoup(response.text,'html.parser')
	#获取书名与链接信息
	resultList=soup.select('a[cpos="title"]')
	#书本相关信息
	bookInfos=soup.select('.result-game-item-info')
	#存储书本信息
	bookList=[]

	for i in range(0,len(resultList)):
		author=bookInfos[i].select('.result-game-item-info-tag span')[1].get_text().strip()
		bookName=resultList[i].get('title')
		bookUrl=resultList[i].get('href')
		book=Book(bookName,author,bookUrl)
		bookList.append(book)
		# print("BookName is %s author is %s and url is %s"%(bookName,author,bookUrl))
	return bookList
		
	# for resultItem in resultList:
	# 	bookName=resultItem.get('title')
	# 	bookUrl=resultItem.get('href')
	# 	print("BookName is %s and url is %s"%(bookName,bookUrl))

books=getBooksInfo(page,booksName)

# print("current page is %s, total size is "+str(len(books)))

#打印返回的信息
position=0
for book in books:
	print("Position is %s name is %s author s %s linkUrl is %s"%(str(position),book.name,book.author,book.linkUrl))
	position+=1


# TODO 验证输入，判断边界
while True:
	print('input position to download:')
	downloadPosition=input()
	#退出
	if downloadPosition=="exit":
		sys.exit()
	#是否为数字
	if downloadPosition.isdigit():
		if int(downloadPosition)>=0 and int(downloadPosition)<len(books):
			print('OK')
			break
		else:
			print('大于0小于%s'%(str(len(books)-1)))
	else:
		print('input type must be int,please try again')
		
url=books[int(downloadPosition)].linkUrl

print("url is %s"%(url))
#根据选择地址获取数据
response=getResponse(url)
#
jsonData=json.dumps(response.text)
status_=jsonData[""]



# def downlload():
# 	pass
