#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:27:55 2017

@author: rocky
"""

from scipy.signal import residue 

b = [2,0.8,0.5,0.3]
a = [1,0.8,0.2]
r,p,k=residue(b,a)
