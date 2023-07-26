import pandas as pd

df = pd.read_csv('./proxyIP.csv')

df0 = df['proxyIP']
print(df0)