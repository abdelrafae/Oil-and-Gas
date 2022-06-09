#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from ipywidgets import interact, interactive
from IPython.display import clear_output, display, HTML


# In[ ]:


plt.style.use('default')

plt.figure(figsize=(12,4))


# In[ ]:


def flowprofile(k,mu,q,Bo):

  re = 3000
  rw = 0.5

  r = np.linspace(rw,re,500)

  pe = 4000

  B = 1

  h = 30 #ft

  P = pe - (141.2*q*mu*Bo*(np.log(re/r))/k/h)

  y_min = P[np.where(r==rw)]



  plt.plot(r,P,linewidth=2,color='red')
  plt.axhline(y_min,linewidth=2,color='black')

  plt.ylim(0,7000)

  plt.xlabel('r(ft)')
  plt.ylabel('P(r), Psi')

  plt.title('Reservoir Pressure Profile')

  plt.grid()

  return r,P


# In[ ]:


w = interactive(flowprofile, k = (10,1000), mu=(10,300), q = (100,200), Bo = (0.9,1.4))


# In[ ]:


display(w)


# In[ ]:




