from PyQt5 import QtWidgets
from OpenGL import GL, GLU
import numpy as np
from RGLEngine.REngine import REngine
from RGLEngine.RSolid import RSolid
import math





def rotate( axis, angle ):
    st = math.sin( angle )
    ct = math.cos( angle )
    if axis == 'x':
        matrix = np.array( [
            1.0, 0.0, 0.0, 0.0,
            0.0,  ct, -st, 0.0,
            0.0,  st,  ct, 0.0,
            0.0, 0.0, 0.0, 1.0
        ] )
    elif axis == 'y':
        matrix = np.array( [
             ct, 0.0,  st, 0.0,
            0.0, 1.0, 0.0, 0.0,
            -st, 0.0,  ct, 0.0,
            0.0, 0.0, 0.0, 1.0
        ] )
    else:
        matrix = np.array( [
             ct, -st, 0.0, 0.0,
             st,  ct, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
        ] )
    return matrix


class RGLWidget( QtWidgets.QOpenGLWidget ):
    def __init__(self, parent=None):
        super( QtWidgets.QOpenGLWidget, self ).__init__( parent=parent )
        self.setObjectName("RoboGL")
        self.WaistValue     = 0
        self.ShoulderValue  = 0
        self.ElbowValue     = 0

    def setWaistValue   ( self, val ):
        self.WaistValue     = float( val )
    
    def setShoulderValue( self, val ):
        self.ShoulderValue  = float( val )
    
    def setElbowValue   ( self, val ):
        self.ElbowValue     = float( val )

    def initializeGL(self):
        self.engine = REngine()
        
        self.motor = RSolid( r".\RMedia\servo.obj", self.engine, 100 )
        self.largo = RSolid( r".\RMedia\largo.obj", self.engine, 100 )

        self.engine.createShaderProgram()
        self.engine.useShaderProgram()
        
    def paintGL(self):
            self._open()
            
            transform = rotate( 'x', self.WaistValue )
            
            self.motor.draw( transform )

            transform = rotate( 'x', self.ShoulderValue )

            self.largo.draw( transform )

            self._close()

    def _open(self):
        GL.glClear( GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    def _close(self):
        self.engine.useVAO()