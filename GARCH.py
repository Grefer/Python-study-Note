# -*- coding: utf-8 -*-
"""
GARCH（1,1）
Created on Tue Nov 10 15:37:16 2020

@author: Admin
"""

import numpy as np
import dataclasses

# example of ARCH model
from random import gauss
from random import seed
from matplotlib import pyplot
from arch import arch_model
# seed pseudorandom number generator
seed(1)
# create dataset
data = [gauss(0, i*0.01) for i in range(0,100)]
# split into train/test
n_test = 10
train, test = data[:-n_test], data[-n_test:]
# define model
model = arch_model(train, mean='Zero', vol='GARCH', p=15, q=15)
# fit model
model_fit = model.fit()
# forecast the test set
yhat = model_fit.forecast(horizon=n_test)
# plot the actual variance
var = [i*0.01 for i in range(0,100)]
pyplot.plot(var[-n_test:])
# plot forecast variance
pyplot.plot(yhat.variance.values[-1, :])
pyplot.show()

from datetime import datetime
from WindPy import w
import time
import pandas as pd
w.start()
w.isconnected()

data=w.wsd('600029.SH','close','2019-10-14','2020-10-14','Period=D;PriceAdj=B',usedf=True)
data=list(data)
data.columns =['date','price']
data['date'] = pd.to_datetime(data['date'])
data = data.set_index('date')

print(data.head(2))



data_test=data_SA.index('2019-10-14':'2020-06-14')
data_test[1].head()

data[1]

