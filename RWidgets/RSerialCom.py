from PyQt5 import QtCore, QtGui, QtWidgets
from serial.tools.list_ports import comports
import serial
import time

class RSerialCom( QtWidgets.QWidget ):
    def __init__(self, parent=None):
        super( RSerialCom, self ).__init__( parent=parent )

        self.port_list = []
        self.serial = None

        layout = QtWidgets.QHBoxLayout( self )

        self.comPorts   = QtWidgets.QComboBox()
        view = QtWidgets.QListView()
        view.setMinimumWidth( 300 )
        self.comPorts.setView( view )

        self.refreshButton = QtWidgets.QPushButton( "Refresh" )
        self.connectButton = QtWidgets.QPushButton( "Connect" )

        layout.addWidget( QtWidgets.QLabel( "Ports" ) )
        layout.addWidget( self.comPorts )
        layout.addWidget( self.refreshButton )
        layout.addWidget( self.connectButton )

        self.refreshButton.clicked.connect( self.getComPorts )

        self.setLayout( layout )
    
    def getComPorts( self ):
        ports = []
        self.port_list = []
        for port, desc, _ in comports():
            ports.append( "{} - {}".format( port, desc ) )
            self.port_list.append( port )
        self.comPorts.clear()
        self.comPorts.addItems( ports )
    
    def getPort( self ):
        port = ""
        if len( self.port_list ):
            port = self.port_list[ self.comPorts.currentIndex() ]
        return port

    def startConnection( self ):
        self.endConnection()
        port = self.getPort()
        self.serial = serial.Serial( port, baudrate=115200 )
        time.sleep( 2.0 )

    def encodeSerial( self, waist, shoulder, elbow ):
        byteArray = ( int( waist ).to_bytes( 2, 'little' ) + 
                    int( shoulder ).to_bytes( 2, 'little' ) +
                    int( elbow ).to_bytes( 2, 'little' ) )
        return b"<" + byteArray + b">"
    
    def endConnection( self ):
        if self.serial != None:
            self.serial.close()
            self.serial = None

    def sendCommand( self, q ):
        if self.serial != None:
            q1 = int( 1023 * q[0] / 300 )
            q2 = int( 1023 * q[1] / 300 )
            q3 = int( 1023 * q[2] / 300 )
            command = self.encodeSerial( q1, q2, q3 )
            self.serial.write( command )
            time.sleep( 0.05 )
            