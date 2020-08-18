import numpy as np
import pandas as pd
from pandas import json_normalize

import requests
import json

avgNeighCoords_df = pd.read_excel('data/NeighborhoodMaxMinCenter.xlsx')

brMaxLatX = neighCenterData["Max Latitude"].max()
brMinLatX = neighCenterData["Min Latitude"].min()
brMaxLongY = neighCenterData["Max Longitude"].max()
brMinLongY = neighCenterData["Min Longitude"].min()

brCenterLat = np.add(brMinLatX, np.divide(np.subtract(brMaxLatX, brMinLatX), 2))
brCenterLong = np.add(brMinLongY, np.divide(np.subtract(brMaxLongY, brMinLongY), 2))

CLIENT_ID='XLQ4AOQ1EPWQSLRZTS2J253I2KIEUF5QOIC3TEQ2T2HKCQIW'
CLIENT_SECRET = 'CZ2KUW1Z2FQ2VI3B5AOUTXNKL3BWPBODJ2XVEYCBPUZQZ3AR'

def getNearbyVenues(names, radius, latitudes, longitudes):
    section = 'food'
    sortByPopularity = 1
    VERSION = '20200805'
    venues_list = []
    for name, radius, lat, lng in zip(names, radius, latitudes, longitudes):
        # create the API request URL
        url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={},section={},limit={},&sortByPopularity={}'.format(
            CLIENT_ID,
            CLIENT_SECRET,
            VERSION,
            lat,
            lng,
            radius,
            section,
            LIMIT,
            sortByPopularity)

        # make the GET request
        results = requests.get(url).json()["response"]['groups'][0]['items']

        # return only relevant information for each nearby venue
        venues_list.append([(
            name,
            lat,
            lng,
            v['venue']['name'],
            v['venue']['location']['lat'],
            v['venue']['location']['lng'],
            v['venue']['categories'][0]['name']) for v in results])

    nearby_venues = pd.DataFrame([item for venue_list in venues_list for item in venue_list])
    nearby_venues.columns = ['Neighborhood',
                             'Neighborhood Latitude',
                             'Neighborhood Longitude',
                             'Venue',
                             'Venue Latitude',
                             'Venue Longitude',
                             'Venue Category']

    return (nearby_venues)

br_venues = getNearbyVenues(names=neighCenterData['Neighborhood'],
                            radius=neighCenterData['Radius'],
                            latitudes=neighCenterData['Center Latitude'],
                            longitudes=neighCenterData['Center Longitude'])
br_venues.to_excel('br_food.xlsx')
