import json
from plotly.graph_objs import Layout
from plotly import offline

file = 'Json files/eq_data_30_day_m1.json'
with open(file) as f:
    datas = json.load(f)
title = datas['metadata']['title']
datas = datas['features']
mag = [value['properties']['mag'] for value in datas]
lon = [value['geometry']['coordinates'][0] for value in datas]
lat = [value['geometry']['coordinates'][1] for value in datas]
hover_texts = [value['properties']['title'] for value in datas]

# data = [Scattergeo(lon = lon, lat = lat)]
data = [{'type': 'scattergeo', 'lon': lon, 'lat': lat, 'text': hover_texts, 'marker': {'size': [3 * mags for mags in mag],
                    'color': mag, 'colorscale': 'Inferno', 'reversescale': True, 'colorbar': {'title': 'Magnitude'}}}]
my_layout = Layout(title = title)
offline.plot({'data': data, 'layout': my_layout}, filename = 'HTML files/eq.html')


# readfile = 'Json files/readable_eq_data.json'
# with open(readfile, 'w') as f:
#     json.dump(data, f, indent=4)
