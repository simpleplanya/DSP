#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 14:59:18 2017

@author: rocky
"""
import numpy as np 
import matplotlib.pyplot as plt 

Num = 50
seq = np.arange(0,Num,1)
Signal = 2*seq*(0.9**seq)
Signal = Signal[:,np.newaxis]
#initialization
NoiseAsig =np.zeros((len(Signal),1))
plt.subplot(2,1,1)
plt.title('Orginal signal')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.stem(seq,Signal)
#Ensemble average
for i in range (0,100,1):
    Noise = np.random.sample((Num,1))-0.5
    temp=Signal+Noise
    NoiseAsig=NoiseAsig+temp
NoiseAsig=NoiseAsig/100
plt.subplot(2,1,2)
plt.title('Ensemble average')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.stem(seq,NoiseAsig)
plt.tight_layout()
plt.show()