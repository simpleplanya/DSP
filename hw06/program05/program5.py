#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:27:55 2017

@author: rocky
"""

from scipy.signal import residue 
from scipy.signal import lfilter
import numpy as np 
#b = [2,0.8,0.5,0.3]
#a = [1,0.8,0.2]
b = [1,2.0]
a=[1,0.4,-0.12]

r,p,k=residue(b,a)
x = [1,0,0,0,0,0,0,0,0,0,0]
i_z=lfilter(b,a,x)
