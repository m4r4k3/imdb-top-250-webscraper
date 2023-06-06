from bs4 import BeautifulSoup 
import requests
ans = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
soup = BeautifulSoup( ans.text, "lxml")
data = soup.select(".lister-list tr .titleColumn a")
for i in data :
    print(i.text)

     