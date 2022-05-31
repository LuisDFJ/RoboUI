import re
import numpy as np
from RUtils.RTypes import RPoint, RJoint
from RGLEngine.RGenDGM import RGenDGM
from RGLEngine.RGenIGM import RGenIGM
from RUtils.RInterpolation import RLinearInterpolator


class RTrajectories():
    VALID_COMMANDS = [ "movej", "movel", "movec", "setj", "pass" ]
    def __init__(self, file : str, mode : str = 'rad', res : float = 10):
        self.file = file
        self.mode = mode
        self.res = res
        self.commands = []
        self.variables = {}
        self.DGM = RGenDGM()
        self.IGM = RGenIGM()
        self.prevJoints = RJoint()
        self.readPath()
        
    
    def getPoints(self, vals : str ):
        points = re.findall( '(?<=\().+?(?=\))', vals )
        val = []
        for point in points:
            if point not in list( self.variables.keys() ):
                p = point.split( "," )
                val.append( RPoint( float( p[0] ), float( p[1] ), float( p[2] ) ) )
            else:
                val.append( self.variables[ point ] )
        return val

    def readPath(self):
        with open( self.file, "r" ) as file:
            text = file.read()
        commands = text.split( ";" )
        self.commands = []
        for command in commands:
            c_command = command.replace( " ", "" ).replace( ";", "" ).replace( "\n", "" )
            if ":" in c_command:
                s_command = c_command.split( ":" )
                mode = s_command[0].lower()
                if "pass" in c_command.lower():
                    vals = int( s_command[1] )
                else:
                    vals = self.getPoints( s_command[1] )
                if mode in self.VALID_COMMANDS:
                    self.commands.append( ( mode,vals ) )
            elif "=" in c_command:
                s_var   = c_command.split( "=" )
                varname = s_var[0]
                val     = self.getPoints( s_var[1] )[0]
                self.variables[ varname ] = val

    def _arg_min( self, fom_q ):
        min_fom = fom_q[0]
        min_i = 0
        for i, fom in enumerate( fom_q ):
            if fom < min_fom:
                min_fom = fom
                min_i = i
        return min_i

    def getBestSolution( self, q_IGM, q_Curr ):
        fom_q = []
        for q in q_IGM:
            if None not in q:
                fom = 0
                for i in range( len( q ) ):
                    fom = fom + ( q[ i ] - q_Curr[ i ] ) ** 2
                fom_q.append( fom )
        if len( fom_q ):
            return self._arg_min( fom_q )
        else:
            return 0

    def genDGM( self, joints : RJoint ):
        self.prevJoints = joints
        pos = self.DGM.GetDGM( list( joints ) )[ :-1,3 ].astype( np.float32 )
        return RPoint( pos[0], pos[1], pos[2] )

    def genIGM( self, pos : RPoint ):
        q_IGM = self.IGM.GetIGM( list( pos ), 'rad' )
        i = self.getBestSolution( q_IGM, list( self.prevJoints ) )
        q = q_IGM[ i ]
        joints = RJoint( q[0], q[1], q[2] )
        self.prevJoints = joints
        return joints

    def movej( self, pos : RPoint ):
        return self.genIGM( pos )

    def movel( self, prev : RPoint, pos : RPoint ):
        lin = RLinearInterpolator( prev, pos, self.res )
        for p in lin.lineal_interpol():
            yield self.genIGM( p )

    def movec( self, prev : RPoint, mid : RPoint, pos : RPoint ):
        for _ in range( 5 ):
            yield self.genIGM( pos )

    def runPath(self, exe='loop'):
        prev = RPoint()
        while(True):
            for command in self.commands:
                mode = command[0]
                params = command[1]
                if mode == 'pass':
                    for _ in range( params ):
                        yield False
                else:
                    if mode == 'movej':
                        print( "MOVE J" )
                        prev = params[0]
                        joints = self.movej( params[0] )
                        yield joints
                    elif mode == 'movel':
                        print( "MOVE L" )
                        pos = params[0]
                        for joints in self.movel( prev, pos ):
                            yield joints
                        prev = pos
                    elif mode == 'movec':
                        print( "MOVE C" )
                        mid = params[0]
                        pos = params[1]
                        for joints in self.movec( prev, mid, pos ):
                            yield joints
                        prev = pos
                    elif mode == 'setj':
                        print( "SET J" )
                        joints = params[0]
                        joints = RJoint( joints.x, joints.y, joints.z )
                        joints.parse()
                        prev = self.genDGM( joints )
                        yield joints
            yield None
            if exe == 'once':
                return
