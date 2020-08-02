import numpy as np
import pandas as pd
from pandas import json_normalize
import requests


geojson = requests.get('https://opendata.arcgis.com/datasets/7c5e82ef83834de2ad2478efc86744ae_0.geojson').json()
df = json_normalize(geojson["features"])

coords = 'geometry.coordinates'
brgeodf = (df[coords].apply(lambda r: [(i[0], i[1]) for i in r[0]])
           .apply(pd.Series).stack()
           .reset_index(level=1).rename(columns={0: coords, "level_1": "point"})
           .join(df.drop(coords, 1), how='left')).reset_index(level=0)
brgeodf[['long', 'lat']] = brgeodf[coords].apply(pd.Series)

brgeodf.rename(columns={'geometry.coordinates': 'Coordinates',
                        'properties.ID': 'ID',
                        'properties.NEIGHBORHOOD': 'Neighborhood',
                        'properties.COMMUNITY': 'Community',
                        'properties.POPULATION': 'Population',
                        'properties.PLANNING_DISTRICT': 'PanningDistrict',
                        'geometry.type': 'Geometry'},
               inplace=True)

neighborhoods = list(brgeodf['Neighborhood'].unique())
neighAvgLong = []
neighAvgLat = []
communities = []

for neighborhood in neighborhoods:
    neighAvgLong.append(np.average(brgeodf.where(brgeodf['Neighborhood'] == neighborhood).dropna()['long']))
    neighAvgLat.append(np.average(brgeodf.where(brgeodf['Neighborhood'] == neighborhood).dropna()['lat']))
    communities.append(brgeodf.where(brgeodf['Neighborhood'] == neighborhood).dropna()['Community'].unique()[0])

neighdata = {"Neighborhood": neighborhoods, "Community": communities, "Lat": neighAvgLat, "Long": neighAvgLong}
avgNeighCoords_df = pd.DataFrame(data=neighdata)