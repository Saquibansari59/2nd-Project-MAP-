from os import read
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev= list(data["ELEV"])

def colour(elevation):
    if elevation < 900:
        return "green"
    elif 900 <= elevation <=2700:
        return "blue"
    else:
        return "red"

map = folium.Map(location=[22.555778964673742, 88.36152496592742],zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+" m",
    fill_colour=colour(el), colour= "grey", fill_capacity = 0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
style_function=lambda x: {'fillcolour':'green' if x['properties']['POP2005']<10000000 
else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
print("Hello Saquib")
