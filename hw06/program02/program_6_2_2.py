# -*- coding: utf-8 -*-
"""
Created on Sat Dec 09 22:47:56 2017

@author: Rocky
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

seven_order=((-0.45)**-5) + ((0.9)**-5)
six_order = -1*((0.9*(-0.45)**-5)-(0.45*((0.9)**-5)))
numerator = [seven_order,six_order,0,0,0,0,0,0,0] 
denominator =[1,-0.45,-0.405]
z,p,k=tf2zpk(numerator,denominator)

z,p = detection_zeroTozero(z,p)

print ('zero=', z)
print ('pole=', p )