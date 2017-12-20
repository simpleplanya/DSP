#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:19:56 2017

@author: rocky
"""
import numpy as np 
import matplotlib.pyplot as plt

global pi 
def DTFT(x_n,omega,sequence):
    DTFT=[]
    for element in omega:
        DTFT.append(np.dot(x_n,np.exp(-1j*element*sequence)))
    return DTFT

def cos_exp(omega,constant=1):
    return (np.exp(1j*constant*omega) + np.exp(-1j*constant*omega) ) /2

if __name__ =='__main__':
    pi= np.pi 
    omega = np.linspace(0,2*pi,1024)
    X=np.exp(-1j*3*omega)*(6 - 6*cos_exp(omega) +4*cos_exp(omega,2) -2*cos_exp(omega,3) )
    plt.subplot(2,1,1)
    plt.plot(omega/pi,np.abs(X))
    plt.title('Magnitude Spectrum')
    plt.xlabel('$\omega$/$\pi$')
    plt.ylabel('Amplitude')
    
    plt.subplot(2,1,2)
    plt.plot(omega/pi,np.angle(X))
    plt.title('Phase Spectrum ')
    plt.xlabel('$\omega$/$\pi$')
    plt.ylabel('Radians')

    plt.show()