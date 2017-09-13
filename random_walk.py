
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt


# In[2]:

pos = 0 #postion to be changed over time


# In[3]:

walk = [pos] #history of pos to be saved after each step


# In[4]:

steps = 1000


# In[5]:

seed = np.random.randint(0, high=2, size=steps) #array of random 0's and 1's


# In[6]:

#check each element of random array where 1 --> +step
for i in range(steps):
    if seed[i] == 1:
        step = 1 
    else: step = -1
    pos += step
    walk.append(pos) #recording pos over time


# In[7]:

walk[990:] #checking position at last 10 steps


# In[8]:

plt.plot(walk) #creating plot
plt.title('Random Walk')
plt.show()

