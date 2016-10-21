# @Author       Andreas Slovace
# @CreatedDate  17.10.2016
#
# Built with:   Python 3.5.2 on Windows 10 64 bit
#
# Repository:   https://github.com/Andreas237/GoogleMapsPython
#
# Requires:
#               Math library, Python native
#               google-maps-services-python, https://github.com/googlemaps/google-maps-services-python
#
# Purpose:      Given a list of cities find the two that are closest.
#
# Method:       Google-maps-services Geocoding API can take cities by name and return their latitude and longitude.
#               The Haversine formula was created to find the arc length between points on an ellipsoid
#               ( https://www.wikiwand.com/en/Great-circle_distance ).  Plug the latitude, longitude pairs
#               into the formula and return the pair with the minimum distance.
#               Note:   I tried their version of the Vicenty formula, and derived another, but crossing 0 Longitude
#                       had the distance coming out incorrectly.
#
# My Approach:  First I tried using the API Key provided by hired, but Google didn't accept it for either the
#               Distance Matrix API or Geocoding API. Since getting a key took seconds, and the Geocoding API
#               seemed best suited for latitude and longitude I got my own key, and recalled geometry class.
#               To run be sure you have the googlemaps Python library. From there you can simply run this.


import googlemaps
import math




#######################################################################################################
#                                     Arc Length Compute
#######################################################################################################
# Helper class to compute distance between two points on a sphere
# Use  Haversine formula.  See references
#                           https://www.wikiwand.com/en/Haversine_formula
#                           https://www.wikiwand.com/en/Great-circle_distance
# Variables:
#   Phi     - Latitude
#   Lamda   - Longitude
# Necessary Libraries: math
class geometry:

    # Radius of the earth
    EarthRadius = 6371


    # Haversine Formula for the central angle
    # Better for small distances
    # Input: (latitude, longitude pairs) as Phi and Lam respectively
    # Output: the central angle of the two points
    def HaversineCentralAngle( c0, c1 ):
        # c = [phi1, lam1]
        phi1 = c0[0]
        lam1 = c0[1]
        phi2 = c1[0]
        lam2 = c1[1]
        dPhi = math.radians( phi1 - phi2)
        dLam = math.radians( lam1 - lam2)
        phi1 = math.radians( phi1)
        phi2 = math.radians( phi2)
        radicand = math.sin(dPhi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dLam/2)**2
        return 2 * math.asin( math.sqrt( radicand ) )


    # Arc Length from the Law of Cosines
    def ArcLength(r, angle):
        return r * angle

        


#######################################################################################################
#                                    End Arc Length Compute
#######################################################################################################










#######################################################################################################
#                                     Begin GoogleMapsAPI
#######################################################################################################



# Google Maps API
# Purpose:  Given a list of cities find the two closest each other
# Method:   Must be "as the crow flies" hence a straight line distance.
#           Use the Google Geocode API to get the coordinates of every city on the list
#           Use the Haversine formula to fill a dictionary with city pairs as keys and
#           distance as values.
#           Compare the distances of all the pairs



# Necessary Libraries: googlemaps, math
class GoogleMapsAPI:
    
    # My Geocoding Key
    API_KEY = 'AIzaSyCniEGWspt4uiot9vJINzb0mwDqEWZzTsI'
    
    # Google Maps API login
    gmaps = googlemaps.Client(key=API_KEY)

    # Latitude and Longitude of the city - from Geocode API
    currentMin = [['',''],99999999]

    

    # Dictionary of cities and coordinates
    CityCoord = {}
    
    # Cities given in the prompt
    Cities = ["San Francisco, CA, United States",
              "Boston, MA, United States",
              "New York, NY, United States",
              "Washington, DC, United States",
              "Seattle, WA, United States",
              "Austin, TX, United States",
              "Chicago, IL, United States",
              "San Diego, CA, United States",
              "Denver, CO, United States",
              "London, England",
              "Toronto, On, Canada",
              "Sydney, NSW, Australia",
              "Melbourne, VIC, Australia",
              "Paris, France",
              "Singapore, Singapore"
              ]



    # Function: __init__
    # Purpose:  Constructor to run using MY GEOCODING KEY
    # Method: Authenticate, get each city's coordinates, find the minimum distance
    def __init__(self):
        gmaps = googlemaps.Client(key=self.API_KEY)
        self.processCities()
        self.printPrettyPair(self.currentMin)


    # Function: getCityGeo
    # Purpose:  Get geocode of a given city
    # Method:   Use JSON returned by Google Maps to access the latitude and longitude
    # Input:
    #           cityName - string of City Name to pass to the API
    def getCityGeo(self, cityName):
        response = self.gmaps.geocode( cityName )
        lat = response[ len(response)-2]['geometry']['location']['lat']
        lng = response[ len(response)-2]['geometry']['location']['lng']
        return [lat,lng]
    

    # Function: printPrettyPair
    # Purpose:  Given a pair of citiesand their distance print it prettily
    # Method:   Print
    # Input:
    #           pair - A 'pair' is [['City 1','City 2'],distance_in_km]
    def printPrettyPair( self, pair):
        print(pair[0][0] + " and " + pair[0][1] + " are " + str( round(pair[1],2) ) + "KM apart.\n")
    

    # Function: processCities
    # Purpose:  Find the minimum distance between all cities in the list
    # Method:   1) Loop through the list of getting their coordinates from the dictionary
    #           2) Get the distance between the two
    #           3) Set the minimum city relative to this pair
    # Input:
    def processCities(self):
        print( "Processing Cities..")
        for index0 in range( len( self.Cities ) ):
            c0 = self.getCityGeo( self.Cities[index0] ) 
            for index1 in range( index0+1, len( self.Cities ) ):
                c1 = self.getCityGeo( self.Cities[index1] )
                distance = math.fabs(geometry.ArcLength( geometry.EarthRadius, geometry.HaversineCentralAngle(c0, c1)))
                currentPair = [[self.Cities[index0],self.Cities[index1]],distance]
                self.setMinPair(currentPair)

    
    

    # Function: setMinPair
    # Purpose:  Set minimum in self based on input
    # Method:   Compare input to current minimum
    # Inputs:
    #           pair - A 'pair' is [['City 1','City 2'],distance_in_km]
    def setMinPair(self, pair):
        if( self.currentMin[1] > pair[1]):
            self.currentMin = pair
            
    



#######################################################################################################
#                                     END GoogleMapsAPI
#######################################################################################################



x = GoogleMapsAPI()
