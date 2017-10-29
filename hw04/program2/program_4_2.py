import numpy as np 
import matplotlib.pyplot as plt

#create two sequences
x1=[3,6,7,1,2,0,0]
x2=[3,6,7,1,2,8,10]
#LTI system h[n]
h = [1,2,3]
y1=np.convolve(x1,h)
y2=np.convolve(x2,h)
plt.subplot(2,1,1)
plt.stem(range(len(y1)),y1)
plt.title('$y_1[n]$')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
y_tick=[i for i in range(0,41,5)]
plt.yticks(y_tick)
plt.grid()

plt.subplot(2,1,2)
plt.stem(range(len(y2)),y2)
plt.title('$y_2[n]$')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.yticks(y_tick)
plt.grid()
plt.tight_layout()
plt.show()

