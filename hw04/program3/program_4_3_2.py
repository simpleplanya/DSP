import numpy as np 
import matplotlib.pyplot as plt 
x = np.array([1,2,3,4,5])
#h1 is unit step function
h1= np.array([1,1,1,1,1])
y1=np.convolve(x,h1)
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.stem(np.arange(len(x)),x,label='$x[n]$')
plt.stem(np.arange(len(y1[0:5])),y1[0:5],label='$y_1[n]$',markerfmt='ro')
#自動調整子圖間的間距
plt.tight_layout()
plt.grid()
plt.legend()
plt.show()

