#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:53:20 2017

@author: rocky
"""
from scipy.io import wavfile
import matplotlib.pyplot as plt 
from scipy import signal
global pi

if __name__ == '__main__':
    
    
    rate,sig = wavfile.read('hello.wav')
    #plt.plot(sig[24000:25750])
    fs=44100
    f, t, Sxx = signal.spectrogram(sig,fs=44100,window='hamming',nperseg=200,noverlap=199,nfft=1000)
    plt.pcolormesh(t, f, Sxx)   
    plt.ylim(0,2500)
    plt.xlim(0.4,1.1)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()
    
