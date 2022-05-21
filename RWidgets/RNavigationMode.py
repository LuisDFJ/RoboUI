from PyQt5 import QtCore, QtWidgets, QtGui

class RNavigationMode( QtWidgets.QWidget ):
    def __init__(self, parent):
        super( RNavigationMode, self ).__init__( parent=parent )
        layout = QtWidgets.QHBoxLayout( self )
        
        self.button = QtWidgets.QPushButton( "Toggle" )
        self.mode   = QtWidgets.QLabel( "IGM" )

        layout.addWidget( self.button )
        layout.addWidget( QtWidgets.QLabel( "Mode: " ) )
        layout.addWidget( self.mode )

        self.setLayout( layout )

    def setMode( self, mode : str = 'IGM' ):
        self.mode.setText( mode )