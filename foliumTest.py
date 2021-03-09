import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import folium
from folium.plugins import MarkerCluster


map = folium.Map(location=[41.1461, -80.71054], zoom_start=12) #centers the map around Youngstown (longitude & latitude from custom Google map)

#Limits --------------------------------------------------------------
limits1 = "Edge of the River in Leavittsburg" #popup name
limitleavittsburg_marker = folium.Marker(location=[41.25223, -80.88751], popup=limits1).add_to(map) #creates popup at edge of river (longitude & latitude from custom Google map)

limits2 = "Edge of the River in Lowellville"
limitlowellville_marker = folium.Marker(location=[41.03095, -80.52481], popup=limits2).add_to(map)

#Dams-----------------------------------------------------------------
dam1 = "Leavittsburg Dam"
leavittsburgDam_marker = folium.Marker(location=[41.23894, -80.882], popup=dam1, icon=folium.Icon(color='darkpurple', icon='exclamation-circle', prefix='fa')).add_to(map)

dam2 = "South Main St. Dam- Warren"
southmainDam_marker = folium.Marker(location=[41.21126, -80.81502], popup=dam2, icon=folium.Icon(color='darkpurple', icon='exclamation-circle', prefix='fa')).add_to(map)

dam3 = "Girard Dam"
girardDam_marker = folium.Marker(location=[41.15459, -80.70599], popup=dam3, icon=folium.Icon(color='darkpurple', icon='exclamation-circle', prefix='fa')).add_to(map)

dam4 = "Summit St. Dam"
SummitStDam_marker = folium.Marker(location=[41.24399, -80.82719], popup=dam4, icon=folium.Icon(color='darkred', icon='exclamation-triangle', prefix='fa')).add_to(map)

dam5 = 'Crescent St. Dam/Division St. Dam- Youngstown'
Crescent_DivisionStDam_marker = folium.Marker(location=[41.1133, -80.67208], popup=dam5, icon=folium.Icon(color='darkred', icon='exclamation-triangle', prefix='fa')).add_to(map)

dam6 = 'Mahoning Ave Dam- Youngstown'
MahoningAveDam_marker = folium.Marker(location=[41.10063, -80.65597], popup=dam6, icon=folium.Icon(color='green', icon='exclamation-circle', prefix='fa')).add_to(map)

dam7 = 'Youngstown Dam'
youngstowndam_marker = folium.Marker(location=[41.07674, -80.6172], popup=dam7, icon=folium.Icon(color='green', icon='exclamation-circle', prefix='fa')).add_to(map)

dam8 = 'Struthers Dam'
struthersdam_marker = folium.Marker(location=[41.06184, -80.58931], popup=dam8, icon=folium.Icon(color='darkpurple', icon='exclamation-circle', prefix='fa')).add_to(map)


map #not sure what this does


map.save('foliumDemo.html') #save the map as html file to view in browser