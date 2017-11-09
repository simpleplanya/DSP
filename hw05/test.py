#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:03:23 2017

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
def DTFT(x_n,omega,sequence):
    DTFT=[]
    for element in omega:
        DTFT.append(np.dot(x_n,np.exp(-1j*element*sequence)))
    return DTFT

def theta(omega,k,N):
    omega = omega-(2*pi*k/N)
    return (np.sin(omega*N/2)/(N*np.sin(omega/2)))*np.exp(-1j*omega*((N-1)/2))

if __name__ == '__main__':
    pi=np.pi 
    N=16
    sequence = np.arange(0,N)
    x_n = np.cos(6*pi*sequence/N)
    M=16
    #DFT
    X_n=np.fft.fft(x_n)
    DFT_Interpolation=[]
    N=len(sequence)
    k=np.arange(0,N)    
    omega=np.arange(pi,3*pi,2*pi/1024)
    for element in omega:
        '''
        first_item=np.sin((element*N-2*pi*k)/2)/ np.sin((element*N-2*pi*k)/2*N)
        second_item=np.exp(-1j*(element-(2*pi*k/N))*((N-1)/2))
        inter_poly=first_item*second_item
        '''
        DFT_Interpolation.append(np.dot(X_n,theta(element,k,N))) 
        
    plt.plot(omega/pi,np.abs(DTFT(x_n,omega,sequence)))   
    plt.plot(omega/pi,np.abs(DFT_Interpolation))
    plt.show()



