from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QTimer
from RWindows.RMainWindow import RMainWindow

class RoboWindow( QMainWindow, RMainWindow ):
    def __init__( self, parent=None ):
        QMainWindow.__init__(self, parent=parent)
        self.setupUI(self)
        self.WaistSlider.Slider.valueChanged.connect(self.getWaistValue)
        self.ShoulderSlider.Slider.valueChanged.connect(self.getShoulderValue)
        self.ElbowSlider.Slider.valueChanged.connect(self.getElbowValue)


        timer = QTimer(self)
        timer.setInterval(20)
        timer.timeout.connect(self.glWidget.update)
        timer.start()

    def getWaistValue(self):
        WaistValue = self.WaistSlider.value( "rad" )
        self.glWidget.setWaistValue( WaistValue )
    
    def getShoulderValue(self):
        ShoulderValue = self.ShoulderSlider.value( "rad" )
        self.glWidget.setShoulderValue( ShoulderValue )

    def getElbowValue(self):
        ElbowValue = self.ElbowSlider.value( "rad" )
        self.glWidget.setElbowValue( ElbowValue )

    def closeEvent(self, e):
        self.glWidget.deleteLater()
        self.glWidget = None
        print( "GoodBye" )

    def keyPressEvent(self, e):
        tps = self.statusbar.getTps()
        if e.key() == Qt.Key.Key_Escape:
            self.close()

        elif e.key() == Qt.Key.Key_Q:
            self.WaistSlider.increaseTicks(tps)
        elif e.key() == Qt.Key.Key_A:
            self.WaistSlider.decreaseTicks(tps)

        elif e.key() == Qt.Key.Key_W:
            self.ShoulderSlider.increaseTicks(tps)
        elif e.key() == Qt.Key.Key_S:
            self.ShoulderSlider.decreaseTicks(tps)
        
        elif e.key() == Qt.Key.Key_E:
            self.ElbowSlider.increaseTicks(tps)
        elif e.key() == Qt.Key.Key_D:
            self.ElbowSlider.decreaseTicks(tps)

        elif e.key() == Qt.Key.Key_Plus:
            self.statusbar.increaseTps()
            self.statusbar.show()
        elif e.key() == Qt.Key.Key_Minus:
            self.statusbar.decreaseTps()
            self.statusbar.show()