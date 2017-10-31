#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:45:22 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt 
x = np.array([1,2,3,4,5])
#h1 is unit step function
h1= np.array([1,1,1,1,1])
y1=np.convolve(x,h1)
h2=[1,-1]
y2=np.convolve(y1[0:5],h2)
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.stem(np.arange(len(y1[0:5])),y1[0:5],label ='$y_1[n]$')
plt.stem(np.arange(len(y2[0:5])),y2[0:5],label ='$y_2[n]$',markerfmt='ro')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

