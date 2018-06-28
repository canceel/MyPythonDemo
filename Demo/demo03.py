from bs4 import BeautifulSoup
import requests

url='https://www.imooc.com/'

res=requests.get(url)

soup=BeautifulSoup(res.text,'html.parser')

linksss=soup.find_all("div",class_=["1","banner-course-card"])

print(str(linksss))