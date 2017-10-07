import numpy as np
import matplotlib.pyplot as plt


alpha = 1.2
amplitude = 0.25
# sequence len
N =30 
# create sequence
n = np.arange(N)
plt.subplot(2,1,1)
plt.stem(n,amplitude*alpha**n)
alpha = 0.9
amplitude = 20
plt.subplot(2,1,2)
plt.stem(n,amplitude*alpha**n)
plt.show()

