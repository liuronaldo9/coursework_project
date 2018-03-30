# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 21:22:56 2018

@author: Administrator
"""

import numpy as np
from scipy.optimize import minimize

def func(x, sign=-1.0):
    return sign*np.sin(x)

def func_deriv(x, sign=-1.0):
    return sign*np.cos(x)



# Now an unconstrained optimization can be performed as:
x0 = 5.0
res = minimize(func, x0, jac=func_deriv, method='SLSQP', options={'disp': True})
print(res.x)
