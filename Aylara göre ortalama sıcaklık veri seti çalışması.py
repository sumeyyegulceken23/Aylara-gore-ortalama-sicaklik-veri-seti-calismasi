#!/usr/bin/env python
# coding: utf-8

# In[91]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[92]:


aylar = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
ortalama_Sıcaklık=[5.2, 6.7, 9.9, 13.6, 18.2, 22.1, 25.5, 25.3, 21.7, 16.2, 10.5, 6.8]
data = {'aylar': aylar, 'ortalama sıcaklık': ortalama_Sıcaklık}
df = pd.DataFrame(data)
df


# In[93]:


plt.figure(figsize=(12, 8)) 
plt.plot(df["aylar"],df["ortalama sıcaklık"],marker="o",color="red")
plt.title("Aylara göre ortalama sıcaklık değerleri")
plt.xlabel("aylar")
plt.ylabel("ortalama sıcaklık")
plt.xticks(rotation=30)
plt.show()


# # Temel istatislik işlemleri

# In[38]:


mean_temp = df['ortalama sıcaklık'].mean()
print("Ortalama sıcaklık:", mean_temp)


# In[39]:


median_temp=df["ortalama sıcaklık"].median()
print("median:",median_temp)


# In[44]:


max_temp=df["ortalama sıcaklık"].max()
print("maximum sıcaklık:",max_temp)


# In[46]:


min_temp=df["ortalama sıcaklık"].min()
print("minumun sıcaklık:",min_temp)


# In[47]:


std_dev = df['ortalama sıcaklık'].std()
print("Standard Deviation:", std_dev)


# In[94]:


plt.figure(figsize=(17, 7))
a=sns.histplot(data=data,x="aylar",hue="ortalama sıcaklık",bins=12,alpha=0.5,color="red")


# In[77]:


plt.figure(figsize=(17,7))
b=sns.scatterplot(data=data,x="aylar",y="ortalama sıcaklık",s=150)
b


# In[80]:


plt.figure(figsize=(17,7))
d=sns.barplot(data=data,x="aylar",y="ortalama sıcaklık")
d


# In[ ]:




