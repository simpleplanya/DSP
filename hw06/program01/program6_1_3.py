#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:55:42 2017

@author: rocky
"""
from scipy.signal import tf2zpk
import numpy as np
np.set_printoptions(threshold=np.nan)

def detection_zeroTozero(zero,pole):
    Cpole = np.copy(pole)
    Czero = np.copy(zero)
    for idx,val in  enumerate (pole):
        if val in np.round(np.real(zero),3):
            Cpole=np.delete(Cpole,idx)      
    for Zidx,Zval in  enumerate (np.round(np.real(zero),3)):

        if Zval in np.round(pole,3):
            Czero=np.delete(Czero,Zidx)
    return  Czero,Cpole 


alpha=-0.45
numerator = [0,0,0,0,alpha**-15,0,0,0,0,0,0,0,0,0,0,-1*(alpha**-4),0,0,0,0] 
denominator =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1*alpha]

z,p,k = tf2zpk(numerator,denominator)
z,p = detection_zeroTozero(z,p)

print ('zero=', z)
print ('pole=', p )