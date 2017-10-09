import numpy as np 
import matplotlib.pyplot as plt
from scipy.fftpack import fft
pi = np.pi
freq = 10000
nCyl = 8
fs = 200000
# np.arange function excluding stop value
t = np.arange(0,(nCyl*1/freq)+1/fs,1/fs)

x = np.cos(2*pi*freq*t)
plt.subplot(3,1,1)
plt.plot(t,x)
plt.subplot(3,1,2)
fs1=20000
t1=np.arange(0,(nCyl*1/freq)+1/fs,1/fs1)
x1=np.cos(2*pi*freq*t1)
plt.plot(t,x)
plt.stem(t1,x1)

plt.subplot(3,1,3)


n = len(x1)
k = np.arange(n)
T=n/fs1
frq = k*T
yf=fft(x1)
plt.plot(2*pi*frq,np.abs(yf))

plt.show()
