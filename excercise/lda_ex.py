import pandas as pd
import urllib.request

urllib.request.urlretrieve("https://raw.githubusercontent.com/franciscadias/data/master/abcnews-date-text.csv", filename="abcnews-date-text.csv")
data = pd.read_csv("abcnews-date-text.csv",error_bad_lines=False)

print(len(data))