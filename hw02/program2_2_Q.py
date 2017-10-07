# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:50:03 2017

@author: Rocky
"""

import numpy as np 
import matplotlib.pyplot as plt
x_seq = np.array([0,0,0,0,-2,0,1,-1,3,0,0,0,0])
h_seq = np.array([0,0,0,1,2,0,-1,0,0,0])    
y_seq = np.convolve(x_seq,h_seq)
plt.stem(np.arange(-4,9),x_seq)
plt.title('x[n]')
#設定x軸刻度
plt.xticks(np.arange(-4,9))
#設定y軸刻度
plt.yticks(x_seq)
plt.xlabel('The index n')
plt.ylabel('Amplitude')
plt.show()
'''-----------------------------------'''
plt.stem(np.arange(-3,7),h_seq)
plt.title('h[n]')
#設定x軸刻度
plt.xticks(np.arange(-3,7))
#設定y軸刻度
plt.yticks(h_seq)
plt.xlabel('The index n')
plt.ylabel('Amplitude')
plt.show()
