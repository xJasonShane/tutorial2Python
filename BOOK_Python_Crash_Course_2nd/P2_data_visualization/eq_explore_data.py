import json

# 探索数据的结构
filename = 'BOOK Python-Crash-Course/P2 data visualization/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

# print(mags[:10])
# print(titles[:2])
# print(lons[:5])
# print(lats[:5])

# readable_file = 'BOOK Python-Crash-Course\P2 data visualization\\readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

import plotly.express as px

fig = px.scatter(
    x=lons,
    y=lats,
    labels={"x": "经度", "y": "维度"},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title="全球地震散点图",
)

fig.write_html("BOOK Python-Crash-Course/P2 data visualization/global_earthquakes.html")
fig.show()
