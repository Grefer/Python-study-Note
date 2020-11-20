# -*- coding: utf-8 -*-
"""
GARCH（1,1）
Created on Tue Nov 10 15:37:16 2020

@author: Admin
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import arch

SA = pd.read_csv(open(r"C:\Users\Admin\Desktop\OneDrive\Project B\Convertable Bond\南航行情序列.csv"))    #导入时间序列

SA.columns =['date','price']
SA['date'] = pd.to_datetime(SA['date'])
SA = SA.set_index('date')            #指定日期为索引值方便调用

SA['return'] = np.log(SA['price']/SA['price'].shift(1))

SA[['price','return']].plot(subplots = True,style = 'b',figsize=(8,5))

SA['Mov_Vol']=pd.rolling_std(SA['Return'],window = 252)*math.sqrt(252)

sample = SA['2019-10-14':'2020-06-14']    #指定样本集
test = SA['2020-06-15':'2020-10-14']      #指定测试集


#GARCH模型建立

model = arch.arch_model(sample, mean='AR', vol='GARCH', p=1, q=1)

model_fit = model.fit()

yhat = model_fit.forecast(horizon=164)

var = [i*0.01 for i in range(0,100)]
plt.plot(var[163:])
# plot forecast variance
plt.plot(yhat.variance.values[-1, :])
plt.show()