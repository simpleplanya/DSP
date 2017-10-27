import numpy as np 
import matplotlib.pyplot as plt

#create two sequences
x1=[3,6,7,1,2,0,0]
x2=[3,6,7,1,2,8,10]

plt.subplot(2,1,1)
plt.stem(range(len(x1)),x1)
plt.title('$x_1[n]$')
plt.xlabel('The index n')
plt.ylabel('Amplitude')
plt.yticks(range(0,12,2))
plt.subplot(2,1,2)
plt.stem(range(len(x2)),x2)
plt.title('$x_2[n]$')
plt.xlabel('The index n')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()

