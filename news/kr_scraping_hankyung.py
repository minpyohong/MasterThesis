import requests
import urllib.request
import pandas as pd
import bs4
from datetime import datetime

# max_article = 100

now = datetime.now()

temp_heder = ['press company','date','title',"url","abstract","date detail","head article","main article"]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}

URL = "https://www.google.com/search?q=intitle:{query}+-라이온봇+after:{fromdate}+before:{todate}+site:{site}&tbm=nws&start={articlenum}"
row = []

outputFileName = '(KR)Hankyung %s-%s-%s %s시 %s분 %s초 result.csv' % (now.year, now.month, now.day, now.hour, now.minute, now.second)

scraping_result = pd.DataFrame(columns=temp_heder)


def run(**params):


    print(URL.format(**params))

    html = requests.get(URL.format(**params),headers=headers,allow_redirects=False).content
    bs_obj = bs4.BeautifulSoup(html,"html.parser")

    div_all = bs_obj.find_all("div",{"class":"dbsr"})

    for div in div_all :

        global scraping_result # 전역변수 사용선언

        link = div.find("a")
        # title = link.find("div",{"class":"phYMDf nDgy9d"})
        title = link.find("div", {"class": "JheGif nDgy9d"})
        #abstract = link.find("div", {"class": "eYN3rb"})
        abstract = link.find("div", {"class": "Y3v8qd"})
        article_date = link.find("span", {"class": "eNg7of"})
        detail_url = link['href']


        print(detail_url)
        print(title.text)

        detail_html = requests.get(detail_url,headers=headers,allow_redirects=False).content
        bs_detail_obj = bs4.BeautifulSoup(detail_html, "html.parser")

        article_datetime =bs_detail_obj.find("span",{"class":"date-modify"})
        detail_datetime = article_datetime.find("span",{"class":"num"})

        #print("detail_datetime==",detail_datetime.text)

        bodytext = bs_detail_obj.find("div",id = "articletxt")

        #print(bodytext)
        #sentence_list = bodytext.find_all("br")


        head_sentence = bs_detail_obj.find("div",{"class":"summary editoropinions"})
        row.append(params['site'])
        row.append(article_date)
        row.append(title.text)
        row.append(detail_url)
        row.append(abstract.text)
        row.append(detail_datetime)
        row.append(head_sentence.text)
        main_article = bodytext.text

        #for setence in sentence_list :
        #    main_article += setence.text
        #    print(main_article)
        row.append(main_article)
        a_series = pd.Series(row, index=temp_heder)
        scraping_result = scraping_result.append(a_series,ignore_index=True)
        row.clear()


    next_url = bs_obj.find_all("a",{"class":"G0iuSb"})
    #print("next url = ",next_url[next_url.__len__()-1].text)

    if not next_url :
        breakflag = "break"
    elif next_url[next_url.__len__()-1].text =="이전" :
        breakflag = "break"
    else :
        breakflag = "continue"

    return breakflag

scraping_site = 'https://www.hankyung.com/'
keyword = "비트코인"
p = 0
while True :
    #breakflag = run(query=keyword,fromdate="2017-3-19", todate= '2017-6-20', site= scraping_site ,articlenum=p)
    #breakflag = run(query=keyword, fromdate="2017-9-15", todate='2017-12-26', site=scraping_site, articlenum=p)
    #breakflag = run(query=keyword, fromdate="2018-1-7", todate='2018-2-5', site=scraping_site, articlenum=p)
    #breakflag = run(query=keyword, fromdate="2018-9-9", todate='2018-11-18', site=scraping_site, articlenum=p)
    #breakflag = run(query=keyword, fromdate="2018-11-19", todate='2018-12-14', site=scraping_site, articlenum=p)
    #breakflag = run(query=keyword, fromdate="2019-4-2", todate='2019-6-26', site=scraping_site, articlenum=p)
    #breakflag = run(query=keyword, fromdate="2019-7-31", todate="2019-8-8", site=scraping_site, articlenum=p)
    #breakflag = run(query=keyword, fromdate="2019-10-25", todate="2019-10-27", site=scraping_site, articlenum=p)
    #breakflag = run(query=keyword, fromdate="2019-7-10", todate="2019-7-16", site=scraping_site, articlenum=p)
    #breakflag = run(query=keyword, fromdate="2019-8-10", todate="2019-8-14", site=scraping_site, articlenum=p)
    #breakflag = run(query=keyword, fromdate="2019-9-23", todate="2019-9-26", site=scraping_site, articlenum=p)
    #breakflag = run(query=keyword, fromdate="2019-11-8", todate="2019-11-24", site=scraping_site, articlenum=p)
    #breakflag = run(query=keyword, fromdate="2020-1-3", todate="2020-2-11", site=scraping_site, articlenum=p)
    #breakflag = run(query=keyword, fromdate="2020-3-8", todate="2020-3-30", site=scraping_site, articlenum=p)
    #breakflag = run(query="비트코인",fromdate="2018-12-20", todate= '2018-12-27', site= 'https://www.hankyung.com/' ,articlenum=p)
    #breakflag = run(query=keyword, fromdate="2020-4-21", todate="2020-5-7", site=scraping_site, articlenum=p)  # 2020 up 2
    breakflag = run(query=keyword, fromdate = "2020-5-8", todate = "2020-5-11", site=scraping_site, articlenum=p)  # 2020 up 2


    if breakflag == "break" :
        break
    p +=10

# print(scraping_result)
scraping_result.to_csv('./scraping_result/kr/'+outputFileName,sep=',')