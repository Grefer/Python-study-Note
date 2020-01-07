# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:22:53 2020

@author: Admin
"""

from scipy.stats import norm
import math

R=4.15       #current rate(%)
K=4.10       #exercise rate*(%)
r= 2.5992      #risk-free rate(%)
sigma=25   #valatility rate(%)
T=1          #option term(Y)

d1=(math.log(R/K)+math.pow(sigma/100,2)*T/2)/(sigma/100*math.sqrt(T))
d2=d1-sigma/100*math.sqrt(T)

if K>=R:
    c=math.exp(-r/100*T)*(R/100*norm.cdf(d1)-K/100*norm.cdf(d2))*10000
    print('The call option fee is :%.2f BP'%c)
else:
    p=math.exp(-r/100*T)*(K/100*norm.cdf(d2)-R/100*norm.cdf(-d1))*10000
    print('The put option fee is :%.2f BP'%p)


