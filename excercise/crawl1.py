from urllib.request import urlopen

url = "https://www.coindesk.com/"

url = "https://www.coindeskkorea.com"

url = "https://www.blockmedia.co.kr/"

url = "https://www.decenter.kr/"


html = urlopen(url)

print(html.read( ))

## error 발생시 참고 url : https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org

# sudo /Applications/Python\ 3.7/Install\ Certificates.command ; exit;  직접 console로 들어가서 typing