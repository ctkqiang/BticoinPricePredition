#!/usr/bin/env python
#
#              Copyright 2020 © John Melody Me
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#             http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# @Author : John Melody Me
# @Copyright: John Melody Me & Tan Sin Dee © Copyright 2020
# @INPIREDBYGF: Cindy Tan Sin Dee <3
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import numpy as np
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
bitcoin_market_info = pd.read_csv("data/bitcoinPriceData.csv")
bitcoin_market_info["Timestamp"] = pd.to_datetime(bitcoin_market_info.Timestamp)
bitcoin_market_info.set_index("Timestamp", inplace=True)
date = bitcoin_market_info.resample("D").mean()
print(bitcoin_market_info.head())
# plt.style.use("seaborn-poster")
fig = plt.figure(figsize=[15, 7])
plt.suptitle("Bitcoin Exchange mean $USD", fontsize=12)
plt.plot(bitcoin_market_info.price, "-", label="BTC price by Months")
plt.legend()
plt.show()