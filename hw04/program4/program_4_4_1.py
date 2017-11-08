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
=======
omega = np.arange(-2*np.pi,2*np.pi,0.001)
>>>>>>> 12c897288894e8e4753a79289230639dc2222c9a
Gp=[]
for element in omega: 
    y = np.dot(h,np.exp(-1j*element*t))
    Gp.append(y)

angle=np.angle(Gp)
plt.subplot(2,1,1)
plt.plot((omega/np.pi)[2512:3771],(np.abs(Gp))[2512:3771])
plt.title('Magnitude Spectrum')
plt.xlabel('$\omega$/$\pi$')
plt.ylabel('Amplitude')
plt.grid()
xtick=list(np.arange(-0.2,0.3,0.1))
xtick.append(0.1273)
ytick=[i for i in range(0,3,1)]
plt.xticks(xtick)

plt.subplot(2,1,2)
angle=np.angle(Gp)
plt.plot((omega/pi)[2512:3771],angle[2512:3771])
xtick=list(np.arange(-0.2,0.3,0.1))
xtick.append(0.1273)
ytick=[i for i in range(-2,3,2)]
ytick.append(angle[3542])
plt.grid()
plt.yticks(ytick)
plt.xticks(xtick)
plt.title('Phase Spectrum ')
plt.xlabel('$\omega$/$\pi$')
plt.ylabel('Radians')
plt.tight_layout()

plt.show()

