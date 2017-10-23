#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 16:20:15 2017

@author: rocky
"""
import numpy as np 
import matplotlib.pyplot as plt 
''' analog signal'''
pi = np.pi
#f_m is the highest frequency in the original analog signal 
f_m = 1
fs = 600.5*f_m
omega_m = 2*pi*f_m
time_index1 = -1.5
time_index2 = 1.5
t = np.arange(time_index1,time_index2+1/fs,1/fs) 
#x = np.cos(omega_m*t) 
x = np.sin(omega_m *t)/(pi*t)
plt.subplot(3,1,1)
plt.title('Orginal Analog Signal in Time Interval [-1.5 1.5]')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.plot(t,x)
'''sampling'''
#F_T = 1/T
F_T = 3.63*f_m
# t is the range of time, in which the analog signal is considered (Thus the analog singal is limimted in time, but unlimited in frequency) 
t_s = np.arange(time_index1,time_index2+1/F_T,1/F_T)  #sampling instances (nT)
#samples =  np.cos(omega_m*t_s) #sampled version of analog signal
samples = np.sin(omega_m *t_s)/(pi*t_s)
plt.subplot(3,1,2)
plt.title('Sample Sequence')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.stem(t_s,samples)
plt.grid()
plt.subplot(3,1,3)
#cutoff freq of lowpass filter
F_C = 1.1*f_m
#initial D/A  
DA = [] 
for val in t:
    y =(np.sin(2*pi*F_C*(val-t_s)))/((2*pi*F_T*(val-t_s))/2)
    DA.append(np.dot(samples,y))
plt.title('Recovery of Analog Signal ')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.plot(t,x,label='Original Signal')
plt.plot(t,DA,'r--',label='Recovery')
plt.grid()
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

