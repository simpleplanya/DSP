#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 10:54:32 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt
global pi

from numpy.fft import ifft
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
    plt.stem(np.real(ifft(Y_1,n=10)))
