import numpy as np
import matplotlib.pyplot as plt 

num = 96
seq = np.arange(0,num)
signal = np.cos(np.pi*0.25*seq)
noise = np.random.rand(num) - 0.5
NoiseAsig = signal+noise
corSignal=np.correlate(signal,NoiseAsig,'full')
#設定stem圖，並接收其回傳資料
markerline, stemlines, baseline = plt.stem(np.arange(-len(corSignal)/2, len(corSignal)/2)+1,corSignal)
#欲修改stem圖的內容，可使用plt.setp來修改
#https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp
#markerline 屬於matplotlib.lines.Line2D 之物件
#https://matplotlib.org/devdocs/api/_as_gen/matplotlib.lines.Line2D.html
#markeredgecolor 的屬性資料:
#https://matplotlib.org/devdocs/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_marker
plt.title('All Sequence')
plt.setp(markerline, 'markerfacecolor' , 'w')
plt.xlabel('Lag index')
plt.ylabel('Amplitude')
plt.show()

plt.title('Lag index -28~28')

#corSignal的size為191，所以中心點在96,但因為陣列內容從0開始，所以最大值存放在位置95
markerline, stemlines, baseline = plt.stem(np.arange(-28,29),corSignal[67:124])
plt.setp(markerline, 'markerfacecolor' , 'w')
plt.xticks(np.arange(-30,31,5))
plt.yticks(np.arange(np.ceil(min(corSignal[68:124])),np.ceil(max(corSignal[68:124])),10))
plt.xlabel('Lag index')
plt.ylabel('Amplitude')
plt.show()
