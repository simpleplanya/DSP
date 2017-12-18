#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 15:24:59 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt

#create two sequences
x1=[3,6,7,1,2,0,0]
x2=[3,6,7,1,2,8,10]
#LTI system h[n]
h = [1,2,3]
y1=np.convolve(x1,h)
y2=np.convolve(x2,h)
#draw y1
plt.stem(range(0,len(y1)),y1,label='$y_1[n]$')
plt.title('Non-Causal System')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
#draw y2
plt.stem(range(-1,len(y2)-1),y2,label='$y_2[n]$',markerfmt='ro')
plt.xticks(range(-1,len(y2)))
plt.legend()
plt.tight_layout()
plt.show()

