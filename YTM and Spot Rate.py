# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:40:45 2020

@author: Admin
"""

import math
from sympy import *
import numpy as np
import matplotlib.pyplot as plt


c=6      #coupon rate(%)
p=100    #par value
z1=2.5  #1Y spot rate
z2=list(range(z1,5,1))


for i in z2:

    v1=c/100*p/(1+z1/100)+(c/100*p+p)/math.pow((1+z2/100),2)
    r = symbols('r')
    solve(c/100*p/(1+r/100)+(c/100*p+p)/math.pow((1+r/100),2)-v1,r)

