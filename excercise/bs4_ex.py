import bs4

html_str = "<html><div>hello</div></html>"

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")

print(type(bs_obj))
print(bs_obj)
print(bs_obj.find("div"))  # div 영역만 추출


html_str1 = """
            <html>
                <body>
                   <ul>
                        <li>hello</li>
                        <li>bye</li>
                        <li>welcome</li>
                   </ul>
                 </body>
            </html>
            """
#print(html_str1)

bs_obj1 = bs4.BeautifulSoup(html_str1,"html.parser")

ul = bs_obj1.find("ul")
li = ul.find("li")

print(li)

lis = ul.findAll("li") # list 형태로 return

print(lis)

print(lis[1])

print(lis[1].text)

print(li.text)
