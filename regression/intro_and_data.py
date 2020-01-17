import pandas as pd

# for fetching data sets
import quandl

# fetch data set
df = quandl.get('WIKI/GOOGL')

# selecting relevant fields
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# Creating new attributes
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

# updating data set
df = df[['Adj. Close', 'Adj. Volume', 'HL_PCT', 'PCT_change']]

# printing the data in the data set
print(df.head())