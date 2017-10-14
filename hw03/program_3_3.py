#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 16:20:15 2017

@author: rocky
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:01:36 2017

@author: rocky
"""
#draw sin and sinc 
#range variable 
import numpy as np 
import matplotlib.pyplot as plt

''' analog signal'''
pi = np.pi
#f_m is the highest frequency in the original analog signal 
f_m = 1
fs = 600*f_m
omega_m = 2*pi*f_m
t = np.arange(-1,1+1/fs,1/fs) 
#x = np.cos(omega_m*t) 
x = np.sin(omega_m *t)/(pi*t)
plt.subplot(3,1,1)
plt.plot(t,x)

'''sampling'''
#F_T = 1/T
F_T = 1.63*f_m
# t is the range of time, in which the analog signal is considered (Thus the analog singal is limimted in time, but unlimited in frequency) 
t_s = np.arange(-1,1+1/F_T,1/F_T)  #sampling instances (nT)
#samples =  np.cos(omega_m*t_s) #sampled version of analog signal
samples = np.sin(omega_m *t_s)/(pi*t_s)
#continuous angular frequency after DTFT
plt.subplot(3,1,2)
plt.stem(t_s,samples)

plt.subplot(3,1,3)
#cutoff freq of lowpass filter
F_C = 2*f_m
DA = [] 

for idx , val in enumerate(t):
    y =(np.sin(2*pi*F_C*(val-t_s)))/((2*pi*F_T*(val-t_s))/2)
    DA.append(np.dot(samples,y))
plt.plot(t,x)
plt.plot(t,DA,'r--')
#plt.ylim(-2,2)
plt.tight_layout()
plt.show()








