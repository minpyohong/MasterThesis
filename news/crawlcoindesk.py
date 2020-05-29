
"""
import feedparser

feed = feedparser.parse("https://www.coindesk.com/feed/")

coindesk_urls = [] #coindesk url들을 가져와서 저장시켜줄 객체

for entry in feed['entries']:
    coindesk_urls.append(entry['link']) #coindesk_url  list에  entries에 들어 있는 link 의 string들을 추가한다.


print(coindesk_urls)
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import datetime

my_url = "https://www.coindesk.com/tag/legal"

# Opening up the website, grabbing the page
uFeedOne = uReq(my_url, timeout=5)

print(uFeedOne)

page_one = uFeedOne.read()

print(page_one)

uFeedOne.close()

# html parser
page_soup1 = soup(page_one, "html.parser")

#print(page_soup1)

# grabs each publication block
containers = page_soup1.findAll("h2", {"class": "heading"} )

for contain in containers :
    print(contain)

"""
for container in containers:
  link = container.attrs['href']
  publication_date = "published on " + container.time.text
  title = container.h3.text
  description = "(CoinDesk)-- " +  container.p.text

  print("link: " + link)
  print("publication_date: " + publication_date)
  print("title: " + title)
  print("description: " + description)
  
"""