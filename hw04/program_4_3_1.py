import numpy as np 
import matplotlib.pyplot as plt 
x = np.array([1,2,3,4,5])
#h1 is unit step function
h1= np.array([1,1,1,1,1])
y1=np.convolve(x,h1)
plt.subplot(2,1,1)
plt.stem(np.arange(len(x)),x)
plt.grid()
plt.subplot(2,1,2)
plt.stem(np.arange(len(y1)),y1)
plt.grid()
plt.show()

