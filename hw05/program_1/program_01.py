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
    N=16
    sequence = np.arange(0,N)
    x_n = np.cos(6*pi*sequence/N)
    M=16
    plt.stem(sequence/M,np.abs(DFT(x_n)))
    M=512
    x_n_padding=zero_padding(x_n,M)
    plt.plot(np.arange(0,M)/M,np.abs(DFT(x_n_padding)))
    #x axis 0~2pi
    plt.show()