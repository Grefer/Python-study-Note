# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:22:53 2020

@author: Admin
"""

from scipy.stats import norm
import math

L=1         #nominal principal(M)
F=4.2       #forward rate(%)
K=4.1       #exercise rate*(%)
r= 2.55     #risk-free rate(%)
sigma=20     #valatility rate(%)
t=0.25         #option start time
T=1       #option term(Y)

d1=(math.log(F/K)+math.pow(sigma/100,2)*t/2)/(sigma/100*math.sqrt(t))
d2=d1-sigma/100*math.sqrt(t)

c=T*math.exp(-r/100*(T+t))*(F/100*norm.cdf(d1)-K/100*norm.cdf(d2))*10000    
f=T*math.exp(-r/100*(T+t))*(K/100*norm.cdf(-d2)-F/100*norm.cdf(-d1))*10000
print('d1=%.4f,d2=%.4f'%(d1,d2))
print('The caplet price rate is:%.2f BP,and the floorlets price rate is:%.2f BP'%(c,f))
print('The caplet price is:%.2f,and the floorlet price is:%.2f'%(c*L*100,f*L*10000))

