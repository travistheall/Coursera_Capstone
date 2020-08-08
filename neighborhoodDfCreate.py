import numpy as np
import pandas as pd
from pandas import json_normalize
import requests

geojson = requests.get('https://opendata.arcgis.com/datasets/7c5e82ef83834de2ad2478efc86744ae_0.geojson').json()
geojson_df = json_normalize(geojson["features"])

coords = 'geometry.coordinates'

brgeodf = (geojson_df[coords].apply(lambda r: [(i[0], i[1]) for i in r[0]])
           .apply(pd.Series).stack()
           .reset_index(level=1).rename(columns={0: coords, "level_1": "point"})
           .join(geojson_df.drop(coords, 1), how='left')).reset_index(level=0)
brgeodf[['Longitude', 'Latitude']] = brgeodf[coords].apply(pd.Series)
brgeodf.rename(columns={'geometry.coordinates': 'Coordinates',
                        'properties.ID': 'ID',
                        'properties.NEIGHBORHOOD': 'Neighborhood',
                        'properties.COMMUNITY': 'Community',
                        'properties.POPULATION': 'Population',
                        'properties.PLANNING_DISTRICT': 'PanningDistrict',
                        'geometry.type': 'Geometry'},
               inplace=True)

brgeodf.to_excel('BatonRougeGeometryDf.xlsx')

neighData = {"Neighborhood": [],
             "Community": [],
             "Population": [],
             "Max Latitude": [],
             "Max Latitude Coordinate": [],
             "Min Latitude": [],
             "Min Latitude Coordinate": [],
             "Center Latitude": [],
             "Max Longitude": [],
             "Max Longitude Coordinate": [],
             "Min Longitude": [],
             "Min Longitude Coordinate": [],
             "Center Longitude": [],
             'Radius': []}

neighborhoods = list(brgeodf['Neighborhood'].unique())


def find_dist_in_meters(lat1, lat2, lon1, lon2):
    r = 6371000  # meters
    phi1 = lat1 * np.pi / 180  # phi, lamda in radians
    phi2 = lat2 * np.pi / 180
    delta_phi = (lat2 - lat1) * np.pi / 180
    delta_lamda = (lon2 - lon1) * np.pi / 180
    a = np.sin(delta_phi / 2) * np.sin(delta_phi / 2) + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lamda / 2) * np.sin(
        delta_lamda / 2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    meters = r * c  # in meters
    return meters


for neighborhood in neighborhoods:
    neighData["Neighborhood"].append(neighborhood)
    community = brgeodf.where(brgeodf['Neighborhood'] == neighborhood).dropna()['Community'].unique()[0]
    neighData["Community"].append(community)
    population = brgeodf.where(brgeodf['Neighborhood'] == neighborhood).dropna()['Population'].unique()[0]
    neighData["Population"].append(population)

    neighLatMaxX = brgeodf.where(brgeodf['Neighborhood'] == neighborhood).dropna()['lat'].max()
    neighData["Max Latitude"].append(neighLatMaxX)
    neighLatMaxLong = brgeodf.where(brgeodf['lat'] == neighLatMaxX).dropna()['long'].iloc(0)[0]
    neighLatMaxCoord = (neighLatMaxX, neighLatMaxLong)
    neighData["Max Latitude Coordinate"].append(neighLatMaxCoord)

    neighLatMinX = brgeodf.where(brgeodf['Neighborhood'] == neighborhood).dropna()['lat'].min()
    neighData["Min Latitude"].append(neighLatMinX)
    neighLatMinLong = brgeodf.where(brgeodf['lat'] == neighLatMinX).dropna()['long'].iloc(0)[0]
    neighLatMinCoord = (neighLatMinX, neighLatMinLong)
    neighData["Min Latitude Coordinate"].append(neighLatMinCoord)

    neighLatCenterX = np.add(neighLatMinX, np.divide(np.subtract(neighLatMaxX, neighLatMinX), 2))
    neighData["Center Latitude"].append(neighLatCenterX)

    neighLongMaxY = brgeodf.where(brgeodf['Neighborhood'] == neighborhood).dropna()['long'].max()
    neighData["Max Longitude"].append(neighLongMaxY)
    neighLongMaxLat = brgeodf.where(brgeodf['long'] == neighLongMaxY).dropna()['lat'].iloc(0)[0]
    neighLongMaxCoord = (neighLongMaxLat, neighLongMaxY)
    neighData["Max Longitude Coordinate"].append(neighLongMaxCoord)

    neighLongMinY = brgeodf.where(brgeodf['Neighborhood'] == neighborhood).dropna()['long'].min()
    neighData["Min Longitude"].append(neighLongMinY)
    neighLongMinLat = brgeodf.where(brgeodf['long'] == neighLongMinY).dropna()['lat'].iloc(0)[0]
    neighLongMinCoord = (neighLongMinLat, neighLongMinY)
    neighData["Min Longitude Coordinate"].append(neighLongMinCoord)

    neighLongCenterY = np.add(neighLongMinY, np.divide(np.subtract(neighLongMaxY, neighLongMinY), 2))
    neighData["Center Longitude"].append(neighLongCenterY)

    radiusChoice1 = abs(neighLatMaxX - neighLatMinX)
    radiusChoice2 = abs(neighLongMaxY - neighLongMinY)

    if radiusChoice1 > radiusChoice2:
        neighData['Radius'].append(find_dist_in_meters(neighLatMaxCoord[0],
                                                       neighLatMinCoord[0],
                                                       neighLatMaxCoord[1],
                                                       neighLatMinCoord[1]) / 2)
    else:
        neighData['Radius'].append(find_dist_in_meters(neighLongMaxCoord[0],
                                                       neighLongMinCoord[0],
                                                       neighLongMaxCoord[1],
                                                       neighLongMinCoord[1]) / 2)

neighCenterData = pd.DataFrame(data=neighData)
neighCenterData.to_excel(excel_writer="NeighborhoodMaxMinCenter.xlsx")
brMaxLatX = neighCenterData["Max Latitude"].max()
brMinLatX = neighCenterData["Min Latitude"].min()
brMaxLongY = neighCenterData["Max Longitude"].max()
brMinLongY = neighCenterData["Min Longitude"].min()
brCenterLat = np.add(brMinLatX, np.divide(np.subtract(brMaxLatX, brMinLatX), 2))
brCenterLong = np.add(brMinLongY, np.divide(np.subtract(brMaxLongY, brMinLongY), 2))

neighCenterData = pd.read_excel('NeighborhoodMaxMinCenter.xlsx')
