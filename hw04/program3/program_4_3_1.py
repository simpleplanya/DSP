#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:53:10 2017

@author: rocky
"""

import matplotlib.pyplot as plt 
h2=[1,-1]
plt.stem(h2)
plt.title('$h_2[n]$')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.xticks([0,1])
plt.show()