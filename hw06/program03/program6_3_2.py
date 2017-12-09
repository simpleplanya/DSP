#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:45:45 2017

@author: rocky
"""
import numpy as np
np.set_printoptions(threshold=np.nan)
from scipy.signal import tf2zpk
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

    
a=pow(-0.45,-5)+pow(0.9,-5)
b=-((0.9*((-0.45)**-5)) + ((-0.45)*(0.9**-5)) )
numerator = [a,b,0,0,0,0,0,0]
denominator = [1,-0.45,-0.405] 

z,p,k=tf2zpk(numerator,denominator)
z,p = detection_zeroTozero(z,p)

print ('zero=', z)
print ('pole=', p )    