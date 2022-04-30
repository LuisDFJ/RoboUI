from RGLEngine.RTransformations import rotateX, rotateY, rotateZ, translate
import math

class RDGM():
    def __init__( self, L1=-0.3, L2=0.3, L3=1.05 ):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3

    def GenDGM( self, q ):
        m0 = rotateX( math.radians( -90.0 ) )
        m1 = translate( z=self.L1 ) @ rotateZ( q[0] ) @ rotateX( math.radians( 90 ) )
        m2 = translate( y=self.L2 ) @ rotateZ( q[1] )
        m3 = translate( y=self.L3 ) @ rotateZ( q[2] )
        T01 = m0 @ m1
        T02 = T01 @ m2
        T03 = T02 @ m3

        return ( T01, T02, T03 )