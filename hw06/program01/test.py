# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 12:35:33 2017

@author: Rocky
"""

from scipy.signal import tf2zpk
from plot_zplane import draw_
num = [2,16,44,56,32] 
dec = [0,3,3,-15,18,-12] 
z,p,k=tf2zpk(num,dec)
z,p=draw_(z,p)
