from PyQt5 import QtWidgets
from OpenGL import GL, GLU
import numpy as np
from RGLEngine.REngine import REngine
from RGLEngine.RSolid import RSolid
from RGLEngine.RDGM import RDGM
from RGLEngine.RView import RView
import math

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
        
        self.dgm = RDGM( -0.3, 0.3, 1.05)

        self.view   = RView( self.engine, np.array( [ -3.0, 4.0, -2.5 ] ), np.array( [ -1.5, 1.5, 0.0 ] ), np.array( [ 1.0, 0.0, 0.0 ] ), self.width() / self.height() )
        
        self.link_1 = RSolid( r".\RMedia\link1_completo.obj", self.engine, 100, np.array( [-0.241, -0.1436, 0.0] ),rotX = math.radians(-90), rotY = math.radians( -7 ), rotZ = math.radians(-90))
        self.link_2 = RSolid( r".\RMedia\link2_completo.obj", self.engine, 100, np.array( [-0.1457, -0.12, -0.2412]) ) 
        self.link_3 = RSolid( r".\RMedia\link3_completo.obj", self.engine, 100, np.array( [-0.1457, -0.12, -0.2412] ) )

        self.engine.createShaderProgram()
        self.engine.useShaderProgram()

        self.view.setView()
        
    def paintGL(self):
            self._open()

            T0n = self.dgm.GenDGM( (self.WaistValue, self.ShoulderValue, self.ElbowValue) )
            
            self.link_1.draw( T0n[0] )
            self.link_2.draw( T0n[1] )
            self.link_3.draw( T0n[2] )

            self._close()

    def _open(self):
        GL.glClear( GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    def _close(self):
        self.engine.useVAO()