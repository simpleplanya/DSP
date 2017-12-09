# -*- coding: utf-8 -*-
"""
Created on Sat Dec 09 23:55:31 2017

@author: Rocky
"""

from scipy.signal import residue 
b = [2,0.8,0.5,0.3]
a = [1,0.8,0.2]

r,p,k=residue(b,a)
x = [1,0,0,0,0,0,0,0,0,0,0]
print ('Residues=', r)
print ('Poles=',p)
print ('Coefficients of the direct polynomial term=',k)