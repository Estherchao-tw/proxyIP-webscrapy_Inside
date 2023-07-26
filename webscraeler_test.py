import requests
from bs4 import BeautifulSoup

url = "https://www.inside.com.tw/"
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text,"html.parser")
data = soup.select("h3.post_title a")
print(data)
for d in data:
    print(d['href'],d.text)