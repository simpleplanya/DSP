import numpy as np 
import matplotlib.pyplot as plt

#create two sequences
x1=[3,6,7,1,2,0,0]
x2=[3,6,7,1,2,8,10]
#LTI system h[n]
h = [1,2,3]
y1=np.convolve(x1,h)
y2=np.convolve(x2,h)
#draw y1
plt.stem(range(len(y1)),y1,label='$y_1[n]$')
plt.title('Causal system')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
#draw y2
plt.stem(range(len(y2)),y2,label='$y_2[n]$',markerfmt='ro')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

