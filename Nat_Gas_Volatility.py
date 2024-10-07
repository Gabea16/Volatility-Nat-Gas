# -*- coding: utf-8 -*-
"""

@author: gabea
"""
# reading excel data and formating spot prices in log returns to smooth data
import pandas as pd 
df = pd.read_excel('Henry_Hub_Natural_Gas_Spot_Price.xlsx', skiprows=4)
import numpy as np
log_returns = np.log(df['Spot Prices MMBTU'] / df['Spot Prices MMBTU'].shift(1))

# plot of spot prices
df.plot(x='Year',y='Spot Prices MMBTU')

# calculating pct change of spot prices, removing first row
df['PCT']=df['Spot Prices MMBTU'].pct_change()
df_PCT=df['PCT'].iloc[1:]

# rolling standard deviations (volatility) over the 128 days
vol_ng_128=df_PCT.rolling(128).std()
print(vol_ng_128)

# rolling volatility over 2 day window 
vol_ng=df_PCT.rolling(2).std()
print(vol_ng)

# plotting rolling volatility over 2 day window
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.plot(vol_ng, label='2-Day Rolling Volatility (Every 12 Days = 1 Year)')

plt.title('2-Day Rolling Volatility of Spot Prices - Past 10 years')
plt.xlabel('Day')
plt.ylabel('Volatility')

plt.legend()

plt.show()
