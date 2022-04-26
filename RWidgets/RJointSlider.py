from PyQt5 import QtCore, QtGui, QtWidgets
from math import radians, degrees

RESOLUTION  = 100
DIVIDER     = 4

class RJointSliderWidget( QtWidgets.QWidget ):
    def __init__(self, parent, Title="Joint: Waist (Q/A)", MaxVal=180, MinVal=0, Step=0.25):
        super(RJointSliderWidget, self).__init__(parent)
        layout          = QtWidgets.QVBoxLayout( self )
        sublayoutTitle  = QtWidgets.QHBoxLayout()
        sublayoutSlider = QtWidgets.QHBoxLayout()
        layout.addLayout( sublayoutTitle )
        layout.addLayout( sublayoutSlider )
        
        # Title
        self.TitleLabel = QtWidgets.QLabel(self)
        self.TitleLabel.setObjectName("TitleLabel")
        # Slider Widget
        self.Slider = QtWidgets.QSlider(self)
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Slider.setObjectName("Slider")
        # Min Label
        self.MinLabel = QtWidgets.QLabel(self)
        self.MinLabel.setObjectName("MinLabel")
        # Max Label
        self.MaxLabel = QtWidgets.QLabel(self)
        self.MaxLabel.setObjectName("MaxLabel")
        # Set  Values
        self.MaxVal = MaxVal
        self.MinVal = MinVal
        self.Title  = Title
        self.Step   = Step
        self.mode   = "deg"
        self.toggleLabels(self.mode)
        self.setTitle()
        # Connections
        self.Slider.valueChanged.connect(self.setTitle)
        # Layout
        sublayoutTitle.addWidget( self.TitleLabel )
        sublayoutSlider.addWidget( self.MinLabel )
        sublayoutSlider.addWidget( self.Slider )
        sublayoutSlider.addWidget( self.MaxLabel )
        self.setLayout( layout )

    def setLimits(self, Min, Max, id="°"):
        self.MinLabel.setText( "{:.2f}{}".format( Min, id ) )
        self.MaxLabel.setText( "{:.2f}{}".format( Max, id ) )
        self.Slider.setMinimum( Min * RESOLUTION )
        self.Slider.setMaximum( Max * RESOLUTION )
        self.Slider.setSingleStep( self.Step * RESOLUTION )

    def toggleLabels(self, format="rad"):
        if format == "rad":
            self.setLimits( radians( self.MinVal ), radians( self.MaxVal ), " rad" )
            self.mode = "rad"
        elif format == "deg":
            self.setLimits( self.MinVal, self.MaxVal, " °" )
            self.mode = "deg"

    def value( self, mode=None ):
        val = self.Slider.value() // ( RESOLUTION // DIVIDER ) / DIVIDER
        if mode == None:
            return val
        
        if mode == "rad" and self.mode == "deg":
            return radians( val )
        elif mode == "deg" and self.mode == "rad":
            return degrees( val )
        else:
            return val

    def setTitle( self ):
        self.TitleLabel.setText( "{} -> {:.2f}".format( self.Title, self.value() ) )

    def increaseTicks( self, tps=1 ):
        self.Slider.setValue( ( self.value() + tps * self.Step ) * RESOLUTION )

    def decreaseTicks( self, tps=1 ):
        self.Slider.setValue( ( self.value() - tps * self.Step ) * RESOLUTION )