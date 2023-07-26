import requests
import re
import time
import pandas as pd
start = time.time()


url = "https://www.sslproxies.org/"
response = requests.get(url)
# print(response.text)

# re(正規表達式)模組(Module)，透過定義規則(Rule)來爬取SSL Proxy IP
# proxy ex = 178.33.3.163:8080
#「\d+」代表數字一個位數以上
proxy_ips = re.findall('\d+\.\d+\.\d+\.\d+:\d+',response.text)
print(proxy_ips)


#驗證
valid_ips = []
count = 0 
for ip in proxy_ips:
    try:
                
        result = requests.get("https://api.ipify.org?format=json",proxies={"https": ip,'http':ip},timeout=5)
        print('My public IP address is: {}'.format(ip))
        valid_ips.append(ip)
        count+= 1
        print(count)

    except:
        print("error: {} invalid.".format(ip))

#append就會想到extend方法，他們兩個很像都是將資料加在串列最後面，不同處在於append方法的參數可以是元素也能是串列，它會把串列當成一個元素放進去


df = pd.DataFrame(valid_ips,columns=['proxyIP' ])
df.to_csv('proxyIP.csv',encoding='utf-8-sig')
df0 = pd.read_csv('proxyIP.csv')
print(df0)

end = time.time()
print('total time : {}'.format(end-start))




