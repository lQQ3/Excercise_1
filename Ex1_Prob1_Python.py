
# coding: utf-8

# In[1]:


# Import libraries and modules
import numpy as np # Henceforth shall the library formerly known as 'numpy' be called 'np'
import scipy.stats as stats # Call the library 'scipy', and just the module 'stats'. Rename it 'stats'.
import pylab as pl # Call the library 'pylab' and rename it 'pl'


# In[2]:


# Declare variables
N = 1000 # 'N' is a constant, equaling 1000
n = 100 # 'n' is a constant equaling 100
x = np.random.normal(size=N) # Randomized Gaussian distribution utilizing 'N' number of itterations
x1 = np.random.poisson(size=n) # Randomized Poisson (predicting agents/time) distribution utilizing 'n' number of itterations


# In[3]:


# Create objects using 'x' to calculate both the x & y ranges
x_fit = np.arange(min(x), max(x), 1/(N)) # numpy.arange sets "a range".
y_fit = stats.norm.pdf(x_fit, np.mean(x), np.std(x))# scipy(library).stats(module).norm(normal continuous random variable).pdf(probability density function)
x1_fit = np.arange(min(x1), max(x1), 1/(n))# numpy.arange sets "a range".
y1_fit = stats.norm.pdf(x1_fit, np.mean(x1), np.std(x1))# scipy(library).stats(module).norm(normal continuous random variable).pdf(probability density function)


# In[4]:


# Assemble, format and display the graph
pl.subplot(1, 2, 1) # Make a 1x2 layout of plots, this is the first one
pl.plot(x_fit, y_fit, 'r.-') # Call to pylab and plot x_fit and y_fit
pl.xlabel('X Axis', fontsize = 18) # label the X axis
pl.ylabel('Y Axis', fontsize = 18) # label the Y axis
pl.hist(x, normed=True) # Create a histogram and normalize it

pl.subplot(1, 2, 2)# Make a 1x2 layout of plots, this is the second one
pl.plot(x1_fit, y1_fit, 'ko') # Call to pylab and plot x1_fit and y1_fit
pl.xlabel('Time', fontsize = 18) # label the X axis
pl.ylabel('Rate of Original Equipment Failure', fontsize = 9) # label the Y axis
pl.hist(x1, normed=True) # Create a histogram and normalize it

pl.show() # Show Plots

