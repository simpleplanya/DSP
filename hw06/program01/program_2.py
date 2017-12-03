#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:48:45 2017

@author: rocky
"""
from scipy.signal import tf2zpk
from plot_zplane import draw_
alpha=-0.45
numerator   = [0,0,0,0,0,alpha**5,0,0,0,0,0,0,0,0,0,0,-alpha**16]
denominator = [1,-alpha,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#numerator = [1,0]
#denominator = [1,0.6]

z,p,k = tf2zpk(numerator,denominator)
z,p=draw_(z,p)