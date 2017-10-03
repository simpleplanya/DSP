import numpy as np 
import matplotlib.pyplot as plt 

seq1 = np.array([1,3,-2,1,2,-1,4,4,2])
seq2 = np.array([2,-1,4,1,-2,3])
#inverse sequence
r=np.correlate(seq1,seq2,'full')
#plot part'
plt.title('Cross-Correlation')
plt.xlabel('Lag index')
plt.ylabel('Amplinude')
plt.xticks(np.arange(-len(seq2)+1,len(seq1)))
plt.yticks(np.arange(min(r),max(r)+5,5))
plt.stem(np.arange(-len(seq2)+1,len(seq1)),r)
plt.show()
