import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal 
PointNum = 1000
pi = np.pi
NumeratorCof = np.array([0.008,-0.033*np.exp(-1j*2*pi),0.05*np.exp(-2j*2*pi)\
                         ,-0.033*np.exp(-3j*2*pi),0.008*np.exp(-4j*2*pi)])

DenominatorCof = np.array([1,2.37*np.exp(-1j*2*pi),2.7*np.exp(-2j*2*pi)\
                           ,1.6*np.exp(-3j*2*pi),0.41*np.exp(-4j*2*pi)])

worN = np.arange(0,4*pi,pi/(PointNum-1))
w,h = signal.freqz(NumeratorCof,DenominatorCof,worN)
#plot part 
PlotTitle = [['Real part' , 'Imaginary part'],['Magnitude Spectrum','Phase Spectrum']]
Ylabel = [['Amplitude','Amplitude'],['Amplitude','Phase radians']]
XValue = [[np.real(h),np.imag(h)],[np.abs(h),np.angle(h)]]
'''
When call subplots function that will returns fig and ax object
fig: matplotlib.figure.Figure object
ax: Axes object or array of Axes objects.
ref:https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.subplots.html
'''
fig,ax = plt.subplots(nrows=2,ncols=2)
for row in range(ax.shape[0]):
    for col in range(ax.shape[1]):
        ax[row,col].set_title(PlotTitle[row][col])
        ax[row,col].set_ylabel(Ylabel[row][col])
        ax[row,col].plot(w/pi,XValue[row][col])
        ax[row,col].set_xlabel('$\omega$/$\pi$')
plt.tight_layout()
plt.show()

