from math import pi

R_OFFSET = 150
W_OFFSET = pi
S_OFFSET = pi/2
E_OFFSET = 0

def getRobotAngle( angle ):
    return int( 1023 * ( angle + R_OFFSET ) / 300 )

def getDGMAngle( q ):
    return [ q[0] + W_OFFSET, q[1] + S_OFFSET, q[2] + E_OFFSET ]