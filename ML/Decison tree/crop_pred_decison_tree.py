#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[18]:


dataset = pd.read_csv("D:/Datasets/crop.csv")


# In[19]:


dataset.shape


# In[20]:


dataset.head()


# In[21]:


X=dataset.drop('Crop',axis=1)
y=dataset['Crop']


# In[22]:


X.head()


# In[23]:


y.head()


# In[24]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


# In[25]:


from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)


# In[26]:


y_pred = classifier.predict(X_test)


# In[27]:


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


# In[55]:


print('Enter temp, humidity and moisture')


# In[ ]:


temp,hum,mois=input()


# In[ ]:


Xnew = [[temp, hum, mois]]


# In[ ]:


ynew = classifier.predict(Xnew)


# In[ ]:


print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))


# In[ ]:





# In[ ]:




