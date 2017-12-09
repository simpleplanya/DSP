#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:55:42 2017

@author: rocky
"""


from scipy.signal import tf2zpk
alpha=-0.45
numerator = [0,0,0,0,alpha**-15,0,0,0,0,0,0,0,0,0,0,-1*(alpha**-4),0,0,0,0] 
denominator =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1*alpha]

z,p,k=tf2zpk(numerator,denominator)