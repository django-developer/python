'''Find the earthquake with max magnitude 

   JSON format:
   http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

   geopy:
   https://pypi.python.org/pypi/geopy/1.9.1
   sudo pip install geopy # install geopy

   address: 'San Francisco, CA 94128, USA'
   Latitude: 37.7792808
   Longitude: -122.4192363


   Usage:
   -----
     import earthquake        #  assumes this package is in earthquake directory

     address = 'San Francisco, CA 94128, USA'

     x = earthquake.EarthQuakes(address)
     x.max_magnitude()

'''

from earthquakes import EarthQuakes

__all__ = ('earthquakes',)


