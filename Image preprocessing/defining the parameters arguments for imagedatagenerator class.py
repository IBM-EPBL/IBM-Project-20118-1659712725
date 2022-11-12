#!/usr/bin/env python
# coding: utf-8

# In[1]:


import keras
from keras.preprocessing.image import ImageDataGenerator


# In[2]:


rain_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,rotation_range=180,zoom_range=0.2,horizontal_flip=True)

test_datagen=ImageDataGenerator(rescale=1./255)


# In[ ]:




