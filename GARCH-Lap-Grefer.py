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

SA = pd.read_csv(open(r"D:\Desktop\One Driver\OneDrive\Project B\Convertable Bond\南航行情序列.csv"))    #导入时间序列

SA.columns =['date','price']
SA['date'] = pd.to_datetime(SA['date'])
SA = SA.set_index('date')            #指定日期为索引值方便调用

SA['return'] = np.log(SA['price']/SA['price'].shift(1))      #计算连续收益率%
SA['vol']=SA['return'].rolling(window=5).std()          #计算滚动标准差/日波动率

#SA[['price','return','vol']].plot(subplots = True,style = 'b',figsize=(8,5))

split_date = '2020-06-15'
sample = SA['2019-10-14':split_date]    #指定样本集
test = SA[split_date:'2020-10-14']      #指定测试集


#GARCH模型建立

model = arch.arch_model(sample['return'], mean='AR', vol='GARCH',p=1,q=1,dist='StudentsT')
model_fit = model.fit(last_obs=split_date)
print(model_fit.summary())


f_vol = model_fit.forecast()
      

np.sqrt(f_vol.variance[split_date:]).plot()
plt.show()

SA['vol']
