import numpy as np
from math import sqrt
from RUtils.RTypes import RFrame, RJoint, RPoint
from math import atan2,sin,cos,pi




#P1 = RPoint( 1,1,2 )
#P2 = RPoint( 2,2,3 )
#P3 = RPoint( 1,3,4 )
#print( calcCircle( P1, P2, P3 ) )

#from RUtils.RInterpolation import RLinearInterpolator

#lin = RLinearInterpolator( RPoint(), RPoint( 5,5,5 ), 1 )

#print( len( lin.lineal_interpol() ) )
#for p in lin.lineal_interpol():
#    print( p )


class RCircularInterpolator():
    def __init__( self, prev : RPoint, mid : RPoint, pos : RPoint, res : float = pi/8 ):
        self.res = res
        self.P1 = prev
        self.P2 = mid
        self.P3 = pos
        self.center, self.r, self.F, self.U3 = self.calcCircle( prev, mid, pos )

    
    def getFrame( self, P1 : RPoint, P2 : RPoint, P3 : RPoint ):
        P12 = P2 - P1
        P13 = P3 - P1

        Nz = P12 % P13
        Nz = Nz / ~Nz
        
        Ny = P13
        Ny = Ny / ~Ny
        
        Nx = Ny % Nz
        Nx = Nx / ~Nx
        return RFrame( Nx, Ny, Nz )

    def calcCircle( self, P1 : RPoint, P2 : RPoint, P3 : RPoint ):
        F = self.getFrame( P1, P2, P3 )
        U2 = ~F % ( P2 - P1 )
        U3 = ~F % ( P3 - P1 )
        m11 = 2*U2.x; m12 = 2*U2.y; r1 = U2.x**2 + U2.y**2
        m21 = 2*U3.x; m22 = 2*U3.y; r2 = U3.x**2 + U3.y**2

        y = ( r2 - m21 * r1 / m11 ) / ( m22 - m21 * m12 / m11 )
        x = ( r1 - m12 * y ) / m11
        r = sqrt( x**2 + y**2 )
        return RPoint( x, y ), r, F, U3


    def planar_circular_interpol( self, prev : RPoint, pos : RPoint, r : float ):
        ang_i = atan2(prev.y, prev.x)
        ang_f = atan2(pos.y, pos.x)
        d = abs( ang_f - ang_i )
        for i in range( int( d // self.res ) ):
            angle = ang_i + self.res * i
            yield RPoint( r*cos(angle), r*sin(angle) )
        yield pos
        
    def circular_interpol( self ):
        prev = -self.center
        pos = self.U3 - self.center
        for point in self.planar_circular_interpol( prev, pos, self.r ):
            yield self.F % ( point + self.center ) + self.P1
            


cint = RCircularInterpolator( RPoint(1,1,0), RPoint(-2,2,0), RPoint(1,3,0) )
for i in cint.circular_interpol():
    print( i )

