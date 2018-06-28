import requests,bs4,os,time
from bs4 import BeautifulSoup

startTime=time.time()
print("Start time "+str(startTime))

baseUrl='https://xkcd.com'
url='https://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
pageNum=1

while not url.endswith('#'):
	#Download the page
	res=requests.get(url)
	res.raise_for_status()
	soup=BeautifulSoup(res.text,'html.parser')
	#Find The URL of the comic image
	ComicElem=soup.select('#comic img')
	if ComicElem==[]:
		print("Page%s URL is %s,comicUrl is not found"%(str(pageNum),url))
		break
	else:
		ComicUrl='http:'+ComicElem[0].get('src')
		print("Page%s URL is %s,comicUrl is %s"%(str(pageNum),url,ComicUrl))
		#Download the image
		res=requests.get(ComicUrl)
		res.raise_for_status()
		#Save the image to ./xkcd
		imageFile=open(os.path.join('xkcd',os.path.basename(ComicUrl)),'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
		#Get the prev button's url
		PrevLink=soup.select('a[rel="prev"]')[0]
		url=baseUrl+PrevLink.get('href')
	pageNum+=1


endTime=time.time()
print("End time "+str(endTime))

print("Spend Time "+str(endTime-startTime))

print('Done.')