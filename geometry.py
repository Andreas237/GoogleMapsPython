import math

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

print(geometry.ArcLength(1,90))

print( geometry.ArcLength( 6372.8 , geometry.HaversineCentralAngle(36.12, 33.94, -86.67, -118.40)) )
print( 6372.8 * geometry.HaversineCentralAngle(36.12, 33.94, -86.67, -118.40) )
print( geometry.ArcLength( 6372.8 , geometry.VicentyCentralAngle(36.12, 33.94, -86.67, -118.40)) )
print( 6372.8 * geometry.VicentyCentralAngle(36.12, 33.94, -86.67, -118.40) )
