#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:23:15 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt 
pi = np.pi
omega = 8*pi
theda = 0
h = np.array([1,1.5,-0.8])
sequence = np.ones(20)
x = np.cos(omega*sequence+theda)
y = np.convolve(x,h)
plt.subplot(2,1,1)
plt.stem(range(len(x)),x)
plt.subplot(2,1,2)
plt.stem(range(len(y)),y)