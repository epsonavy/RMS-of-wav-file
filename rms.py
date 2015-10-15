
# coding: utf-8

# In[1]:

#3. Given that the downmixed normalized sample is a single dimensional array of
#values between +1 and -1, Implement a function that calculates the RMS or root 
#mean square of the values. Use this function on tracks of same artist/genre and 
#compare.
from scipy.io import wavfile

sr, src = wavfile.read('/Users/EPSO/Downloads/1.wav')
src.shape, src.dtype


# In[2]:

import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (16, 4)
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
from matplotlib.pyplot import figure
import numpy as np
from numpy import sum
from scipy.signal import decimate
from scipy.signal import argrelextrema


# In[3]:

# Take just the first 100K samples
src_small = np.array(src)[0:100000,:]
src_small.shape


# In[4]:

# Downmixing
src_mono = sum(src_small.astype(float)/src_small.shape[1], axis=1).astype(src_small.dtype)
src_mono.shape, src_mono.dtype


# In[5]:

# Normalize using the abs max
abs_max = max(abs(src_mono.min().astype(float)), abs(src_mono.max().astype(float)))
abs_max
src_mono_norm = src_mono.astype(float) / abs_max
src_mono_norm.shape
# Down sample
src_mono_norm_dec = decimate(src_mono_norm, 20)


# In[16]:

# normalized array
src_mono_norm
#plot(src_mono_norm)
#show()


# In[31]:

#This function return root mean square of the list"
def rms(list):
    sum = 0
    for e in list:
        sum += e**2
    sum = np.sqrt(sum / len(list))
    return sum;
rms(src_mono_norm)
