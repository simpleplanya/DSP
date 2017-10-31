#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 14:36:08 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt 

h=np.array([-6.76195 ,13.456335, -6.76195])
#h_f=np.fft.fft(h)
t=np.array([0,1,2])
omega = np.arange(-np.pi,np.pi,0.01)
Gp=[]
for element in omega: 
    y = np.dot(h,np.exp(-1j*element*t))
    Gp.append(y)

plt.subplot(2,1,1)
plt.plot(omega/np.pi,np.abs(Gp))
plt.title('Magnitude Spectrum')
plt.xlabel('$\omega$/$\pi$')
plt.ylabel('Amplitude')
plt.subplot(2,1,2)
plt.plot(omega/np.pi,np.angle(Gp))
plt.title('Phase Spectrum ')
plt.xlabel('$\omega$/$\pi$')
plt.ylabel('Radians')
plt.tight_layout()
plt.show()

