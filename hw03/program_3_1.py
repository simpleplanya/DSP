import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal 
PointNum = 1000
pi = np.pi
NumeratorCof = np.array([0.008,-0.033*np.exp(-1j*2*pi),0.05*np.exp(-2j*2*pi),-0.33*np.exp(-3j*2*pi),0.008*np.exp(-4j*2*pi)])


DenominatorCof = np.array([1,2.37*np.exp(-1j*2*pi),2.7*np.exp(-2j*2*pi),1.6*np.exp(-3j*2*pi),0.41*np.exp(-4j*2*pi)])

w = np.arange(0,pi,pi/(PointNum-1))

FreResponse , d = signal.freqz(NumeratorCof,DenominatorCof,w)
print (w.shape)
#print (np.real(FreResponse.shape))
plt.plot(w/pi,np.real(FreResponse))
plt.show()
