'''dsp homework 1  '''
import numpy as np 
import matplotlib.pyplot as plt 

Num = 50
seq = np.arange(0,Num,1)
Signal = 2*seq*(0.9**seq)
#signal為陣列，使用np.newaxis 將其改變成矩陣
Signal = Signal[:,np.newaxis]
#create random matrix ,dim is 50*1 and each element value between [0,1)  
Noise = np.random.rand(Num,1)-0.5
NoiseAsig = Signal+Noise
#plot part
plt.subplot(2,2,1)
plt.title('Orginal signal')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.stem(seq,Signal)

plt.subplot(2,2,2)
plt.title('Noise')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.stem(seq,Noise)

plt.subplot(2,2,3)
plt.title('Nosie corrupted signal')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.stem(seq,Signal+Noise)

#Ensemble average
for i in range (0,50,1):
    Noise = np.random.rand(Num,1)-0.5
    temp=Signal+Noise
    NoiseAsig=NoiseAsig+temp
NoiseAsig=NoiseAsig/50

plt.subplot(2,2,4)
plt.title('Ensemble average')
plt.xlabel('Time index')
plt.ylabel('Amplitude')
plt.stem(seq,NoiseAsig)

#自動調整子圖間的間距
plt.tight_layout()
plt.show()
