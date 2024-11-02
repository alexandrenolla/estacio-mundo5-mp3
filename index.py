import pandas as pd
import numpy as np

data = pd.read_csv('data.csv', sep=';', engine='python', encoding='utf-8')
copy = data.copy()

copy['Calories'] = copy['Calories'].fillna(0)

copy['Date'] = copy['Date'].fillna('1900/01/01')

copy['Date'] = copy['Date'].str.replace("'", "", regex=False)
copy['Date'] = copy['Date'].str.replace('20201226', '2020/12/26')
copy['Date'] = copy['Date'].replace('1900/01/01', np.nan)
copy['Date'] = pd.to_datetime(data_copy['Date'], format='%Y/%m/%d', errors='coerce')

copy = copy.dropna()

print(copy)
