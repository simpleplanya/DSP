import numpy as np
import matplotlib.pyplot as plt 

num = 96
seq = np.arange(0,num)
signal = np.cos(np.pi*0.25*seq)
noise = np.random.rand(num) - 0.5
NoiseAsig = signal+noise
corSignal=np.correlate(signal,NoiseAsig,'full')
#�]�wstem�ϡA�ñ�����^�Ǹ��
markerline, stemlines, baseline = plt.stem(np.arange(-len(corSignal)/2, len(corSignal)/2)+1,corSignal)
#���ק�stem�Ϫ����e�A�i�ϥ�plt.setp�ӭק�
#https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp
#markerline �ݩ�matplotlib.lines.Line2D ������
#https://matplotlib.org/devdocs/api/_as_gen/matplotlib.lines.Line2D.html
#markeredgecolor ���ݩʸ��:
#https://matplotlib.org/devdocs/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_marker
plt.title('All Sequence')
plt.setp(markerline, 'markerfacecolor' , 'w')
plt.xlabel('Lag index')
plt.ylabel('Amplitude')
plt.show()

plt.title('Lag index -28~28')

#corSignal��size��191�A�ҥH�����I�b96,���]���}�C���e�q0�}�l�A�ҥH�̤j�Ȧs��b��m95
markerline, stemlines, baseline = plt.stem(np.arange(-28,29),corSignal[67:124])
plt.setp(markerline, 'markerfacecolor' , 'w')
plt.xticks(np.arange(-30,31,5))
plt.yticks(np.arange(np.ceil(min(corSignal[68:124])),np.ceil(max(corSignal[68:124])),10))
plt.xlabel('Lag index')
plt.ylabel('Amplitude')
plt.show()
