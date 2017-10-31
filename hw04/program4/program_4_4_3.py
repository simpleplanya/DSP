#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:41:27 2017

@author: rocky
"""
import numpy as np 
import matplotlib.pyplot as plt 
pi = np.pi
omega = 1.2
#omega=1.2
theda = 0
h = np.array([-6.76195 ,13.456335, -6.76195])
sequence = np.arange(0,100,1)
x = np.cos(omega*sequence+theda)
y = np.convolve(x,h)

plt.subplot(2,1,1)
plt.title('x[n],$\omega_0=1.2$')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.stem(sequence,x,label='x[n]')
plt.subplot(2,1,2)
plt.title('y[n],$\omega_0=1.2$')
plt.stem(sequence,y[:-2])
plt.tight_layout()
plt.show()
