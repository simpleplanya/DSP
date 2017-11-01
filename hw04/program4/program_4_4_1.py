#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 14:36:08 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt 
pi=np.pi
h=np.array([-6.76195 ,13.456335, -6.76195])
#h_f=np.fft.fft(h)
t=np.array([0,1,2])
omega = np.arange(-pi,pi,0.001)
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
angle=np.angle(Gp)
plt.plot(omega[2742:3542],angle[2742:3542])
xtick=np.arange(-0.4,0.5,0.2)
ytick=[i for i in range(-2,3,2)]
ytick.append(angle[3542])
plt.grid()
plt.yticks(ytick)
plt.xticks(xtick)
plt.title('Phase Spectrum ')
plt.xlabel('$\omega$')
plt.ylabel('Radians')
plt.tight_layout()
plt.show()

