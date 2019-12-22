'''
Converting inexact addresses to latitude and longitude coordinates
'''


import numpy as np
import pandas as pd
from geopy.geocoders import GoogleV3
import pygeoj


#Load incidents data
jun_dec18 = pd.read_csv("May23-Dec-2018-Fire.csv")


#Create a api key with Google
geolocator = GoogleV3(api_key = "your_key")

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


#Load coordinates to a csv file for plottign
points.to_csv("Jun_Dec18FireIncients1.csv")


# Now we create an intensity map by counting how many incidents fall within each grid

f = pygeoj.load("grids_w_zoneNum.json")



jan_dict = {grid : 0 for grid in range(1187)}
for i in range(len(f)):
    feature = f[i]
    coords = feature.geometry.coordinates
    bbpath = mplPath.Path(coords[0])
    for j in range(len(points["lng"])):
        if bbpath.contains_point((points["lng"][j], points["lat"][j])):
            jan_dict[i] += 1


# Load intensity map into csv file for plotting

jd18 = pd.DataFrame({"Intensity": [i for i in jan_dict.values()]})
jd18.to_csv("intensity_JunDec18.csv")






