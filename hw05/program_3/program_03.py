#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:13:49 2017

@author: rocky
"""

import numpy as np 
#import matplotlib.pyplot as plt 
np.set_printoptions(threshold=np.nan)
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
    sequence = np.arange(0,16)
    x_n = np.cos(6*pi*sequence/16)
    k = np.arange(0,16)
    N=18
    print('x[n]:')
    print(x_n.round(3))
    N_list=[16,18,12]
    for N in N_list:
        omega_k = np.arange(0,2*pi,2*pi/N)
        #use omega_k do DTFT
        Y_N =DTFT(x_n,omega_k,sequence)
        Y_N_iff =np.fft.ifft(Y_N)
        print('N=%d' %N,':')
        print(np.real(Y_N_iff).round(3))
        
    
    '''
    plt.stem(np.real(Y_N_iff),markerfmt='r^')
    plt.stem(x_n)
    '''
    
    
    
    