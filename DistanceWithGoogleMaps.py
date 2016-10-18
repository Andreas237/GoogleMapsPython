# Author
# Date
# Purpose
# Method

# Thoughts:
# - pop up a window to show the two closes cities and their distance
# - create a list of the cities
# -- create pairs array

import googlemaps
import json
import urllib.request
from datetime import datetime

API_KEY = 'AIzaSyCGIKWtEZRhBMB7kTLuxCnCV1MeujAOtS0'

print("My API KEY = " + API_KEY)



gmaps = googlemaps.Client(key=API_KEY)

print( gmaps.distance_matrix("San Francisco, CA", "San Jose, CA",mode=None) )





theURL = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=Vancouver+BC|Seattle&destinations=San+Francisco|Victoria+BC&mode=bicycling&language=fr-FR'

response = urllib.request.urlopen(theURL)


with urllib.request.urlopen('http://www.python.org/') as f:
    print( f.read(300).decode('utf-8') )







print("Successful Run")
