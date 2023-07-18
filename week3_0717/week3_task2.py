import urllib.request as req
import bs4

def getPage(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    return bs4.BeautifulSoup(data,"html.parser")

def getDataAndWrite(url):
    pageContent = getPage(url)
    titleSections = pageContent.find_all("div",class_="r-ent")
    nextLink = "https://www.ptt.cc"+pageContent.find("a",string="‹ 上頁")["href"]
    with open("movie.txt",mode="a",encoding='utf-8') as file:
        for titleSection in titleSections:
            #get data
            tweetNum = titleSection.find("div",class_="nrec").string if titleSection.find("div",class_="nrec").contents!=[] else "0"
            title = titleSection.find("div",class_="title").a.string
            link = "https://www.ptt.cc"+titleSection.find("div",class_="title").a["href"]
            time = getPage(link).find_all("span",class_="article-meta-value")[3].string
            #write data into txt file
            file.write("{},{},{}\n".format(title,tweetNum,time))
    
    return nextLink


url="https://www.ptt.cc/bbs/movie/index.html"
pageCount=0
while pageCount<3:
    url = getDataAndWrite(url)
    pageCount+=1

print("Done")