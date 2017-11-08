#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:20:43 2017

@author: rocky
"""
def zero_padding(seq,extendSize):
    padding=np.zeros(extendSize)
    padding[:len(seq)]=seq    
    return padding

import numpy as np 
import matplotlib.pyplot as plt 
x=np.array([-2,4,1,-1,3,5])
N=len(x)
h=np.array([1,-2,4,-1])
M=len(h)
x1=np.array([3,5,-2,4,1,-1,3,5])
x2=np.array([-1,3,5,-2,4,1,-1,3,5])
x3=np.array([1,-1,3,5,-2,4,1,-1,3,5])
y1=np.convolve(x1,h)
y2=np.convolve(x2,h)
y3=np.convolve(x3,h)
y1_=y1[2:N+2]
y2_=y2[3:N+3]
y3_=y3[4:N+4]
h_e=zero_padding(h,6)
y1_DFT=np.fft.fft(y1_)
y2_DFT=np.fft.fft(y2_)
y3_DFT=np.fft.fft(y2_)
H_e=np.fft.fft(h_e)
plt.figure(1)
plt.stem(np.fft.ifft(y1_DFT/H_e),markerfmt='r^',label='$\hat x_1[n]$')
plt.stem(x,label='x[n]')
plt.legend()
plt.grid()

plt.figure(2)
plt.stem(np.fft.ifft(y2_DFT/H_e),markerfmt='r^',label='$\hat x_2[n]$')
plt.stem(x,label='x[n]')
plt.legend()
plt.grid()
plt.figure(3)

plt.stem(np.fft.ifft(y3_DFT/H_e),markerfmt='r^',label='$\hat x_3[n]$')
plt.stem(x,label='x[n]')
plt.legend()
plt.grid()








