import numpy as np
import pandas as pd
import folium as fo


map = fo.Map()

x = fo.FeatureGroup(name= "My Map")
x.add_child(fo.Marker(location=[80,70], popup = "jai ho", icon=fo.Icon(color= "red")))
map.add_child(x)

volcano = pd.read_csv("volcano.csv")

lat_vo = list(volcano["Latitude"])
lon_vo = list(volcano["Longitude"])
name_vo = list(volcano["Name"])

vol = fo.FeatureGroup(name= "My Map")

for lat,lon,name in zip(lat_vo,lon_vo,name_vo):
    vol.add_child(fo.Marker(location=[lat,lon], popup = name, icon=fo.Icon(color= "red")))

map.add_child(vol)

vol.add_child(fo.GeoJson(data=(open("world.json", "r", encoding= "utf-8-sig").read())))
map.add_child(vol)


# OTHER PROJECT ON US POPULATION

# popu = pd.read_csv("us cities pop.csv")
# popu.head()

# lat_po = list(popu["lat"])
# lon_po = list(popu["lon"])
# name_po = list(popu["name"])
# pop_po = list(popu["pop"])

# po = fo.FeatureGroup(name= "my map")
# for lat,lon,name,pop in zip(lat_po,lon_po,name_po,pop_po):
#     po.add_child(fo.Marker(location=[lat,lon],popup= [pop,name], icon= fo.Icon(color= "red")))

# map.add_child(po)