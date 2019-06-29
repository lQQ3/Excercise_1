
# coding: utf-8

# In[1]:


#Import libraries
import numpy as np


# In[2]:


# Does a 50/50 coin flip, 0 = Heads, 1 = Tails
def coin_flip():
    return(np.random.randint(low=0, high=2))

tail_count = 0

flip = coin_flip()

while flip == 0:
    print(flip)
    tail_count+=1
    flip = coin_flip()
    
print('Number of tails until a heads was rolled: ', tail_count)

