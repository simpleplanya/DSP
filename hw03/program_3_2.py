import numpy as np 
import matplotlib.pyplot as plt

pi = np.pi
#f_m is the highest frequency in the original analog signal 
f_m = 30
omega_m = 2*pi*f_m
#F_T=1/T
F_T = 2*f_m


# t is the range of time, in which the analog signal is considered (Thus the analog singal is limimted in time, but unlimited in frequency) 
t = np.arange(-1,2,1/F_T)
#continuous angular frequency after DTFT
omega  =  np.arange(-omega_m-5,omega_m+5,0.05)
Gp = np.zeros(len(omega))
# analog signal  page 51 
x = np.sin(omega_m *t)/(pi*t)

for index ,element in enumerate(omega): 
    y = np.dot(x,np.exp(-1j*element*t))
    Gp[index]=y

plt.subplot(2,1,1)
plt.plot(omega,Gp)
plt.subplot(2,1,2)
omega  =  np.arange(-3*omega_m-5,3*omega_m+5,0.05)
Gp = np.zeros(len(omega))
# analog signal  page 51 
x = np.sin(omega_m *t)/(pi*t)

for index ,element in enumerate(omega): 
    y = np.dot(x,np.exp(-1j*element*t))
    Gp[index]=y
plt.plot(omega,Gp)
#p148 D/A
#hold
'''

plt.subplot(3,1,1)
plt.plot(t,x)
plt.subplot(3,1,2)
fs1=30
#t1=np.arange(0,(1/freq)+1/fs,1/fs1)

x1=np.sin(pi*fs1*t)/(pi*fs1*t)
plt.plot(t,x1)
plt.stem(t,x1)

plt.subplot(3,1,3)

n = len(x1)
k = np.arange(n)
T=n/fs1
frq = k*T
yf=fft(x1)
plt.plot(2*pi*frq,np.abs(yf))
plt.show()
'''