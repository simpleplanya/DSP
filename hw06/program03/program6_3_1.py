#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:20:10 2017

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
def cheaksize(seq1,seq2):
    if len(seq1) == len(seq2):
        print("--------------len are equal--------------")
        return True
    else :
        return False
    
a=(-0.45**5)+(0.9**5)
b=-((0.9*(-0.45**5)) + ((-0.45)*0.9**5) )
numerator = [0,0,0,0,0,a,b]
denominator = [1,-0.45,-0.405,0,0,0,0] 

if cheaksize(numerator,denominator) == True:
    z,p,k=tf2zpk(numerator,denominator)
else :
    print("numerator's len not equal denominator's len")
    
z,p = detection_zeroTozero(z,p)

print ('zero=', z)
print ('pole=', p )    
    
    
    