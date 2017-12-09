# -*- coding: utf-8 -*-
"""
Created on Sat Dec 09 23:21:21 2017

@author: Rocky
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

seven_order = (-0.9)**5 *(-0.45)
six_order = ((-0.45)**5 + (0.9)**5)
five_order = -1*(-0.45)**5 * (0.9)**-1

numerator   = [0,0,0,0,0,five_order,six_order,seven_order]
denominator = [-1*(0.9)**-1,0.5,0.45,0,0,0,0,0]
z,p,k = tf2zpk(numerator,denominator)
z,p,k=tf2zpk(numerator,denominator)
z,p = detection_zeroTozero(z,p)

print ('zero=', z)
print ('pole=', p )    