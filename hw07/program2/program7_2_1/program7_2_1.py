#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 10:11:56 2017

@author: rocky
"""
import numpy as np 
import matplotlib.pyplot as plt
global pi

 
def cos_exp(omega,constant=1):
    return (np.exp(1j*constant*omega) + np.exp(-1j*constant*omega) ) /2

def PlotResponse(X,H,Y):
    for idx , ele in enumerate(H): 
        plt.figure(idx)
        plt.subplot(2,1,1)
        plt.plot(omega/pi,np.abs(X),'b',label='$X(e^{j\omega})$')
        plt.plot(omega/pi,np.abs(ele),'r--',label='$H_'+str(idx+1)+'$'+'$(e^{j\omega})$')
        plt.plot(omega/pi,np.abs(Y[idx]),'y--',label='$Y_'+str(idx+1)+'$'+'$(e^{j\omega})$')
        plt.title(' Magnitude Spectrum')
        plt.xlabel('$\omega$/$\pi$')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.subplot(2,1,2)
        plt.plot(omega/pi,np.angle(X),'b',label='$X(e^{j\omega})$')
        plt.plot(omega/pi,np.angle(ele),'r--',label='$H_'+str(idx+1)+'$'+'$(e^{j\omega})$')
        plt.plot(omega/pi,np.angle(Y[idx]),'y--',label='$Y_'+str(idx+1)+'$'+'$(e^{j\omega})$')
        plt.title('Phase Spectrum ')
        plt.xlabel('$\omega$/$\pi$')
        plt.ylabel('Radians')
        plt.legend(loc='upper right')
        plt.tight_layout()
        plt.show()
    
if __name__ =='__main__':
    pi= np.pi 
    omega = np.linspace(0,2*pi,1024)
    X=np.exp(-1j*3*omega)*(6 - 6*cos_exp(omega) +4*cos_exp(omega,2) -2*cos_exp(omega,3))
    H_1 = np.ones(np.size(omega))
    H_2 = np.exp(-1j*3*omega)
    H_3 = (0.4-np.exp(-1j*omega))/(1-0.4*np.exp(-1j*omega))
    Y_1=X*H_1
    Y_2=X*H_2
    Y_3=X*H_3
    H_List = [H_1,H_2,H_3]
    Y_List = [Y_1,Y_2,Y_3 ]
    PlotResponse(X,H_List,Y_List) 
    #tested angle functrion
    #ang=np.arctan(np.sin(omega)/(-2.5+np.cos(omega)))-np.arctan(np.sin(omega)/(-0.4+np.cos(omega)))
    #plt.plot(omega/pi,ang)
    #plt.figure(3)

