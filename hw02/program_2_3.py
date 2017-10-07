import numpy as np 
import matplotlib.pyplot as plt 

gain = 1
length = 40 
# create complex 
c= -0.083+0.523j
seq = np.arange(0,length)
x = gain*np.exp(c*seq)
#plot part
plt.subplot(2,1,1)
plt.stem(seq,np.real(x))
plt.title('Real part')
plt.xlabel('Time index n')
plt.ylabel('Amplitude')
plt.subplot(2,1,2)
plt.stem(seq,np.imag(x))
plt.title('Imaginary part')
plt.ylim(-1,1)
plt.xlabel('Time index n')
plt.ylabel('Amplitude')
#自動調整子圖間的間距
plt.tight_layout()
plt.show()

