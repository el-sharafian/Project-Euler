#!/usr/bin/env python
# coding: utf-8

# In[26]:


import math


# In[50]:


def sumOfSquares(n1, n2):
    sum = 0
    for i in range(n1, n2+1):
        sum += math.pow(i, 2)
    return sum

def squareOfSum(n1 ,n2):
    sum = 0
    for i in range(n1, n2+1):
        sum += i
    sum = math.pow(sum, 2)
    return sum


# In[51]:


sumOfSquare = sumOfSquares(1, 100)
squareofSum = squareOfSum(1, 100)
print(squareofSum - sumOfSquare)

