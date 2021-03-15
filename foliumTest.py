#Instructions: 1) run this code. It should save a file called "foliumDemo.html" in the folder where you saved this python code. 2) open the html file 3) your browser will show you the map. If you make changes to the code, you have to run the code and see the changes by opening the html file.
# if it doesn't work, you didn't install all the packages (see comment after this for packages)

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import folium
from folium.plugins import MarkerCluster

#packages to install: folium ("pip install folium" if you're using Mac), geojson ("pip install geojson"), and json ("pip install json"). Code should run after this.

#so right below this is asection using this thing called geojson where the problem is. You can see that n=6 means it's making a 6 squares x 6 squares grid. We want to figure out how to change it to 0.5 mi between each square. I tried Googling "geojson distance" and can't figure out how I might make the changes.
# i got this section of the code from https://www.jpytr.com/post/analysinggeographicdatawithfolium/

def get_geojson_grid(upper_right, lower_left, n=6): 
    """Returns a grid of geojson rectangles, and computes the exposure in each section of the grid based on the vessel data.

    Parameters
    ----------
    upper_right: array_like
        The upper right hand corner of "grid of grids" (the default is the upper right hand [lat, lon] of the USA).

    lower_left: array_like
        The lower left hand corner of "grid of grids"  (the default is the lower left hand [lat, lon] of the USA).

    n: integer
        The number of rows/columns in the (n,n) grid.

    Returns
    -------

    list
        List of "geojson style" dictionary objects   
    """

    all_boxes = []

    lat_steps = np.linspace(upper_right[0], lower_left[0], n+1)
    lon_steps = np.linspace(upper_right[1], lower_left[1], n+1)

    lat_stride = lat_steps[1] - lat_steps[0]
    lon_stride = lon_steps[1] - lon_steps[0]

    for lat in lat_steps[:-1]:
        for lon in lon_steps[:-1]:
            # Define dimensions of box in grid
            upper_left = [lon, lat + lat_stride]
            upper_right = [lon + lon_stride, lat + lat_stride]
            lower_right = [lon + lon_stride, lat]
            lower_left = [lon, lat]

            # Define json coordinates for polygon
            coordinates = [
                upper_left,
                upper_right,
                lower_right,
                lower_left,
                upper_left
            ]

            geo_json = {"type": "FeatureCollection",
                        "properties":{
                            "lower_right": lower_right,
                            "upper_left": upper_left
                        },
                        "features":[]}

            grid_feature = {
                "type":"Feature",
                "geometry":{
                    "type":"Polygon",
                    "coordinates": [coordinates],
                }
            }

            geo_json["features"].append(grid_feature)

            all_boxes.append(geo_json)

    return all_boxes

upper_left = [41.27237, -80.88808] #coordinates for upper left corner of map
lower_right = [41.03095, -80.52481] #coordinates for lower right coner of map
map = folium.Map(zoom_start = 12, location=[41.1461, -80.71054]) #This is the central point of the map and sets how far to zoom in
grid = get_geojson_grid(upper_left, lower_right , n=6) #determines how many squares in the grid

for i, geo_json in enumerate(grid):

    color = plt.cm.Reds(i / len(grid))
    color = mpl.colors.to_hex(color)

    gj = folium.GeoJson(geo_json,
                        style_function=lambda feature, color=color: {
                                                                        'fillColor': color,
                                                                        'color':"black",
                                                                        'weight': 2,
                                                                        'dashArray': '5, 5',
                                                                        'fillOpacity': 0.35,
                                                                    })
    popup = folium.Popup("example popup {}".format(i))
    gj.add_child(popup)

    map.add_child(gj)

#Limits --------------- ---------------- ---------------- ----------------
limits1 = "Edge of the River in Leavittsburg" #popup name
limitleavittsburg_marker = folium.Marker(location=[41.25223, -80.88751], popup=limits1).add_to(map) #creates popup at edge of river (longitude & latitude from custom Google map)

limits2 = "Edge of the River in Lowellville"
limitlowellville_marker = folium.Marker(location=[41.03095, -80.52481], popup=limits2).add_to(map) #creates popup at edge of river (longitude & latitude from custom Google map)

#Dams ---------------- ---------------- ---------------- ----------------

#Adds markers for dams to the map
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

'''
IGNORE THIS SECTION ---------------- ---------------- ---------------- -------------------------------- ---------------- ---------------- ----------------

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
'''

map #not sure what this does


map.save('foliumDemo.html') #save the map as html file to view in browser
