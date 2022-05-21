from math import pi

R_OFFSET = 150
W_OFFSET = pi
S_OFFSET = pi/2
E_OFFSET = 0

def getRobotAngle( angle ):
    return int( 1023 * ( angle + R_OFFSET ) / 300 )

def getDGMAngle( q ):
    return [ q[0] + W_OFFSET, q[1] + S_OFFSET, q[2] + E_OFFSET ]

def getIGMAngle( q ):
    return [ _boundRadians( q[0], - W_OFFSET ),
             _boundRadians( q[1], - S_OFFSET ),
             _boundRadians( q[2], - E_OFFSET ) ]

def _boundRadians( q, offset ):
    if q != None:
        q = q + offset
        if q > pi:
            q = q - 2 * pi
        if q < -pi:
            q = 2 * pi + q 
        return q
    return None