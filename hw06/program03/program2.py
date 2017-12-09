#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:45:45 2017

@author: rocky
"""
import numpy as np
from scipy.signal import tf2zpk
def cheaksize(seq1,seq2):
    if len(seq1) == len(seq2):
        print("--------------len are equal--------------")
        return True
    else :
        return False
    
a=pow(-0.45,-5)+pow(0.9,-5)
b=-((0.9*((-0.45)**-5)) + ((-0.45)*(0.9**-5)) )
numerator = [a,b,0,0,0,0,0,0]
denominator = [1,-0.45,-0.405] 

zpk=tf2zpk(numerator,denominator)