#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 14:36:08 2017

@author: rocky
"""

import numpy as np 
import matplotlib.pyplot as plt 

h=np.array([1,1.5,-0.8])
h_f=np.fft.fft(h)
freq = np.fft.fftfreq(h.shape[-1])
plt.plot(abs(h_f.real))
plt.show()