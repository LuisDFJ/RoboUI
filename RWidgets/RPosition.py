from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

class RPosition( QtWidgets.QWidget ):
    def __init__( self, parent=None ):
        super(RPosition,self).__init__( parent=parent )
        layout = QtWidgets.QHBoxLayout( self )
        
        self.matrix = QtWidgets.QLabel()
        self.matrix.setWordWrap( True )

        layout.addWidget( QtWidgets.QLabel( "End Effector" ) )
        layout.addWidget( self.matrix )
        self.setPosition( np.eye( 4 ) )
        self.setLayout( layout )

    def setPosition( self, matrix ):
        smatrix = ""
        for row in matrix:
            for val in row:
                smatrix = smatrix + "{:<12}".format( "{:.2f}".format( val ) )
            smatrix = smatrix + "\n"
        self.matrix.setText( smatrix[:-1] )
