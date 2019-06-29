
# coding: utf-8

# In[1]:


# Shawn Rice
# 4/29/18
# This will simulate the 'Monte Hall' problem


# In[2]:


# Import libraries
import random


# In[3]:


# How many times should we play?
rounds = 100000
# Set stage
# Create win\loss count containers
wins = 0
losses = 0
# Create doors
doors = [1, 2, 3]
# Randomize winning door
n = random.randint(1, 3)
winningDoor = n


# In[4]:


# Let's play
# Set number of rounds to run
for i in range(rounds):
    # Select door as a uniform randomized distribution
    d = random.choice(doors)
    doorSelected = d
    # Compare to winning door
    if doorSelected == winningDoor:
        # If losing; increase losses count and change selected door
        losses = losses+1
        d = random.choice(doors)
        doorSelected = d
    else:
        # If winning; increase winning count, end round, and if remaining unplayed rounds then restart
        wins = wins+1
        n = random.randint(1, 3)
        winningDoor = n


# In[5]:


# Output
# Display number of wins and losses
print("Wins:") 
print(wins)
print("Losses:")
print(losses)
# Turn Wins and Losses to percentages
pcent = (100.0 * wins)/(wins + losses)
# Show end percentage of wins by changing
print("By changing doors every time, you won", pcent ,"of the time.")

