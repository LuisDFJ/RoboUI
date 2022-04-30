import math
import numpy as np

def translate( x=0.0, y=0.0, z=0.0 ):
    return np.array( [ [ 1.0, 0.0, 0.0, x ],
                       [ 0.0, 1.0, 0.0, y ],
                       [ 0.0, 0.0, 1.0, z ],
                       [ 0.0, 0.0, 0.0, 1.0 ] ] )

def rotateX( angle ):
    st = math.sin( angle )
    ct = math.cos( angle )
    return np.array( [
        [ 1.0, 0.0, 0.0, 0.0 ],
        [ 0.0,  ct, -st, 0.0 ],
        [ 0.0,  st,  ct, 0.0 ],
        [ 0.0, 0.0, 0.0, 1.0 ]
    ] )

def rotateY( angle ):
    st = math.sin( angle )
    ct = math.cos( angle )
    return np.array( [
        [ ct, 0.0,  st, 0.0 ],
        [ 0.0, 1.0, 0.0, 0.0 ],
        [ -st, 0.0,  ct, 0.0 ],
        [ 0.0, 0.0, 0.0, 1.0 ]
    ] )

def rotateZ( angle ):
    st = math.sin( angle )
    ct = math.cos( angle )
    return np.array( [
        [ ct, -st, 0.0, 0.0 ],
        [ st,  ct, 0.0, 0.0 ],
        [ 0.0, 0.0, 1.0, 0.0 ],
        [ 0.0, 0.0, 0.0, 1.0 ]
    ] )
