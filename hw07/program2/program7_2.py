#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 10:11:56 2017

@author: rocky
"""
import numpy as np 
import matplotlib.pyplot as plt
global pi

 
def cos_exp(omega,constant=1):
    return (np.exp(1j*constant*omega) + np.exp(-1j*constant*omega) ) /2

if __name__ =='__main__':
    pi= np.pi 
    omega = np.linspace(0,2*pi,1024)
    X=np.exp(-1j*3*omega)*(6 - 6*cos_exp(omega) +4*cos_exp(omega,2) -2*cos_exp(omega,3))
    H_1 = 1
    H_2 = np.exp(-1j*3*omega)
    H_3 = (0.4-np.exp(-1j*omega))/(1-0.4*np.exp(-1j*omega))
    Y_1=X*H_1
    Y_2=X*H_2
    Y_3=X*H_3
    plt.subplot(2,1,1)
    plt.plot(omega/pi,np.abs(H_2))
    plt.title('Magnitude Spectrum')
    plt.xlabel('$\omega$/$\pi$')
    plt.ylabel('Amplitude')
    plt.subplot(2,1,2)
    plt.plot(omega/pi,np.angle(H_2))
    plt.title('Phase Spectrum ')
    plt.xlabel('$\omega$/$\pi$')
    plt.ylabel('Radians')
    plt.tight_layout()
    plt.show()
        