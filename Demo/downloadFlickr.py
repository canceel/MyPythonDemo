import requests,bs4,os
from bs4 import BeautifulSoup

baseUrl="http://www.flickr.com"
url="http://www.flickr.com/photos/dorinser/13545844805/in/photolist-mCZZJn-9bLLEJ-9XLrR4-bpnxfN-qYAD3D-e6u5Ej-b2ygdF-fZh6UW-abGk8F-7b4y4a-oztsCu-8HhZTe-7c8PDh-4HauQG-b5gHki-fZgT9e-8MzgVR-djzdH3-25z9JjK-5QQL1U-84219z-qJc99b-dxTfvt-ifAkvP-mju1Ce-4BignY-brLwjq-dGHvJj-p7Eqvq-jxQLth-amNm4v-mju2S8-65ZwUn-8znjgb-RQC2yH-djzdrY-apqLdG-22NYH5r-9Dudjp-4BaaHa-bCywUs-eJVv-nLbBuK-oNcFUa-djzcqh-djzdWL-e8edEu-djzdki-Vx2zFR-oZfY1u"

os.makedirs('flickr',exist_ok=True)

res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,'html.parser')

linkElems=soup.select('.main-photo')

if linkElems==[]:
	print('None of url')
else:
	imageUrl='http:'+linkElems[0].get('src')
	print("ImageUrl------>"+str(imageUrl))
	res=requests.get(imageUrl)
	res.raise_for_status()
	imageFile=open(os.path.join('flickr',os.path.basename(imageUrl)),'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()
	#Get the prev button's url
	prevLink=soup.select('a[data-track="nextPhotoButtonClick"]')
	# 
	# prevLink=soup.find_all("href",class_=["navigate-target","navigate-next","no-outline"])
	print(str(prevLink))