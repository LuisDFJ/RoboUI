from RGLEngine.RLoader import RLoader
import numpy
from RGLEngine.RDGM import RDGM
import glm

#array = RLoader( path=r".\RMedia\link2_completo.obj", scale=100 ).array
#print( numpy.max( array[:,2] ) / 2 )

dgm = RDGM( 
            [ False, False, False ],
            [ 0, 2, 3 ],
            [ glm.radians( -90 ), glm.radians( -90 ), glm.radians( 0 ) ],
            [ 0, 4, 5 ],
            [ 0, 0, 0 ]
        )

for i in range( 4 ):
    angle = glm.radians( 15 * (i+1) )
    T0n = dgm.GenDGM( [ angle, 0, 0 ] )
    print( angle )
    print( T0n[1] )