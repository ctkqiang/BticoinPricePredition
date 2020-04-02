#!/usr/bin/env python
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import numpy as np

bitcoin_market_info = pd.read_csv("data/bitcoinPriceData.csv")
bitcoin_market_info["Timestamp"] = pd.to_datetime(bitcoin_market_info.Timestamp)
bitcoin_market_info.set_index("Timestamp", inplace=True)
date = bitcoin_market_info.resample("D").mean()
print(bitcoin_market_info.head())
plt.style.use("seaborn-poster")
fig = plt.figure(figsize=[15, 7])
plt.suptitle("Bitcoin Exchange mean $USD", fontsize=12)
# plt.subplot(221)
plt.plot(bitcoin_market_info.price, "-", label="BTC price by Months")
plt.legend()
plt.show()