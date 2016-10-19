# @Author       Andreas Slovace
# @CreatedDate  17.10.2016


import googlemaps
import math




#######################################################################################################
#                                     Arc Length Compute
#######################################################################################################
# Helper class to compute distance between two points on a sphere
# Use  Vincenty formula which is accurate for all points on the globe. Will use Haversine as test
#                           https://www.wikiwand.com/en/Haversine_formula
#                           https://www.wikiwand.com/en/Great-circle_distance
# Variables:
#   Phi     - Latitude
#   Lamda   - Longitude
# Necessary Libraries: math
class geometry:

    # Radius of the earth
    EarthRadius = 6371

    # Via Speherical Law of Cosines for the central angle
    # Input: (latitude, longitude pairs) as Phi and Lam respectively
    # Output: the central angle of the two points
    def centralAngle( phi1, phi2, lam1, lam2):
        sines = math.sin(phi1) * math.sin(phi2)
        cosines = math.cos(phi1) * math.cos(phi2) * math.cos( absoluteDistance(lam1, lam2) )
        return math.acos( sines + cosines )



    # Haversine Formula for the central angle
    # Better for small distances
    # Input: (latitude, longitude pairs) as Phi and Lam respectively
    # Output: the central angle of the two points
    def HaversineCentralAngle( phi1, phi2, lam1, lam2 ):
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
    def VicentyCentralAngle( phi1, phi2, lam1, lam2 ):
        dPhi = math.radians( phi1 - phi2)
        dLam = math.radians( lam1 - lam2)
        phi1 = math.radians( phi1)
        phi2 = math.radians( phi2)
        radicand = ( math.cos(phi2)*math.sin(dLam))**2 + (math.cos(phi1)*math.sin(phi2)-math.sin(phi1)*math.cos(phi2)*math.cos(dLam))**2
        denominator = math.sin(phi1)*math.sin(phi2)+math.cos(phi1)*math.cos(phi2)*math.cos(dLam)
        return math.atan( math.sqrt( radicand ) / denominator )



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
#   4 [] ) Get the distance result for all cities


# Necessary Libraries: googlemaps
class GoogleMapsAPI:
    
    # [ My Geocoding Key, My Distance Matrix Key ; Hired's key]
    API_KEY = ['AIzaSyCniEGWspt4uiot9vJINzb0mwDqEWZzTsI','AIzaSyCGIKWtEZRhBMB7kTLuxCnCV1MeujAOtS0','AIzaSyDG0q5LNcKR189qBWXyjW9CeaYXNOA2Vtg']
    
    # Google Maps API login
    gmaps = googlemaps.Client(key=API_KEY[0])

    # Response sent by Google for parsing
    response = ''

    # Latitude and Longitude of the city - from Geocode API
    lat = 0.0
    lng = 0.0
    
    
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


    # Test that the repsonse is coming in as expected - REQUIRES MY KEY
    def test2(self):
        print( self.gmaps.distance_matrix( self.Cities[2] , self.Cities[5],mode=None)  )


    # Get geocode of a given city - REQUIRES HIRED KEY
    def getCityCeo(self):
        self.response = self.gmaps.geocode( self.Cities[0] )
        self.lat = self.response[ len(self.response)-2]['geometry']['location']['lat']
        self.lng = self.response[ len(self.response)-2]['geometry']['location']['lng']
        print( "Longitude:\t" + str(self.lng) + "\nLatitude:\t" + str(self.lat) )
        invLat = -1*self.lat
        invLng = -1*self.lng
        #print( self.response[ self.response.index()]['geometry']['location']['lng'] )


    # Get value from JSON
    def getDistance(self):
        print( self.response['rows'][0]['elements'][0]['distance']['text'] )


    # Store one copy the response
    def getResponse(self):
        self.response =  self.gmaps.distance_matrix( self.Cities[2] , self.Cities[5],mode=None)


    # Run functions using MY DISTANCE MATRIX KEY
    def runWithASKey(self):
        gmaps = googlemaps.Client(key=self.API_KEY[1])
        self.test2()
        self.getResponse()
        print( self.response )
        # self.getDistance() #Gets the text distance- which is incorrect

    # Run functions using MY GEOCODING KEY 
    def runWithHiredKey( self ):
        gmaps = googlemaps.Client(key=self.API_KEY[0])
        self.getCityCeo()
    

    # Run the program
    def __init__(self):
        self.runWithASKey()
        print("\n\nOnto getting JSON:\n\n")
        self.runWithHiredKey()
        
        


#######################################################################################################
#                                     END GoogleMapsAPI
#######################################################################################################






list = []
a = 4
for i in range( 0 , a): 
    for j in range (i+1 , a): 
        list.append([i,j])

for i in range( len(list)):
    print( list[i] )


# x = GoogleMapsAPI()
print("Successful Run")
