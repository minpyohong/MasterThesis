import bs4

html_str =  """
            <html>
                <body>
                   <ul class="greet">
                        <li>hello</li>
                        <li>bye</li>
                        <li>welcome</li>
                   </ul>
                   <ul class="reply">
                        <li>ok</li>
                        <li>no</li>
                        <li>sure</li>
                   </ul>
                 </body>
            </html>
            """

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")

ul = bs_obj.find("ul",{"class":"reply"})

print(ul)

html_str1 =  """
            <html>
                <body>
                   <ul class="ko">
                        <li>
                            <a href="https://www.naver.com/">네이버</a>
                        </li>
                        <li>
                            <a href="https://www.daum.net/">다음</a>
                        </li>
                   </ul>
                   <ul class="sns">
                        <li>
                            <a href="https://www.google.com/">구글</a>
                        </li>
                        <li>
                            <a href="https://www.facebook.com/">페이스북</a>
                        </li>
                   </ul>
                 </body>
            </html>
            """


bs_obj1 = bs4.BeautifulSoup(html_str1,"html.parser")
atag = bs_obj1.find("a")

print(atag)

print(atag["href"])


