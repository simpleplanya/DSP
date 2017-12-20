#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:03:23 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt 
global pi

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

def DFT_Interpolation(X_n,omega):
    Interpolation=[]
    N=len(X_n)
    k=np.arange(0,N)    
    for element in omega:
        Interpolation.append(np.dot(X_n,theta(element,k,N))) 
    return Interpolation

if __name__ == '__main__':
    pi=np.pi 
    N=16
    sequence = np.arange(0,N)
    x_n = np.cos(6*pi*sequence/N)
    #DFT
    X_n=DFT(x_n)
    omega=np.arange(-1.5*pi,1.5*pi,3*pi/1024)
    plt.title('DTFT from DFT by Interpolation')
    plt.plot(omega/pi,np.abs(DTFT(x_n,omega,sequence)),'-',linewidth=3,label='DTFT') 
    plt.plot(omega/pi,np.abs(DFT_Interpolation(X_n,omega)),'r:',linewidth=2,label='DTFT from DFT by Interpolation')
    plt.xlabel('$\omega/\pi$')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.tight_layout()
    plt.show()



