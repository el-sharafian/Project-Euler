#!/usr/bin/env python
# coding: utf-8

# In[17]:


import math
def LCD(a, b):
    gcd = math.gcd(a ,b)
    lcd = a*b / gcd
    return int(lcd)


# In[25]:


a = 1
for i in range(20):
    print(a, 'when i is: ', i)
    a = LCD(a, i+1)


# In[ ]:




