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

URL = "https://www.google.com/search?q={query}+after:{fromdate}+before:{todate}+site:{site}&tbm=nws&hl=en&lr=lang_en&start={articlenum}"
row = []

outputFileName = 'NYtimes %s-%s-%s %s시 %s분 %s초 result.csv' % (now.year, now.month, now.day, now.hour, now.minute, now.second)

scraping_result = pd.DataFrame(columns=temp_heder)


def run(**params):


    print(URL.format(**params))

    html = requests.get(URL.format(**params),headers=headers,allow_redirects=False).content
    bs_obj = bs4.BeautifulSoup(html,"html.parser")

    div_all = bs_obj.find_all("div",{"class":"dbsr"})

    for div in div_all :

        global scraping_result # 전역변수 사용선언

        link = div.find("a")
        title = link.find("div",{"class":"phYMDf nDgy9d"})
        abstract = link.find("div", {"class": "eYN3rb"})
        article_date = link.find("span", {"class": "eNg7of"})
        detail_url = link['href']
        row.append(params['site'])
        row.append(article_date.text)
        row.append(title.text)
        row.append(detail_url)
        row.append(abstract.text)



        detail_html = requests.get(detail_url,headers=headers,allow_redirects=False).content
        bs_detail_obj = bs4.BeautifulSoup(detail_html, "html.parser")

        print(detail_url)

        article_datetime =bs_detail_obj.find("li",{"class":"css-i49r68"})

        print(article_datetime)
        if not article_datetime :
            detail_datetime = article_date
        else :
            detail_datetime = article_datetime.find("time", {"class": "css-129k401 e16638kd0"})



        bodytext = bs_detail_obj.find("section",{"name":"articleBody"})
        print(detail_datetime.text)

        sentence_list = bodytext.find_all("p")
        head_sentence = (lambda x : title if not x else x)(bs_detail_obj.find("div",{"class":"css-1a48zt4 ehw59r15"}))
        row.append(detail_datetime.text)
        row.append(head_sentence.text)
        main_article = ""

        for setence in sentence_list :
            main_article += setence.text

        row.append(main_article)
        a_series = pd.Series(row, index=temp_heder)
        scraping_result = scraping_result.append(a_series,ignore_index=True)
        row.clear()


    next_url = bs_obj.find_all("a",{"class":"G0iuSb"})
    #print("next url = ",next_url[next_url.__len__()-1].text)

    if not next_url :
        breakflag = "break"
    elif next_url[next_url.__len__()-1].text =="Previous" :
        breakflag = "break"
    else :
        breakflag = "continue"

    return breakflag

p = 0

while True :
    breakflag = run(query="BitCoin",fromdate="2017-3-19", todate= '2017-6-20', site= 'https://www.nytimes.com/' ,articlenum=p)
    if breakflag == "break" :
        break
    p +=10

#print(scraping_result)
scraping_result.to_csv('./scraping_result/'+outputFileName,sep=',')