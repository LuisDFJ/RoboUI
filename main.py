import numpy as np
from math import sqrt
from RUtils.RTypes import RFrame, RJoint, RPoint



def getFrame( P1 : RPoint, P2 : RPoint, P3 : RPoint ):
    P12 = P2 - P1
    P13 = P3 - P1

    Nz = P12 % P13
    Nz = Nz / ~Nz
    
    Ny = P13
    Ny = Ny / ~Ny
    
    Nx = Ny % Nz
    Nx = Nx / ~Nx
    return RFrame( Nx, Ny, Nz )

def calcCircle( P1 : RPoint, P2 : RPoint, P3 : RPoint ):
    F = getFrame( P1, P2, P3 )
    U2 = ~F % ( P2 - P1 )
    U3 = ~F % ( P3 - P1 )
    m11 = 2*U2.x; m12 = 2*U2.y; r1 = U2.x**2 + U2.y**2
    m21 = 2*U3.x; m22 = 2*U3.y; r2 = U3.x**2 + U3.y**2

    y = ( r2 - m21 * r1 / m11 ) / ( m22 - m21 * m12 / m11 )
    x = ( r1 - m12 * y ) / m11
    r = sqrt( x**2 + y**2 )
    return x, y, r

#P1 = RPoint( 1,1,2 )
#P2 = RPoint( 2,2,3 )
#P3 = RPoint( 1,3,4 )
#print( calcCircle( P1, P2, P3 ) )

#from RUtils.RInterpolation import RLinearInterpolator

#lin = RLinearInterpolator( RPoint(), RPoint( 5,5,5 ), 1 )

#print( len( lin.lineal_interpol() ) )
#for p in lin.lineal_interpol():
#    print( p )

from RUtils.RTrajectories import RTrajectories

traj = RTrajectories( r".\RMedia\Trajectories\path_2.rui" )
trajectories = traj.runPath( 'once' )
print( len( list( trajectories ) ) )
