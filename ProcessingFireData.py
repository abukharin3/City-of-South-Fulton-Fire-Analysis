#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from geopy.geocoders import GoogleV3
import pygeoj


# In[ ]:


jun_dec18 = pd.read_csv("May23-Dec-2018-Fire.csv")


# In[6]:


geolocator = GoogleV3(api_key = "AIzaSyBhyJESOr7d1aQxZN44es3t8XMLWdwUw3o")


# In[10]:


lat = []
lng = []
for point in jun_dec18["Street"]:
    try:
        location = geolocator.geocode(point + "South Fulton", timeout = 3)
        lng.append(location.longitude)
        lat.append(location.latitude)
    except:
        continue
points = pd.DataFrame({"lat": lat, "lng": lng})


# In[11]:


points.to_csv("Jun_Dec18FireIncients1.csv")


# # Now we create an intensity map

# In[12]:


f = pygeoj.load("grids_w_zoneNum.json")


# In[14]:


jan_dict = {grid : 0 for grid in range(1187)}
for i in range(len(f)):
    feature = f[i]
    coords = feature.geometry.coordinates
    bbpath = mplPath.Path(coords[0])
    for j in range(len(points["lng"])):
        if bbpath.contains_point((points["lng"][j], points["lat"][j])):
            jan_dict[i] += 1


# In[20]:


jd18 = pd.DataFrame({"Intensity": [i for i in jan_dict.values()]})
jd18.to_csv("intensity_JunDec18.csv")


# In[ ]:




