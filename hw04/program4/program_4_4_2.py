#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:23:15 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt 
pi = np.pi
omega = 0.4
#omega=1.2
theda = 0

h = np.array([1.6,1.5,-0.8])
# = np.array([1])
#sequence = np.arange(-1,1+0.05,0.05)

sequence = np.arange(-1,1+0.05,0.05)

h = np.array([-6.76195 ,13.456335, -6.76195])
sequence = np.arange(0,100,1)
x = np.cos(omega*sequence+theda)
y = np.convolve(x,h)
plt.title('$\omega_0=0.4$')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.stem(sequence,x,label='x[n]')
plt.stem(sequence,y[:-2],markerfmt='ro',label='y[n]')
plt.legend()
plt.tight_layout()
plt.show()
