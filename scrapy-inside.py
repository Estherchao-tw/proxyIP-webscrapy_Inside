# 透過隨機換IP去爬inside網站的每篇文章的標題
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

pf = pd.read_csv('proxyIP.csv')
proxyIps = pf['proxyIP']
count = 0
for proxyIp in range(2):
    try:
        #隨機取得IP
        proxyIp = random.choice(proxyIps)
        print(proxyIp)
        # proxy ip 替換
        url = "https://www.inside.com.tw/"
        response = requests.get(url,proxies={'https':proxyIp ,'https': proxyIp})
        count += 1
        print(count)
        # 爬取 techorange最新文章
    
        soup = BeautifulSoup(response.text,"html.parser")
        data = soup.select("h3.post_title a")
        # print(data)
        for d in data:
            print(d['href'],d.text)

    except:
        print("ERROR")