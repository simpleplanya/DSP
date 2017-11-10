#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:30:22 2017

@author: rocky
"""
import numpy as np 
import matplotlib.pyplot as plt 

def zero_padding(seq,extendSize):
    padding=np.zeros(extendSize)
    padding[:len(seq)]=seq    
    return padding

def DFT(x_n):
    pi=np.pi
    M=len(x_n)
    sequence = np.arange(0,M)
    k=np.arange(0,M)
    X_n=[]
    for element in k :
        X_n.append(np.dot(x_n,np.exp(-1j*2*pi*element*sequence/M)))
    return np.asarray(X_n)

if __name__ == '__main__':
    #initialization 
    x=np.array([1,2,3])
    h_n=np.array([1,1,1])
    y1=np.convolve(x,h_n)
    x_e3=zero_padding(x,3)
    x_e4=zero_padding(x,4)
    x_e5=zero_padding(x,5)
    x_e6=zero_padding(x,6)
    x_e7=zero_padding(x,7)
    h_e3=zero_padding(h_n,3)
    h_e4=zero_padding(h_n,4)
    h_e5=zero_padding(h_n,5)
    h_e6=zero_padding(h_n,6)
    h_e7=zero_padding(h_n,7)
    #create gruop
    x_space=[x_e3,x_e4,x_e5,x_e6,x_e7]
    h_space=[h_e3,h_e4,h_e5,h_e6,h_e7]
    y_space=[]
    for i in range (len(x_space)):
        y_space.append(np.fft.ifft(DFT(x_space[i])*DFT((h_space[i]))))
        
    print('y1[n]:')
    print(y1)
    for j in range(len(x_space)):
        
        print('M=:',j+3)
        print(np.real(y_space[j]).round(3))
    
    '''
    plt.figure(1)
    plt.stem(y_space[0],label='M=3',markerfmt='r>',)
    plt.stem(y1,label='$y_1[n]$',markerfmt='b^')    
    plt.legend()
    plt.show()
    plt.figure(2)
    plt.stem(y_space[1],label='M=4',markerfmt='r>',)
    plt.stem(y1,label='$y_1[n]$',markerfmt='b^')    
    plt.legend()    
    plt.show()
    plt.figure(3)
    plt.stem(y_space[2],label='M=5',markerfmt='r>',)
    plt.stem(y1,label='$y_1[n]$',markerfmt='b^')    
    plt.legend()   
    plt.show()
    plt.figure(4)
    plt.stem(y_space[3][:5],label='M=6',markerfmt='r>',)
    plt.stem(y1,label='$y_1[n]$',markerfmt='b^')    
    plt.legend()   
    plt.show()
    plt.figure(5)
    plt.stem(y_space[4][:5],label='M=7',markerfmt='r>',)
    plt.stem(y1,label='$y_1[n]$',markerfmt='b^')    
    plt.legend()   
    plt.show()
    '''




