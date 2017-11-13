#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:09:22 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt 
global pi

def zero_padding(seq,extendSize):
    padding=np.zeros(extendSize)
    padding[:len(seq)]=seq    
    return padding

def DFT(x_n):
    M=len(x_n)
    sequence = np.arange(0,M)
    k=np.arange(0,M)
    X_n=[]
    for element in k :
        X_n.append(np.dot(x_n,np.exp(-1j*2*pi*element*sequence/M)))
    return X_n

if __name__ == '__main__':
    pi=np.pi 
    M=16
    sequence = np.arange(0,M)
    x_n = np.cos(6*pi*sequence/M)
    N=16
    markerline, stemlines, baseline =plt.stem(np.arange(0,2*pi,2*pi/N)/pi,np.abs(DFT(x_n)) ,fillstyle='none',markerfmt='ro',label='M-point DFT of x[n]')
    plt.setp(markerline, 'markerfacecolor' , 'w')
    plt.setp(stemlines,'linestyle','None')
    N=512
    x_n_padding=zero_padding(x_n,N)
    plt.plot(np.arange(0,2*pi,2*pi/N)/pi,np.abs(DFT(x_n_padding)),label='N-point DFT of x[n]')
    #x axis 0~2pi
    plt.title('N=%d' %N)
    plt.legend()
    plt.xlabel('$\omega/\pi $')
    plt.ylabel('Amplitude')
    plt.show()
    