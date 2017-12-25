#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 17:24:38 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt 

pi = np.pi
a=0.5
b=-0.8
omega = np.linspace(0,pi,10240)
X = (-0.8*np.exp(1j*omega)+1) / (np.exp(1j*omega)+0.5)
func = np.arctan(b*np.sin(omega)/(1+b*np.cos(omega)))- np.arctan(np.sin(omega)/(a+np.cos(omega)))
plt.plot(omega/pi,np.angle(X),'b')
plt.plot(omega/pi,func,'r--')

'''
pi = np.pi
a=-0.4
b=-2.5
omega = np.linspace(0,pi,1024)
X = (0.4-np.exp(-1j*omega)) / (1 - (0.4*np.exp(1j*omega)))
func = np.arctan(np.sin(omega)/(b+np.cos(omega))) - np.arctan(np.sin(omega)/(a+np.cos(omega)))
plt.plot(omega/pi,np.angle(X),'b')
plt.plot(omega/pi,func,'r--')
'''