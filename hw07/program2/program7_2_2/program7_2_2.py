#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 10:54:32 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt
global pi
from scipy.signal import lfilter 
from numpy.polynomial.polynomial import polymul
def cos_exp(omega,constant=1):
    return (np.exp(1j*constant*omega) + np.exp(-1j*constant*omega) ) /2

def impz(outputLen,b,a):
    x = np.zeros(outputLen)
    x[0]=1
    return lfilter(b,a,x)    
    
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
    #Y_1
    z_x = [-1,2,-3,6,-3,2,-1]
    y_1 = impz(7,z_x,1)
    print('y_1 = ',y_1)
    #plt.stem(impz(7,[-1,2,-3,6,-3,2,-1],1))
    #Y_2
    z_h2 = [0,0,0,1,0,0,0]
    y_2 = impz(10,polymul(z_x,z_h2),1)
    print('y_2 = ',y_2)
    #plt.stem(impz(10,[0,0,0,-1,2,-3,6,-3,2,-1],1))
    b=-2.5
    a=-0.4
    z_h3_numerator = [0.4,0.4*b]
    z_h3_denominator = [1,a,0,0,0,0,0,0,0,0]
    #Y_3
<<<<<<< HEAD:hw07/program2/program7_2_2.py
    y_3 = impz(20,[-0.4,-0.4*b+0.8,0.8*b-1.2,2.4-1.2*b,2.4*b-1.2,0.8-1.2*b,0.8*b-0.4,-0.4*b],[1,a,0,0,0,0,0,0,0,0])
=======
    y_3 = impz(7,polymul(z_x,z_h3_numerator,),z_h3_denominator)
>>>>>>> e70dc0ecc6e912ebf65f3c5531bca3ece82b8dc1:hw07/program2/program7_2_2/program7_2_2.py
    print('y_3 = ' ,y_3)
    #plt.stem(impz(7,[-0.4,-0.4*b+0.8,0.8*b-1.2,2.4-1.2*b,2.4*b-1.2,0.8-1.2*b,0.8*b-0.4,-0.4*b],[1,a,0,0,0,0,0,0,0,0]))