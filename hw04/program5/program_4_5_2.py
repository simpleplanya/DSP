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
sequence = np.ones(25)
x = np.cos(omega*sequence+theda)
y = np.convolve(x,h)
plt.subplot(2,1,1)
plt.title('$x[n]$')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.stem(range(len(x)),x)

x_ticks = [ i for i in range(0,25,5)]
x_ticks.append(24)
plt.xticks(x_ticks)

plt.subplot(2,1,2)
plt.title('$y[n]$')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.stem(range(len(y)),y)
x_ticks = [ i for i in range(0,len(y),5)]
x_ticks.append(26)
plt.xticks(x_ticks)
plt.tight_layout()

plt.show()