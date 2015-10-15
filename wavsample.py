
# coding: utf-8
from scipy.io import wavfile

# Read wav file
sr, src = wavfile.read('/Users/EPSO/Downloads/1.wav')
src.shape, src.dtype


import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (16, 4)
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
from matplotlib.pyplot import figure
import numpy as np
from numpy import sum
from scipy.signal import decimate
from scipy.signal import argrelextrema


# Take just the first 100K samples
src_small = np.array(src)[0:100000,:]
src_small.shape


# In[46]:

#plot(src_small)
#show()


# In[47]:

# Downmixing
src_mono = sum(src_small.astype(float)/src_small.shape[1], axis=1).astype(src_small.dtype)
src_mono.shape, src_mono.dtype


# In[48]:

# Compare the mono vs stereo
#plot(src_mono)
#figure()
#plot(src_small)
#show()


# In[49]:

# Normalize using the abs max
abs_max = max(abs(src_mono.min().astype(float)), abs(src_mono.max().astype(float)))
abs_max
src_mono_norm = src_mono.astype(float) / abs_max
src_mono_norm.shape
# Down sample
src_mono_norm_dec = decimate(src_mono_norm, 20)


# In[50]:

# Compare the downsample vs the normalized
plot(src_mono_norm_dec)
show()


# In[51]:

maxima = argrelextrema(src_mono_norm_dec, np.greater)
minima = argrelextrema(src_mono_norm_dec, np.less)
maxima, minima


# In[52]:

plot(src_mono_norm_dec)
plot(maxima[0], np.zeros_like(maxima[0]),'x')
plot(minima[0], np.zeros_like(minima[0]),'x')
show()

