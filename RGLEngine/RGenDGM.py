import numpy as np
from math import pi
from RGLEngine.RTransformations import rotateX, rotateY, rotateZ, translate

class RGenDGM():
    def __init__(self, L1=93.4, L2=93.5, L3=155.6):
        self.a     = [      0.0,     L2,     L3   ]
        self.alpha = [   pi/2,      0.0,      0.0   ]
        self.d     = [     L1,      0.0,      0.0   ]
        
    def GetDGM( self, q ):
        n = len(q)
        T = np.zeros([4,4,n+1])
        U = np.zeros([4,4,n+1])
        T0n = np.eye(4)

        T[:,:,0] = np.eye(4)
        U[:,:,0] = np.eye(4)

        for i in range(0,n):
            T[:,:,i+1] = rotateZ( q[i] )@translate( z=self.d[i] )@rotateX( self.alpha[i] )@translate( x=self.a[i] )
            T0n = T0n @ T[:,:,i+1]
            U[:,:,i+1] = T0n

        return U[:,:,3]