from PyQt5 import QtCore, QtGui, QtWidgets
from RWidgets.RJointSlider import RJointSliderWidget
from RWidgets.RSerialCom import RSerialCom
from RWidgets.RStatusBar import RStatusBar
from RWidgets.RGLWidget import RGLWidget
from RWidgets.RPosition import RPosition
from RWidgets.RSolution import RSolution
from RWidgets.RCoordinates import RCoordinates
from RWidgets.RNavigationMode import RNavigationMode

class RMainWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 584)
        # Central Widget Init
        self.centralwidget  = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Menu Bar Init
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 21))
        self.menubar.setObjectName("menubar")
        # Status Bar Init
        self.statusbar = RStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # Widgets Init
        self.setup()
        # MainWindow Setup
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setup(self):
        self._setupCentralWidget( self.centralwidget )
        self._setupMenuBar( self.menubar )
        self._setupStatusBar( self.statusbar )

    def _setupCentralWidget(self, widget):
        # OpenGL Widget
        self.glWidget = RGLWidget( widget )
        self.glWidget.setGeometry(QtCore.QRect(0, 0, 591, 531))
        # Navigation Mode
        self.navMode = RNavigationMode( widget )
        self.navMode.setGeometry(QtCore.QRect(670, 20, 180, 50))
        # COM Ports
        self.SerialCom = RSerialCom( widget )
        self.SerialCom.setGeometry(QtCore.QRect(640, 80, 220, 50))
        # Waist Slider
        self.WaistSlider    = RJointSliderWidget( widget, Title="Joint: Waist (Q/A)", MaxVal=150, MinVal=-150 )
        self.WaistSlider    .setGeometry(QtCore.QRect(640, 120, 220, 50))
        # Shoulder Slider
        self.ShoulderSlider = RJointSliderWidget( widget, Title="Joint: Shoulder (W/S)", MaxVal=150, MinVal=-150 )
        self.ShoulderSlider .setGeometry(QtCore.QRect(640, 160, 220, 50))
        # Elbow Slider
        self.ElbowSlider    = RJointSliderWidget( widget, Title="Joint: Elbow (E/D)", MaxVal=150, MinVal=-150 )
        self.ElbowSlider    .setGeometry(QtCore.QRect(640, 200, 220, 50))
        # Coordinates Input
        self.Coords       = RCoordinates( widget )
        self.Coords       .setGeometry(QtCore.QRect(640, 250, 180, 90))
        # Position Display
        self.Position       = RPosition( widget )
        self.Position       .setGeometry(QtCore.QRect(600, 320, 280, 150))
        # Solutions Display
        self.Solution       = RSolution( widget )
        self.Solution       .setGeometry(QtCore.QRect(600, 450, 250, 80))

        
    def _setupMenuBar(self, widget):
        pass

    def _setupStatusBar(self, widget):
        self.statusbar.show()