#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:09:22 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt 


def zero_padding(seq,extendSize):
    padding=np.zeros(extendSize)
    padding[:len(seq)]=seq    
    return padding
    
pi = np.pi
sequence = np.arange(0,16)
x_n = np.cos(6*pi*sequence/16)
k=np.arange(0,16)
DFT=[]
for element in k :
    DFT.append(np.dot(x_n,np.exp(-1j*2*pi*element*sequence/16)))

plt.stem(k/16,np.abs(DFT))
M=32
x_n_padding=zero_padding(x_n,M)
DTFT=[]
k=np.arange(0,32)
sequence = np.arange(0,32)
for element in k :
    DTFT.append(np.dot(x_n_padding,np.exp(-1j*2*pi*element*sequence/32)))


plt.plot(k/32,np.abs(DTFT))
plt.show()