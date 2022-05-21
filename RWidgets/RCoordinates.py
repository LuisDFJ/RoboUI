from PyQt5 import QtCore, QtGui, QtWidgets

class RSpinBox( QtWidgets.QSpinBox ):
    def __init__( self, parent = None ):
        super( RSpinBox, self ).__init__(parent=parent)
        self.setKeyboardTracking( False )
        self.active = False

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.active:
            return super().mousePressEvent(ev)
    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.active:
            return super().mouseReleaseEvent(ev)
    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.active:
            return super().mouseDoubleClickEvent(a0)
    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.active:
            return super().mouseMoveEvent(ev)
    def keyPressEvent(self, ev: QtGui.QKeyEvent) -> None:
        if self.active:
            return super().keyPressEvent(ev)
    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        if self.active:
            return super().keyReleaseEvent(a0)

class RCoordinates( QtWidgets.QWidget ):
    def __init__(self, parent=None, step=1):
        self.step = step
        super(RCoordinates, self).__init__( parent=parent )
        layout          = QtWidgets.QHBoxLayout( self )
        sublayout_label = QtWidgets.QVBoxLayout()
        sublayout_spin  = QtWidgets.QVBoxLayout()
        layout.addLayout( sublayout_label )
        layout.addLayout( sublayout_spin )

        self.XCoord = RSpinBox()
        self.XCoord.setRange( -350, 350 )
        self.XCoord.setSingleStep( 1 )
        self.XCoord.setValue( 0 )

        self.YCoord = RSpinBox()
        self.YCoord.setRange( -350, 350 )
        self.YCoord.setSingleStep( 1 )
        self.YCoord.setValue( 0 )

        self.ZCoord = RSpinBox()
        self.ZCoord.setRange( -350, 350 )
        self.ZCoord.setSingleStep( 1 )
        self.ZCoord.setValue( 0 )

        sublayout_label.addWidget( QtWidgets.QLabel( "X Coord (mm)" ) )
        sublayout_label.addWidget( QtWidgets.QLabel( "Y Coord (mm)" ) )
        sublayout_label.addWidget( QtWidgets.QLabel( "Z Coord (mm)" ) )

        sublayout_spin.addWidget( self.XCoord )
        sublayout_spin.addWidget( self.YCoord )
        sublayout_spin.addWidget( self.ZCoord )

        self.setLayout( layout )

    def getCoords( self ):
        return ( self.XCoord.value(), self.YCoord.value(), self.ZCoord.value() )

    def setPosition( self, matrix ):
        self.XCoord.blockSignals( True )
        self.XCoord.setValue( matrix[0][3] )
        self.XCoord.blockSignals( False )
        
        self.YCoord.blockSignals( True )
        self.YCoord.setValue( matrix[1][3] )
        self.YCoord.blockSignals( False )
        
        self.ZCoord.blockSignals( True )
        self.ZCoord.setValue( matrix[2][3] )
        self.ZCoord.blockSignals( False )
        

    def increaseTicks( self, tps=1, axis='x' ):
        if axis.lower() == 'x':
            self.XCoord.setValue( self.XCoord.value() + tps * self.step  )
        elif axis.lower() == 'y':
            self.YCoord.setValue( self.YCoord.value() + tps * self.step  )
        elif axis.lower() == 'z':
            self.ZCoord.setValue( self.ZCoord.value() + tps * self.step  )

    def decreaseTicks( self, tps=1, axis='x' ):
        if axis.lower() == 'x':
            self.XCoord.setValue( self.XCoord.value() - tps * self.step  )
        elif axis.lower() == 'y':
            self.YCoord.setValue( self.YCoord.value() - tps * self.step  )
        elif axis.lower() == 'z':
            self.ZCoord.setValue( self.ZCoord.value() - tps * self.step  )

    def activate( self, mode :bool = True ):
        self.XCoord.active = mode
        self.YCoord.active = mode
        self.ZCoord.active = mode