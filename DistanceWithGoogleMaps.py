# @Author       Andreas Slovace
# @CreatedDate  17.10.2016
#
# Built with:   Python 3.5.2 on Windows 10 64 bit
#
# Requires:
#               Math library, Python native
#               google-maps-services-python, https://github.com/googlemaps/google-maps-services-python
#
# Purpose:      Given a list of cities find the two that are closest.
#
# Method:       Google-maps-services Geocoding API can take cities by name and return their latitude and longitude.
#               The Vicenty formula was created to find the arc length between points on an ellipsoid at any
#               distance ( https://www.wikiwand.com/en/Great-circle_distance ).  Plug the latitude, longitude pairs
#               into the vicenty formula and return the pair with the minimum distance.
#
# My Approach:  First I tried using the API Key provided by hired, but Google didn't accept it for either the
#               Distance Matrix API or Geocoding API. Since getting a key took seconds, and the Geocoding API
#               seemed best suited for latitude and longitude I got my own key, and recalled geometry class.


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



    # Haversine Formula for the central angle
    # Better for small distances
    # Input: (latitude, longitude pairs) as Phi and Lam respectively
    # Output: the central angle of the two points
    def HaversineCentralAngle2( phi1, phi2, lam1, lam2 ):
        dPhi = math.radians( phi1 - phi2)
        dLam = math.radians( lam1 - lam2)
        phi1 = math.radians( phi1)
        phi2 = math.radians( phi2)
        radicand = math.sin(dPhi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dLam/2)**2
        return 2 * math.asin( math.sqrt( radicand ) )

    # Vicenty Formula for the central angle
    # This special case works for all distances
    # Input: (latitude, longitude pairs) as Phi and Lam respectively
    # Output: the central angle of the two points
    def VicentyCentralAngle( c0, c1 ):
        # c = [phi1, lam1]
        phi1 = c0[0]
        lam1 = c0[1]
        phi2 = c1[0]
        lam2 = c1[1]
        dPhi = math.radians( phi1 - phi2)
        dLam = math.radians( lam1 - lam2)
        phi1 = math.radians( phi1)
        phi2 = math.radians( phi2)
        radicand = ( math.cos(phi2)*math.sin(dLam))**2 + (math.cos(phi1)*math.sin(phi2)-math.sin(phi1)*math.cos(phi2)*math.cos(dLam))**2
        denominator = math.sin(phi1)*math.sin(phi2)+math.cos(phi1)*math.cos(phi2)*math.cos(dLam)
        return math.atan( math.sqrt( radicand ) / denominator )


    # Vicenty Formula for the central angle
    # This special case works for all distances
    # Input: (latitude, longitude pairs) as Phi and Lam respectively
    # Output: the central angle of the two points
    def VicentyCentralAngle2( phi1, phi2, lam1, lam2 ):
        dPhi = math.radians( phi1 - phi2 )
        dLam = math.radians( lam1 - lam2 )
        phi1 = math.radians( phi1)
        phi2 = math.radians( phi2)
        radicand = ( math.cos(phi2)*math.sin(dLam))**2 + (math.cos(phi1)*math.sin(phi2)-math.sin(phi1)*math.cos(phi2)*math.cos(dLam))**2
        denominator = math.sin(phi1)*math.sin(phi2)+math.cos(phi1)*math.cos(phi2)*math.cos(dLam)
        return math.atan( math.sqrt( radicand ) / denominator )


    # From my geometry book
    def centralAngleGeometryClass( phi1, phi2, lam1, lam2 ):
        return math.acos( math.sin(phi1)*math.sin(phi2) + math.cos(phi1)*math.cos(phi2)*math.cos(lam1-lam2)) 


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
# Purpose: Given a list of cities find the two closest each other
# Method: Must be "as the crow flies" hence a straight line distance.
#   To be found in the Distance API...

#   1 [X] ) Log in
#   2 [X] ) Test that a pair of cities can be fetched [see test2]
#   3 [X] ) Get their distance from JSON [see getDistance() ]
#   4 [X] ) Get the distance result for all cities
#   5 [] ) Print the formatted answer
#   6 [] ) FINAL: print on the minimum


# Necessary Libraries: googlemaps
class GoogleMapsAPI:
    
    # [ My Geocoding Key, My Distance Matrix Key ; Hired's key]
    API_KEY = ['AIzaSyCniEGWspt4uiot9vJINzb0mwDqEWZzTsI','AIzaSyCGIKWtEZRhBMB7kTLuxCnCV1MeujAOtS0','AIzaSyDG0q5LNcKR189qBWXyjW9CeaYXNOA2Vtg']
    
    # Google Maps API login
    gmaps = googlemaps.Client(key=API_KEY[0])

    # Response sent by Google for parsing
    response = ''

    # Latitude and Longitude of the city - from Geocode API
    currentMin = [['',''],99999999]
    lat = 0
    lng = 0
    

    # Cities and coordinates
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


    # Test that the repsonse is coming in as expected - REQUIRES MY DISTNANCE MATRIX KEY
    def test2(self):
        print( self.gmaps.distance_matrix( self.Cities[2] , self.Cities[5],mode=None)  )


    # Fill the CityCoord variable with City as key and its coordinates as values
    def fillCityCoord(self):
        print("Filling City Coordinates")
        for i in range( len( self.Cities) ):
            self.CityCoord[ self.Cities[i] ] = self.getCityGeo( self.Cities[i] ) 


    # Get geocode of a given city - REQUIRES MY GEOCODING KEY
    def getCityGeo(self):
        self.response = self.gmaps.geocode( self.Cities[0] )
        lat = self.response[ len(self.response)-2]['geometry']['location']['lat']
        lng = self.response[ len(self.response)-2]['geometry']['location']['lng']
        return [lat,lng]

    # Get geocode of a given city - REQUIRES MY GEOCODING KEY
    def getCityGeo(self, cityName):
        self.response = self.gmaps.geocode( cityName )
        lat = self.response[ len(self.response)-2]['geometry']['location']['lat']
        lng = self.response[ len(self.response)-2]['geometry']['location']['lng']
        return [lat,lng]


    # Get value from JSON
    def getDistance(self):
        print( self.response['rows'][0]['elements'][0]['distance']['text'] )


    # Store one copy the response using MY DISTANCE MATRIX KEY
    def getResponse(self):
        self.response =  self.gmaps.distance_matrix( self.Cities[2] , self.Cities[5],mode=None)
    

    # Given a pair of citiesand their distance print it prettily
    # A 'pair' is [['City 1','City 2'],distance_in_km]
    def printPrettyPair( self, pair):
        print(pair[0][0] + " and " + pair[0][1] + " are " + str( pair[1] ) + "KM apart.\n")
    

    # Process pairs of cities and update the max
    def processCities(self):
        print( "Processing Cities..")
        for index0 in range( len( self.Cities ) ):
            c0 = self.getCityGeo( self.Cities[index0] ) 
            for index1 in range( index0+1, len( self.Cities ) ):
                c1 = self.getCityGeo( self.Cities[index1] )
                # c0 = self.CityCoord[ self.Cities[index0] ]
                # c1= self.CityCoord[ self.Cities[index1] ]
                distance = math.fabs(geometry.ArcLength( geometry.EarthRadius, geometry.HaversineCentralAngle(c0, c1)))
                currentPair = [[self.Cities[index0],self.Cities[index1]],distance]
                self.setMinPair(currentPair)
                #self.printPrettyPair( self.Cities[index0], self.Cities[index1], distance)
                # print( self.Cities[index0] + "\tLat: " + str(c0[0]) + "\tLong: " + str(c0[1]) )
                # print( self.Cities[index1] + "\tLat: " + str(c1[0]) + "\tLong: " + str(c1[1]) )
    

    # Run functions using MY DISTANCE MATRIX KEY
    def runWithASDistanceMatrix(self):
        gmaps = googlemaps.Client(key=self.API_KEY[1])
        self.test2()
        self.getResponse()
        print( self.response )
        # self.getDistance() #Gets the text distance- which is incorrect
    

    # Run functions using MY GEOCODING KEY 
    def runWithASGeoCodeKey( self ):
        gmaps = googlemaps.Client(key=self.API_KEY[0])
        # c = self.getCityGeo( self.Cities[5] )
        # print("Latitude: " + str( c[0] ) + "\tLongitude: " + str( c[1] ) )
        # self.fillCityCoord()
        self.processCities()
    

    # Set minimum in self based on input
    def setMinPair(self, newIn):
        if( self.currentMin[1] > newIn[1]):
            # print("\n\n\nChanged Min from: " + self.currentMin[0][0] + "," + self.currentMin[0][1] + "\td = " + str(self.currentMin[1]) + "\n" + newIn[0][0] + "," + newIn[0][1] + "\td = " + str(newIn[1]) )
            self.currentMin = newIn
            
    

    # Run the program
    def __init__(self):
        self.runWithASGeoCodeKey()
        self.printPrettyPair(self.currentMin)
        
        


#######################################################################################################
#                                     END GoogleMapsAPI
#######################################################################################################



x = GoogleMapsAPI()
