import numpy as np 
import matplotlib.pyplot as plt

pi = np.pi
#f_m is the highest frequency in the original analog signal 
f_m = 30
omega_m = 2*pi*f_m
#F_T=1/T
F_T = 3*f_m
time_index1 = -1
time_index2 = 1
# t is the range of time, in which the analog signal is considered (Thus the analog singal is limimted in time, but unlimited in frequency) 
t = np.arange(time_index1,time_index2+1/F_T,1/F_T)
#continuous angular frequency after DTFT
omega = np.arange(-omega_m-5,omega_m+5,0.05)
Gp = np.zeros(len(omega))
# analog signal (page 51) 
x = np.sin(omega_m *t)/(pi*t)
for index ,element in enumerate(omega): 
    y = np.dot(x,np.exp(-1j*element*t))
    Gp[index]=y

plt.subplot(2,1,1)
plt.plot(omega,Gp)
plt.title('$\omega_T$')
plt.xlabel('$\omega$')
plt.ylabel('$G_p(j\omega)$')
plt.subplot(2,1,2)
omega = np.arange(-4*omega_m-5,4*omega_m+5,0.05)
Gp = np.zeros(len(omega))
# analog signal  page 51 
x = np.sin(omega_m *t)/(pi*t)
for index ,element in enumerate(omega): 
    y = np.dot(x,np.exp(-1j*element*t))
    Gp[index]=y
plt.plot(omega,Gp)
plt.title('3 $\omega_T$')
plt.xlabel('$\omega$')
plt.ylabel('$G_p(j\omega)$')
plt.tight_layout()
plt.show()