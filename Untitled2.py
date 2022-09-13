#!/usr/bin/env python
# coding: utf-8

# In[1]:


#download vital python libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


#read the data from the csv file
gender = pd.read_csv"https://raw.githubusercontent.com/Irodakhanim/Irodakhanim/main/gender-gap-in-primary-education.csv", delimiter=";"
gender


# In[3]:


gender = pd.read_csv("https://raw.githubusercontent.com/Irodakhanim/Irodakhanim/main/gender-ratios-for-mean-years-of-schooling.csv",delimiter=";")
gender


# In[4]:


primary = pd.read_csv("https://raw.githubusercontent.com/Irodakhanim/Irodakhanim/main/primary-completion-rate-gender-parity-index.csv",delimiter=";")
primary


# In[13]:


#Can we see that from the given chart the total number of people aged 15+ with no education in millions by continent 1970-2050
import matplotlib.pyplot as plt

labels = 'Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America'
sizes = [108.5529022, 543.0627898, 38.40432161, 17.69630628, 0.435840983, 27.23616332]
explode = (0, 0.25, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Asia')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# In[ ]:




