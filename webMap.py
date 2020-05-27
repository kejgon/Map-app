import folium
import pandas

# folium is converted python code to html, css, and js code
# also you need html, css, js to create the web map
# -1.301674, 36.767820
# Reading the Data Frame file
data = pandas.read_csv("files/Volcanoes.csv")
# Accessing sub columns in the Data Frame File. which are longitude and Langitude
lat = list(data["LAT"])
lon = list(data["LON"])
elv = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")


# the great way to add children is to add feature group

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


fgv = folium.FeatureGroup(name="Volcano")

# Now you loop through the the lan and lon, you use the zip() function to loop through the two or more list

for lt, ln, el in zip(lat, lon, elv):
    fgv.add_child(folium.CircleMarker(location=(lt, ln), radius=6, popup=str(el) + " M", fill_color=color_producer(el),
                                     color='gray', fill_opacity='0.7'))

fg = folium.FeatureGroup(name="Population")

fg.add_child(folium.GeoJson(data=open('files/world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Map1.html")
