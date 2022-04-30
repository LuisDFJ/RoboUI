import glm
import numpy as np

class RView():
    def __init__( self, engine, ViewPosition, ViewPoint, ViewUp, ratio, fov=45.0 ):
        self.engine         = engine
        self.ViewPosition   = glm.fvec3( ViewPosition[0], ViewPosition[1], ViewPosition[2] )
        self.ViewPoint      = glm.fvec3( ViewPoint[0], ViewPoint[1], ViewPoint[2] )
        self.ViewUp         = glm.fvec3( ViewUp[1], ViewUp[0], ViewUp[2] )
        
        self.view           = np.array( glm.lookAt( self.ViewPosition, self.ViewPoint, self.ViewUp ) )
        self.perspective    = np.array( glm.perspective( glm.radians( fov ), ratio, 0.1, 10.0 ) )

    def setView( self ):
        self.engine.setUniformMatrix4fv( "view", self.view )
        self.engine.setUniformMatrix4fv( "perspective", self.perspective )
