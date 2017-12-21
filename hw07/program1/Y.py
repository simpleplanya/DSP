#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 10:08:24 2017

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
    X=np.exp(-1j*3*omega)*(6 - 6*cos_exp(omega) +4*cos_exp(omega,2) -2*cos_exp(omega,3) )
    H=(4*(1.09+0.6*cos_exp(omega))*(1.16-0.8*cos_exp(omega))) /(1.04-0.2*cos_exp(omega))*(1.25+cos_exp(omega))   
    Y=X*H
    plt.subplot(2,1,1)
    plt.plot(omega/pi,np.abs(Y))
    plt.title('Magnitude Spectrum')
    plt.xlabel('$\omega$/$\pi$')
    plt.ylabel('Amplitude')
    
    plt.subplot(2,1,2)
    plt.plot(omega/pi,np.angle(Y))
    plt.title('Phase Spectrum ')
    plt.xlabel('$\omega$/$\pi$')
    plt.ylabel('Radians')

    plt.show()