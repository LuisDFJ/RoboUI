from numpy import size
from RGLEngine.RLoader import RLoader
from OpenGL import GL

class RSolid():
    def __init__(self, path, engine, scale=1):
        array       = RLoader( path=path, scale=scale ).array
        self.engine = engine
        self.size   = array.size
        self.vao    = engine.createVAO( array, None )
    
    def draw(self, transform):
        self.engine.setUniformMatrix4fv( "transform", transform )
        self.engine.useVAO( self.vao )
        GL.glDrawArrays( GL.GL_TRIANGLES, 0, self.size )
