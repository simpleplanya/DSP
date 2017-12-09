#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:20:10 2017

@author: rocky
"""
from scipy.signal import tf2zpk
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