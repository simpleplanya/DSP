#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:18:56 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt 
x1=np.array([1,2,3])
x2=np.array([1,2,3])
h_n=np.array([1,1,1])
y1=np.convolve(x1,h_n)
y2=np.convolve(x2,h_n)
plt.stem(y1,label='$y_1[]$')
plt.stem(np.arange(-1,4),y2,markerfmt='ro',label='$y_2[]$')
plt.legend()
plt.show()

