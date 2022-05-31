from PyQt5 import QtCore, QtGui, QtWidgets
from RMedia.Icons import __file__ as icons_file
from RMedia.Trajectories import __file__ as traj_file
from RUtils.RTrajectories import RTrajectories
import os

class RTrajectory( QtWidgets.QWidget ):
    def __init__(self, parent):
        self.setup( parent )
        self.trajectories = None
        self.run = False
        self.c = 0

    def setup(self, parent):
        super(RTrajectory, self).__init__(parent)
        layout          = QtWidgets.QVBoxLayout( self )
        sublayoutTop    = QtWidgets.QHBoxLayout()
        sublayoutBot    = QtWidgets.QHBoxLayout()
        sublayoutPrg    = QtWidgets.QHBoxLayout()
        layout.addLayout( sublayoutTop )
        layout.addLayout( sublayoutBot )
        layout.addLayout( sublayoutPrg )

        path = os.path.abspath( os.path.dirname(  icons_file ) )

        self.progress = QtWidgets.QProgressBar()

        self.load = QtWidgets.QPushButton( "Load" )
        self.play = QtWidgets.QPushButton( "Play" )
        self.stop = QtWidgets.QPushButton( "Stop" )
        self.step = QtWidgets.QPushButton( "Step" )

        self.load.setIcon( QtGui.QIcon( os.path.join( path, "file.png" ) ) )
        self.play.setIcon( QtGui.QIcon( os.path.join( path, "play.png" ) ) )
        self.stop.setIcon( QtGui.QIcon( os.path.join( path, "stop.png" ) ) )
        self.step.setIcon( QtGui.QIcon( os.path.join( path, "forward.png" ) ) )

        self.load.clicked.connect( self.loadTrajectory )
        self.play.clicked.connect( self.playTrajectory )
        self.stop.clicked.connect( self.stopTrajectory )

        self.file = QtWidgets.QLabel( "" )

        sublayoutTop.addWidget( self.load )
        sublayoutTop.addWidget( self.file )
        sublayoutBot.addWidget( self.play )
        sublayoutBot.addWidget( self.stop )
        sublayoutBot.addWidget( self.step )

        sublayoutPrg.addWidget( self.progress )

        self.setLayout( layout )

    def loadTrajectory( self ):
        path = os.path.abspath( os.path.dirname(  traj_file ) )
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName( self, "RoboUI Trajectory", path, "Robo UI trajectory file (*.rui)" )
        basename = os.path.basename( filepath )
        if os.path.isfile( filepath ) and basename.split( '.' )[1].lower() == 'rui':
            self.file.setText( basename )
            traj = RTrajectories( filepath )
            self.c = 0
            self.trajectories = traj.runPath()
            self.progress.setRange( 0, len( list( traj.runPath('once') ) ) )
            self.progress.setValue( 0 )
            
        else:
            self.file.setText( "" )
            self.progress.setRange( 0, 0 )
            self.progress.setValue( 0 )
            self.trajectories = None
            self.c = 0

    def playTrajectory( self ):
        self.run = True

    def stopTrajectory( self ):
        self.run = False

    def next(self):
        if self.trajectories != None:
            joints = next( self.trajectories, None )
            self.progress.setValue( self.c )
            if joints == None: self.c = 0
            else: self.c += 1
            return joints


