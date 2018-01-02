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
    #序列參數初始化
    omega_0 = 10*pi*10**-5
    seq = np.arange(0,20000)    
    #建立x_n序列
    x_n = np.cos(omega_0 *(seq*seq))
    #使用scipy.signal.spectrogram 進行 spectrogram參數運算
    #可參考：https://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.signal.spectrogram.html
    f, t, Sxx = signal.spectrogram(x_n,window='hamming',nperseg=200,noverlap=199)
    plt.title('R=200')
    plt.pcolormesh(t, f, Sxx)   
    plt.colorbar()
    plt.xlim(0,20000)
    plt.ylabel('Frequency ($\omega$)')
    plt.xlabel('Time (n)')
    plt.show()
