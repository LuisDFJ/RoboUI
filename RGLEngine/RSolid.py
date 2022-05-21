from RGLEngine.RTransformations import rotateX, rotateY, rotateZ, translate
from RGLEngine.RLoader import RLoader
from OpenGL import GL
import numpy as np

class RSolid():
    def __init__(self, path, engine, scale=1, offset=None, rotX=0, rotY=0, rotZ=0, color=np.array( [0.9,0.9,0.9] ) ):
        array       = RLoader( path=path, scale=scale ).array
        self.engine = engine
        self.size   = array.size
        self.vao    = engine.createVAO( array, None )
        self.color  = color
        
        if isinstance( offset, np.ndarray ):
            offset = translate( offset[0], offset[1], offset[2] )
        else:
            offset = np.eye( 4 )
        rotation = rotateX( rotX ) @ rotateY( rotY ) @ rotateZ( rotZ )
        self.offset = rotation @ offset
    
    def draw(self, transform):
        t = transform @ self.offset 
        self.engine.setUniformMatrix4fv( "transform", t )
        self.engine.setUniform3fv( "uColor", self.color )
        self.engine.useVAO( self.vao )
        GL.glDrawArrays( GL.GL_TRIANGLES, 0, self.size )
