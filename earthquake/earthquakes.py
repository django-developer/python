#! /usr/bin/python

'''
JSON format:
http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

geopy:
https://pypi.python.org/pypi/geopy/1.9.1
sudo pip install geopy # install geopy

address: 'San Francisco, CA 94128, USA'
Latitude: 37.7792808
Longitude: -122.4192363
'''

import json, urllib, urllib2, sys, os, tempfile
from pprint import pprint
from time import time
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

class EarthQuakes(object):
    '''class definition for earth quakes

    args:
        address:  'San Francisco, CA 94128, USA'
        days:     optional, default = 7,
                  consider the earth quakes during the recent 'days'
        distance: optional, default = 100,
                  consider the earth quakes within this 'distance' in miles from 'address'
    '''

    URL = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'

    def __init__(self,
                 address,
                 days = 60,
                 distance = 100):

        '''constructor for EarthQuakes

        '''

        geolocator = Nominatim()
        location = geolocator.geocode(address, timeout = 60)
        self.address = (location.latitude, location.longitude)
        del geolocator, location

        self.days = days*24*60*60*1000        # milliseconds
        self.distance = distance              # miles

        self.json_data = self._get_json_data()     # json data of the earthquakes

    def _get_json_data(self):

        '''read json_data from the URL.

        return json_data
        '''

        try:
            json_data = urllib2.urlopen(EarthQuakes.URL)

        except urllib2.URLError as e:
            if hasattr(e, 'reason'):
                exit_msg = 'We failed to reach a server.\n'
                exit_msg += 'Reason: {0}\n'.format(e.reason)
            elif hasattr(e, 'code'):
                exit_msg = 'The server could not fulfill the request.\n'
                exit_msg += 'Error code: {0}\n'.format(e.code)
            else:
                exit_msg = 'URLError'
                sys.exit(exit_msg)
    
        fp = tempfile.NamedTemporaryFile(delete=False)
        tmp_file = fp.name
        fp.close()

        with open(tmp_file, 'w') as f:
            f.write(json_data.read())

        with open(tmp_file, 'r') as f:
            json_data = json.load(f)

        os.remove(tmp_file)
        return(json_data)
    
    def _filter_fn(self, x):

        '''filter earth quake feature records

        filter earth quake feature records based on
            1. distance (miles, within self.distance from self.address)
            2. time     (milliseconds, within self.days from now)

        return True if (above conditions) else False
        '''
  
        def is_within_days(x):
            return( ((time() * 1000) - self.days) <= x['properties']['time'] <= (time() * 1000) )

        def is_within_distance(x):
            earth_quake_location = (x['geometry']['coordinates'][1],
                                    x['geometry']['coordinates'][0])
            return(vincenty(self.address, earth_quake_location).miles <= self.distance)
  
        return( is_within_days(x) and is_within_distance(x) )

    def max_magnitude(self):

        '''earthquake feature with the max magnitude

        print the max magnitude, satisfying the conditions (days, distance)
        '''

        try:
            t = [x for x in self.json_data['features'] if self._filter_fn(x)]
            max_mag_record = max(t, key = lambda x : x['properties']['mag'])
            max_mag = max_mag_record['properties']['mag']
            print('\nMax magnitude = {0}\n'.format(max_mag))
            pprint(max_mag_record)

        except ValueError:
            print('\nNo Earth Quakes\n')


if __name__ == '__main__':

    address = 'San Francisco, CA 94128, USA'
    x = EarthQuakes(address)
    x.max_magnitude()

