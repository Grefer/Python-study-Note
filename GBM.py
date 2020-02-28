# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 23:56:53 2019

@author: Minevei
"""

import matplotlib.pyplot as plt
import numpy as np

rect = [0.1,5.0,0.1,0.1]
fig = plt.figure(figsize=(10,6))

T = 2
mu = 0.2
sigma = 0.05
B0 = 1
dt = 0.01
step = round(T/dt)
t = np.linspace(0,T,step)

N = np.random.standard_normal(size = step)
W = np.cumsum(N)*np.sqrt(dt)

Bt = (mu-0.5*sigma**2)*t + sigma*W
St = B0*np.exp(Bt)
#figure
plt.plot(t,St,lw=2)
plt.xlabel("Time t",fontsize=16)
plt.ylabel("Value St",fontsize=16)
plt.title("dSt=μStdt+σStdWt",fontsize=18)
plt.show()
