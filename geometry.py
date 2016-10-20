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

print(geometry.ArcLength(1,90))
c0 = [36.12,-86.67]
c1 = [ 33.94, -118.40 ]

# London - Melbourne
# print( 6372.8 * geometry.VicentyCentralAngle2(51.5073509,-37.8136276,-0.1277583,144.9630576) )

# London - Singapore
# print( 6372.8 * geometry.HaversineCentralAngle(51.5073509,1.3553794,-0.1277583,103.8677444) )

# Melbourne - Singapore
#print( 6372.8 * geometry.HaversineCentralAngle(-37.8136276,1.3553794,144.96305763,103.8677444) )
#print( 6372.8 * geometry.VicentyCentralAngle2(-37.8136276,1.3553794,144.9630576,103.8677444) )


# London - Paris
#print( 6372.8 * geometry.VicentyCentralAngle2(51.5073509,48.856614,-0.1277583,2.3522219) )
#print( 6372.8 * geometry.HaversineCentralAngle(51.5073509,48.856614,-0.1277583,2.3522219) )


# Melbourne - Paris
print( 6372.8 * geometry.VicentyCentralAngle2(-37.8136276,48.856614,144.96305763,2.3522219) )
print( 6372.8 * geometry.HaversineCentralAngle(-37.8136276,48.856614,144.96305763,2.3522219) )

# print( 6372.8 * geometry.VicentyCentralAngle(  c0, c1) )
