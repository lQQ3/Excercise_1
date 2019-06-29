
# coding: utf-8

# In[1]:


#Import libraries
import scipy as sp
# Got an error saying: "module 'scipy' has no attribute 'stats'". This imports stats implicitly.
from scipy import stats  
import pandas as pd


# In[2]:


# Declare constant and give it a value
Total_Flips = 10 
# Return evenly spaced numbers over a specified interval: (start, stop, increase flip count)
Heads = sp.linspace(0, Total_Flips, Total_Flips+1) 
# Binomial.Probability_Mass_Function (location, number, probability)
Probability = sp.stats.binom.pmf(Heads, Total_Flips, 0.5) 


# In[3]:


# df is now a DataFrame object which holds Probability as the contents
df = pd.DataFrame(data=Probability, columns=["Probability"])
# This titles the column
df.index.names = ["Heads"]
# Show it
print(df)

