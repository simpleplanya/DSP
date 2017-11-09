#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:54:59 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt 

def DTFT(x_n,omega,sequence):
    DTFT=[]
    for element in omega:
        DTFT.append(np.dot(x_n,np.exp(-1j*element*sequence)))
    return DTFT
def DFT(x_n,k,sequence):
    DFT=[]
    for element in k :
        DFT.append(np.dot(x_n,np.exp(-1j*2*pi*element*sequence/16)))
    return DFT
    
if __name__ == '__main__':
    pi = np.pi
    sequence = np.arange(0,16)
    x_n = np.cos(6*pi*sequence/16)
    k = np.arange(0,16)
    
    X_k=DFT(x_n,k,sequence)    
    DFT_Interpolation=[]
    N=len(sequence)    
    omega=np.arange(-1.5*pi,1.5*pi+0.001,0.05)
    for element in omega:
        first_item=np.sin((element*N-2*pi*k)/2)/ np.sin((element*N-2*pi*k)/2*N)
        second_item=np.exp(-1j*(element-(2*pi*k/N))*((N-1)/2))
        inter_poly=first_item*second_item
        DFT_Interpolation.append(np.dot(X_k,inter_poly)/N) 
    
    #plt.stem(X_k)
    plt.plot(omega/pi,np.abs(DTFT(x_n,omega,sequence)))
    plt.plot(omega/pi,np.abs(DFT_Interpolation))
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    