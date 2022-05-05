from PyQt5 import QtCore, QtGui, QtWidgets
from RWidgets.RJointSlider import RJointSliderWidget
from RWidgets.RSerialCom import RSerialCom
from RWidgets.RStatusBar import RStatusBar
from RWidgets.RGLWidget import RGLWidget
from RWidgets.RPosition import RPosition

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
        #self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setup(self):
        self._setupCentralWidget( self.centralwidget )
        self._setupMenuBar( self.menubar )
        self._setupStatusBar( self.statusbar )

    def _setupCentralWidget(self, widget):
        # OpenGL Widget
        self.glWidget = RGLWidget( widget )
        self.glWidget.setGeometry(QtCore.QRect(0, 0, 591, 531))
        # COM Ports
        self.SerialCom = RSerialCom( widget )
        self.SerialCom.setGeometry(QtCore.QRect(640, 130, 220, 50))
        # Waist Slider
        self.WaistSlider    = RJointSliderWidget( widget, Title="Joint: Waist (Q/A)", MaxVal=100, MinVal=0 )
        self.WaistSlider    .setGeometry(QtCore.QRect(640, 190, 220, 50))
        # Shoulder Slider
        self.ShoulderSlider = RJointSliderWidget( widget, Title="Joint: Shoulder (W/S)", MaxVal=100, MinVal=0 )
        self.ShoulderSlider .setGeometry(QtCore.QRect(640, 230, 220, 50))
        # Elbow Slider
        self.ElbowSlider    = RJointSliderWidget( widget, Title="Joint: Elbow (E/D)", MaxVal=100, MinVal=0 )
        self.ElbowSlider    .setGeometry(QtCore.QRect(640, 270, 220, 50))
        # Position Display
        self.Position       = RPosition( widget )
        self.Position       .setGeometry(QtCore.QRect(600, 340, 280, 150))

        
    def _setupMenuBar(self, widget):
        pass

    def _setupStatusBar(self, widget):
        self.statusbar.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DGMLabel.setText(_translate("MainWindow", "Direct Geometric Model"))
        self.WaistLabel.setText(_translate("MainWindow", "Joints: Waist (q/a)"))
        self.WaistMinLabel.setText(_translate("MainWindow", "0 rad"))
        self.WaistMaxLabel.setText(_translate("MainWindow", "3.14 rad"))
        self.ShoulderMinLabel.setText(_translate("MainWindow", "0 rad"))
        self.ShoulderLabel.setText(_translate("MainWindow", "Joints: Shoulder (w/s)"))
        self.ShoulderMaxLabel.setText(_translate("MainWindow", "3.14 rad"))
        self.ElbowLabel.setText(_translate("MainWindow", "Joints: Elbow (e/d)"))
        self.ElbowMinLabel.setText(_translate("MainWindow", "0 rad"))
        self.ElbowMaxLabel.setText(_translate("MainWindow", "3.14 rad"))
        self.IGMLabel.setText(_translate("MainWindow", "Inverse Geometric Model"))
        self.XLabel.setText(_translate("MainWindow", "X axis"))
        self.YLabel.setText(_translate("MainWindow", "Y axis"))
        self.ZLabel.setText(_translate("MainWindow", "Z axis"))
        self.DegreesButton.setText(_translate("MainWindow", "Degrees"))
        self.DGMButton.setText(_translate("MainWindow", "DGM"))
        self.IGMButton.setText(_translate("MainWindow", "IGM"))
        self.ModeLabel.setText(_translate("MainWindow", "Mode"))

    