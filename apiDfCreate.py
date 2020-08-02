import numpy as np
import pandas as pd
from pandas import json_normalize

import requests
import json

avgNeighCoords_df = pd.read_excel('Average_Neighborhood_Coord.xlsx')

lat = np.average(avgNeighCoords_df['Lat'])
long = np.average(avgNeighCoords_df['Long'])
urlExplore = 'https://api.foursquare.com/v2/venues/explore'
oneMileInMeters = 1609
exploreParams = dict(
    client_id='Hidden',
    client_secret="Hidden",
    ll=f'{lat},{long}',
    v='20200725',
    query='restaurant',
    limit=100,
    radius=2 * oneMileInMeters
)

def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']

    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']


for iternum, [lat, long, neighborhood, community] in enumerate(zip(avgNeighCoords_df['Lat'],
                                                                   avgNeighCoords_df['Long'],
                                                                   avgNeighCoords_df['Neighborhood'],
                                                                   avgNeighCoords_df['Community'])):
    exploreParams['ll'] = f'{lat},{long}'
    response = requests.get(url=urlExplore, params=exploreParams)
    data = json.loads(response.text)
    if len(data['response']['groups'][0]['items']) == 0:
        print(f'No Restaurant for {neighborhood}, {community} are available at the moment!')
    else:
        venues = data['response']['groups'][0]['items']
        foursquareDf = json_normalize(venues)
        for col in foursquareDf.columns:
            if col.find('venue') != -1:
                foursquareDf.rename(columns={col: col[len('venue.'):]}, inplace=True)
        filtered_columns = ['name', 'categories'] + [col for col in foursquareDf.columns if
                                                     col.startswith('location.')] + ['id']
        if iternum == 0:
            foursquareDf_filtered = foursquareDf.loc[:, filtered_columns]
            foursquareDf_filtered['categories'] = foursquareDf_filtered.apply(get_category_type, axis=1)
            foursquareDf_filtered.columns = [column.split('.')[-1] for column in foursquareDf_filtered.columns]
        else:
            foursquareDf_filtered1 = foursquareDf.loc[:, filtered_columns]
            foursquareDf_filtered1['categories'] = foursquareDf_filtered1.apply(get_category_type, axis=1)
            foursquareDf_filtered1.columns = [column.split('.')[-1] for column in foursquareDf_filtered1.columns]
            foursquareDf_filtered = pd.concat([foursquareDf_filtered, foursquareDf_filtered1], axis=0,
                                              ignore_index=True)

foursquareDf_filtered = foursquareDf_filtered.drop_duplicates(subset=['address'], keep='first')
foursquareDf_filtered.to_csv('fsfilter.csv')