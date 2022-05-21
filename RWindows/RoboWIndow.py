from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QTimer
from RWindows.RMainWindow import RMainWindow
from RGLEngine.RGenDGM import RGenDGM
from RGLEngine.RGenIGM import RGenIGM


class RoboWindow( QMainWindow, RMainWindow ):
    def __init__( self, parent=None ):
        QMainWindow.__init__(self, parent=parent)
        self.setupUI(self)
        self.WaistSlider.Slider.valueChanged.connect(self.getWaistValue)
        self.ShoulderSlider.Slider.valueChanged.connect(self.getShoulderValue)
        self.ElbowSlider.Slider.valueChanged.connect(self.getElbowValue)
        self.SerialCom.connectButton.clicked.connect(self.connectPort)

        self.Coords.XCoord.valueChanged.connect(self.getCoordsValue)
        self.Coords.YCoord.valueChanged.connect(self.getCoordsValue)
        self.Coords.ZCoord.valueChanged.connect(self.getCoordsValue)

        self.navMode.button.clicked.connect(self.toggleMode)

        self.activeKeys = []

        self.mode = 'IGM'
        self.DGM = RGenDGM()
        self.IGM = RGenIGM()
        self.setPosition()

        timer_graphics = QTimer(self)
        timer_graphics.setInterval(20)
        timer_graphics.timeout.connect(self.glWidget.update)

        timer_keyboard = QTimer(self)
        timer_keyboard.setInterval(20)
        timer_keyboard.timeout.connect(self.keyboardHandler)

        timer_graphics.start()
        timer_keyboard.start()


    def connectPort(self):
        self.SerialCom.startConnection()

    def activateSliders(self, mode:bool = True):
        self.WaistSlider    .activate( mode )
        self.ShoulderSlider .activate( mode )
        self.ElbowSlider    .activate( mode )

    def activateCoords(self, mode:bool = True):
        self.Coords.activate( mode )

    def calculateIGM(self, mode : str='deg'):
        X = self.Coords.getCoords()
        q = self.IGM.GetIGM( X, mode=mode )
        return q[ 2 ]

    def calculateDGM(self, q = None):
        if q == None:
            q = [ self.WaistSlider.value( "rad" ), self.ShoulderSlider.value( "rad" ), self.ElbowSlider.value( "rad" ) ]
        T = self.DGM.GetDGM( q )
        return T
    
    def setSliders(self, q, mode : str='rad' ):
        self.WaistSlider    .setValue( q[0], mode )
        self.ShoulderSlider .setValue( q[1], mode )
        self.ElbowSlider    .setValue( q[2], mode )
    
    def setSimulation(self, q):
        self.glWidget.setWaistValue     ( q[0] )
        self.glWidget.setShoulderValue  ( q[1] )
        self.glWidget.setElbowValue     ( q[2] )

    def toggleMode(self):
        if self.mode == 'IGM':
            self.toggleDGMIGM( 'DGM' )
        elif self.mode == 'DGM':
            self.toggleDGMIGM( 'IGM' )

    def toggleDGMIGM(self, mode):
        if self.mode != mode:
            self.mode = mode
            if mode == 'IGM':
                self.activateCoords( True )
                self.activateSliders( False )
            else:
                self.activateCoords( False )
                self.activateSliders( True )
            self.navMode.setMode( mode )

    def getCoordsValue(self):
        if self.mode == 'IGM':
            q = self.calculateIGM( 'rad' )
            if None not in q:
                self.setSimulation( q )
                self.setSliders( q )
                T = self.calculateDGM( q )
                self.Position.setPosition( T )
                self.setServos()
            

    def getWaistValue(self):
        if self.mode == 'DGM':
            WaistValue = self.WaistSlider.value( "rad" )
            self.glWidget.setWaistValue( WaistValue )
            self.setPosition()
            self.setServos()
    
    def getShoulderValue(self):
        if self.mode == 'DGM':
            ShoulderValue = self.ShoulderSlider.value( "rad" )
            self.glWidget.setShoulderValue( ShoulderValue )
            self.setPosition()
            self.setServos()

    def getElbowValue(self):
        if self.mode == 'DGM':
            ElbowValue = self.ElbowSlider.value( "rad" )
            self.glWidget.setElbowValue( ElbowValue )
            self.setPosition()
            self.setServos()

    def setPosition(self):
        T = self.calculateDGM()
        self.Position.setPosition( T )
        self.Coords.setPosition( T )

    def setServos(self):
        q = [ self.WaistSlider.value( "deg" ), self.ShoulderSlider.value( "deg" ), self.ElbowSlider.value( "deg" ) ]
        self.SerialCom.sendCommand( q )

    def closeEvent(self, e):
        self.SerialCom.endConnection()
        self.glWidget.deleteLater()
        self.glWidget = None
        print( "GoodBye" )

    def keyboardHandler(self):
        if len( self.activeKeys ):
            tps = self.statusbar.getTps()
            if Qt.Key.Key_Escape in self.activeKeys:
                self.close()

            move_keys = [ Qt.Key.Key_Q, Qt.Key.Key_A,
                          Qt.Key.Key_W, Qt.Key.Key_S,
                          Qt.Key.Key_E, Qt.Key.Key_D ]

            if any( [ x in self.activeKeys for x in move_keys ] ):
                if Qt.Key.Key_Shift in self.activeKeys:
                    self.toggleDGMIGM( 'DGM' )
                else:
                    self.toggleDGMIGM( 'IGM' )

            if Qt.Key.Key_Shift in self.activeKeys:
                # Joints control
                if Qt.Key.Key_Q in self.activeKeys:
                    self.WaistSlider.increaseTicks(tps)
                elif Qt.Key.Key_A in self.activeKeys:
                    self.WaistSlider.decreaseTicks(tps)

                if Qt.Key.Key_W in self.activeKeys:
                    self.ShoulderSlider.increaseTicks(tps)
                elif Qt.Key.Key_S in self.activeKeys:
                    self.ShoulderSlider.decreaseTicks(tps)

                if Qt.Key.Key_E in self.activeKeys:
                    self.ElbowSlider.increaseTicks(tps)
                elif Qt.Key.Key_D in self.activeKeys:
                    self.ElbowSlider.decreaseTicks(tps)
            else:
                # Linear control
                if Qt.Key.Key_Q in self.activeKeys:
                    self.Coords.increaseTicks(tps=tps, axis='x')
                elif Qt.Key.Key_A in self.activeKeys:
                    self.Coords.decreaseTicks(tps=tps, axis='x')

                if Qt.Key.Key_W in self.activeKeys:
                    self.Coords.increaseTicks(tps=tps, axis='y')
                elif Qt.Key.Key_S in self.activeKeys:
                    self.Coords.decreaseTicks(tps=tps, axis='y')

                if Qt.Key.Key_E in self.activeKeys:
                    self.Coords.increaseTicks(tps=tps, axis='z')
                elif Qt.Key.Key_D in self.activeKeys:
                    self.Coords.decreaseTicks(tps=tps, axis='z')

            if Qt.Key.Key_Plus in self.activeKeys:
                self.statusbar.increaseTps()
                self.statusbar.show()
            elif Qt.Key.Key_Minus in self.activeKeys:
                self.statusbar.decreaseTps()
                self.statusbar.show()
            

    def keyPressEvent(self, e):
        if e.key() not in self.activeKeys:
            self.activeKeys.append( e.key() )

    def keyReleaseEvent(self, e):
        if e.key() in self.activeKeys:
            self.activeKeys.remove( e.key() )
        