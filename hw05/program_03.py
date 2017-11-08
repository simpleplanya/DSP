#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:13:49 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt 
def DTFT(x_n,omega,sequence):
    X_n=[]
    for element in omega:
        X_n.append(np.dot(x_n,np.exp(-1j*element*sequence)))
    return X_n

def IDFT(X_n):
    x_n=[]
    k=np.arange(len(X_n))
    N=np.arange(len(X_n))
    for i in N:
        x_n.append(np.dot(X_n,np.exp((-1j*2*np.pi*k*i)/len(N)))/len(N))
    return x_n


    
if __name__ == '__main__':
    pi = np.pi
    fs = 1000
    sequence = np.arange(0,16)
    x_n = np.cos(6*pi*sequence/16)
    k = np.arange(0,16)
    omega=np.arange(-1.5*pi,1.5*pi+0.001,0.1)
    N=16
    omega_k = np.arange(-1.5*pi,1.5*pi,3*pi/N)
    x_n_DTFT = DTFT(x_n,omega,sequence)
    Y_N =DTFT(x_n,omega_k,sequence)
    Y_N_iff =np.fft.ifft(x_n_DTFT)
   
    #plt.plot(Y_N_iff)
    #plt.plot(omega/pi,np.abs(DTFT(x_n,omega,sequence)))
    #plt.stem(x_n)
    plt.stem(np.real(Y_N_iff)[0:16],markerfmt='ro')
    plt.stem(x_n)