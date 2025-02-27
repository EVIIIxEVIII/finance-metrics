import pandas as pd

df = pd.read_csv('ibm.csv')

df['Open'] = df['Open'] / 10000
df['Close'] = df['Close'] / 10000
df['High'] = df['High'] / 10000
df['Low'] = df['Low'] / 10000

df['Date'] = pd.to_datetime(df['Date'])

df.to_csv('clean_imb.csv', index=False)

