#https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.convolve.html

#§ï¤T­Ó¹Ï
import numpy as np 
import matplotlib.pyplot as plt
x_seq = np.array([0,0,0,0,-2,0,1,-1,3,0,0,0,0])
h_seq = np.array([0,0,0,1,2,0,-1,0,0,0])    
y_seq = np.convolve(x_seq,h_seq)
markerline, stemlines, baseline=plt.stem(np.arange(-7,15),y_seq)
plt.setp(markerline, 'markerfacecolor' , 'w')
plt.title('Convolution Sum y[n]')
plt.xticks(np.arange(-7,15))
#設定y軸刻度
plt.yticks(y_seq)
plt.xlabel('The index n')
plt.ylabel('Amplitude')
plt.show()
