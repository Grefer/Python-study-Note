# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:40:00 2020

@author: Admin
"""


# 欧式看涨期权BSM定价公式

from scipy.stats import norm
import numpy as np
def BSMCall(S,K,r,sigma,t):
	d1=(np.log(S/K)+(r+0.5*sigma**2)*t)/(sigma*np.sqrt(t))
	d2=d1-sigma*np.sqrt(t)
	return S*norm.cdf(d1)-K*np.exp(-r*t)*norm.cdf(d2)

# 牛顿迭代法

def newton_call(P2,S,r,sigma,t,B):
	K=6.24
	while abs(BSMCall(S,K,r,sigma,t)*int(100/K)+B-P2)>0.0001:
		if BSMCall(S,K,r,sigma,t)*int(100/K)+B>P2:
			K+=0.0001
		else:
			K-=0.0001
	return K

#   P2---回售价格   B---债券价值

print('调整后转股价为:%.2f' %newton_call(100,4.37,0.0279,0.3,2,97.923))