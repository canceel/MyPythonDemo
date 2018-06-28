import requests,bs4,os,time,threading
from bs4 import BeautifulSoup

startTime=time.time()
print("Start time "+str(startTime))

baseUrl='https://xkcd.com/'
os.makedirs('xkcd',exist_ok=True)
pageNum=1

def downloadXkcd(startComic,endComic):
	for urlNum in range(startComic,endComic):
		#download Page
		# print("Downloading page %s..."%(baseUrl)+urlNum)
		url=baseUrl+str(urlNum)
		res=requests.get(url)
		res.raise_for_status()
		soup=BeautifulSoup(res.text,'html.parser')
		#Find the url of the comic mage
		comicElement=soup.select('#comic img')
		if comicElement==[]:
			print("Page%s URL is %s,comicUrl is not found"%(str(pageNum),url))
		else:
			ComicUrl='http:'+comicElement[0].get('src')
			print("Page%s URL is %s,comicUrl is %s"%(str(pageNum),url,ComicUrl))
			#Download the image
			res=requests.get(ComicUrl)
			res.raise_for_status()
			#Save the image to ./xkcd
			imageFile=open(os.path.join('xkcd',os.path.basename(ComicUrl)),'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()

downloadThreads=[]

for i in range(1,2011,30):
	downloadThread=threading.Thread(target=downloadXkcd,args=(i,i+99))
	downloadThreads.append(downloadThread)
	downloadThread.start()


for downloadThread in downloadThreads:
	downloadThread.join()
		
endTime=time.time()
print("End time "+str(endTime))

print("Spend Time "+str(endTime-startTime))

print('Done.')