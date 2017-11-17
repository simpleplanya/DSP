#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:38:10 2017

@author: rocky
"""
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal
global pi

if __name__ == '__main__':
    pi = np.pi
    omega_0 = 10*pi*10**-5
    seq = np.arange(0,20000)    
    x_n = np.cos(omega_0 *(seq*seq))
    f, t, Sxx = signal.spectrogram(x_n,window='hamming',nperseg=200,noverlap=199)
    plt.pcolormesh(t, f, Sxx)   
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()