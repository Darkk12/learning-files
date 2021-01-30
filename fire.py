import plotly
import csv
from datetime import datetime

file = 'CSV files/world_fires_1_day.csv'
with open(file) as f:
    read = csv.reader(f)
    header = next(read)
    for i, j in enumerate(header):
        print(i, j)
    lon, lat, date = [], [], []
    for i in read:
        # dt = datetime.strptime(str(i[5]), '%Y-%m-%d')
        # date.append(dt)
        lon.append(i[1])
        lat.append(i[0])
data = [{'type': 'scattergeo', 'lon': lon, 'lat': lat, 'marker': {'colorscale': 'magma', 'reversescale': True, 'colorbar': {'title': 'magnitude'}}}]
my_layout = plotly.graph_objs.Layout(title = "Global Fire")
plotly.offline.plot({'data': data, 'layout': my_layout}, filename = 'HTML files/global_fire.html')