# TODO 抓取腾讯漫画，下载下来界面数据没有加载出，待完成
import os
import requests
from bs4 import BeautifulSoup

baseUrl = "http://ac.qq.com"
url = "http://ac.qq.com/ComicView/index/id/530132/cid/3"

#<a id="nextChapter" href="/ComicView/index/id/530132/cid/4?fromPrev=1">                    <span class="iconfont icon-btnright">&nbsp;</span> <span class="tool_title">下一话</span></a>

res = requests.get(url)
res.raise_for_status()
#save page to ../tencent

pageFile=open(os.path.join('tencent',os.path.basename(url)),'wb')
for chunk in res.iter_content(100000):
	pageFile.write(chunk)
pageFile.close()


soup=BeautifulSoup(res.text,'html.parser')
ComicElem=soup.select('#comicContain')

print(ComicElem)


prvLink=soup.select("#nextChapter")[0].get('href')

print("PrvLink :"+prvLink)

