#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:43:33 2017

@author: rocky
"""

from scipy.signal import tf2zpk
from plot_zplane import zplane 

alpha=-0.45
numerator = [0,0,0,0,0,alpha**-5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1*(alpha**16)] 
denominator =[0,0,0,0,0,1,-1*alpha,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

z,p,k = tf2zpk(numerator,denominator)
