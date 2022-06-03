from math import pi
from math import atan2, sqrt, cos, sin, degrees
from RUtils.RAnglesUtil import getIGMAngle

class RGenIGM():
    def __init__( self, L1=36.0, L2=93.5, L3=210.0 ):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3

    #Type 2 equation function: Returns two possible solutions for q
    def Type2 ( self, Pos ):
        PX = Pos[0]; PY = Pos[1]
        X = PX; Y = -PY; Z = 0
        q1_1 = None
        q1_2 = None
        if X != 0 or Y != 0:
            if X == 0 and Y != 0:
                C1 = Z/Y
                q1_1 = atan2( sqrt(1-C1**2), C1 )
                q1_2 = atan2(-sqrt(1-C1**2), C1 )
            elif Y == 0 and X != 0:
                S1 = Z/X
                q1_1 = atan2( S1,  sqrt(1-S1**2) )
                q1_2 = atan2( S1, -sqrt(1-S1**2) )
            elif X != 0 and Y != 0 and Z == 0:
                q1_1 = atan2( -Y, X )
                q1_2 = q1_1 + pi
            else:
                S1 = ( X*Z+Y*sqrt(X**2+Y**2-Z**2) ) / (X**2+Y**2)
                C1 = ( Y*Z-X*sqrt(X**2+Y**2-Z**2) ) / (X**2+Y**2)
                q1_1 = atan2(S1,C1)
                
                S2 = (X*Z-Y*sqrt(X**2+Y**2-Z**2)) / (X**2+Y**2)
                C2 = (Y*Z+X*sqrt(X**2+Y**2-Z**2)) / (X**2+Y**2)
                q1_2 = atan2(S2,C2)
        return q1_1, q1_2

    #Type 8 equation function: Requires q1 input. Returns two possible solutions for q2 and q3
    def Type8 (self, Pos, q):
        PX = Pos[0]; PY = Pos[1]; PZ = Pos[2]
        L1=self.L1; L2=self.L2; L3=self.L3
        
        q2_1 = None
        q2_2 = None
        q3_1 = None
        q3_2 = None
        
        if q != None:
            X1 = L2 
            Y1 = L3
            Z1 = PX*cos(q)+PY*sin(q)
            Z2 = PZ-L1     

            cosq3 = ((Z1**2)+(Z2**2)-(X1**2)-(Y1**2))/(2*X1*Y1)
            
            if cosq3 < 1 and cosq3 > -1:
                
                q3_1 = atan2(sqrt(1-(cosq3)**2),cosq3)
                q3_2 = atan2(-sqrt(1-(cosq3)**2),cosq3)
                
            
                B1 = X1+Y1*cosq3
                B2_option1 = Y1*sin(q3_1)
                B2_option2 = Y1*sin(q3_2)
            
                sinq2_option1 = ((B1*Z2)-(B2_option1*Z1))/((B1**2)+(B2_option1**2))
                cosq2_option1 = ((B1*Z1)+(B2_option1*Z2))/((B1**2)+(B2_option1**2))
            
                sinq2_option2 = ((B1*Z2)-(B2_option2*Z1))/((B1**2)+(B2_option2**2))
                cosq2_option2 = ((B1*Z1)+(B2_option2*Z2))/((B1**2)+(B2_option2**2))
            
                q2_1 = atan2(sinq2_option1,cosq2_option1)
                q2_2 = atan2(sinq2_option2,cosq2_option2)

        return q2_1, q2_2, q3_1, q3_2



    def GetIGM( self, Pos, mode='deg'):
        
        q1_1, q1_2 = self.Type2 (Pos)
        q2_1, q2_2, q3_1, q3_2 = self.Type8(Pos,q1_1)
        q2_3, q2_4, q3_3, q3_4 = self.Type8(Pos,q1_2)
        
            
        IGM = [ getIGMAngle( [q1_1,q2_1,q3_1] ),
                getIGMAngle( [q1_1,q2_2,q3_2] ),
                getIGMAngle( [q1_2,q2_3,q3_3] ),
                getIGMAngle( [q1_2,q2_4,q3_4] ) ]
        if mode == 'deg':
            return self.toDegrees( IGM )
        else:
            return IGM

    def toDegrees( self, IGM ):
        nIGM = []
        for sol in IGM:
            solution = []
            for q in sol:
                if q != None:
                    solution.append( degrees( q ) )
                else:
                    solution.append( None )
            nIGM.append( solution )

        return nIGM








#from math import pi
#from math import atan2, sqrt, cos, sin, degrees
#from RUtils.RAnglesUtil import getIGMAngle
#
#class RGenIGM():
#    def __init__( self, L1=36.0, L2=93.5, L3=203.0 ):
#        self.L1 = L1
#        self.L2 = L2
#        self.L3 = L3
#
#    def getQ1( self, x, y ):
#        """ Type 2 equation to obtain q1 """
#        
#        X = x; Y = -y
#        if X != 0 and Y !=0 :
#            S1 = ( Y*sqrt( X**2 + Y**2 ) ) / ( X**2 + Y**2 )
#            C1 = (-X*sqrt( X**2 + Y**2 ) ) / ( X**2 + Y**2 )
#            q1 = atan2(S1,C1) 
#            
#            S2 = (-Y*sqrt( X**2 + Y**2 ) ) / ( X**2 + Y**2 )
#            C2 = ( X*sqrt( X**2 + Y**2 ) ) / ( X**2 + Y**2 )
#            q2 = atan2(S2,C2)
#            return q1, q2
#        return None, None
#
#    def getQ23( self, x, y, z, q1 ):
#        """ Type 8 equation to solve q2 and q3 for first q1 option """
#        X = self.L2
#        Y = self.L3
#        
#        q2_1 = None
#        q2_2 = None
#        q3_1 = None
#        q3_2 = None
#
#        if q1 != None:
#            Z1 = x * cos(q1) + y * sin(q1)
#            Z2 = z - self.L1
#
#            C3 = ( Z1**2 + Z2**2 - X**2 - Y**2 ) / ( 2*X*Y )
#
#            if C3 < 1:
#                q3_1 = atan2( sqrt( 1 - C3**2 ), C3 )
#                q3_2 = atan2(-sqrt( 1 - C3**2 ), C3 )
#
#                B1 = X + Y * C3
#                B2_1 = Y * sin( q3_1 )
#                B2_2 = Y * sin( q3_2 )
#
#                S2_1 = ( B1*Z2 - B2_1*Z1 ) / ( B1**2 + B2_1**2 )
#                C2_1 = ( B1*Z1 + B2_1*Z2 ) / ( B1**2 + B2_1**2 )
#
#                S2_2 = ( B1*Z2 - B2_2*Z1 ) / ( B1**2 + B2_2**2 )
#                C2_2 = ( B1*Z1 + B2_2*Z2 ) / ( B1**2 + B2_2**2 )
#
#                q2_1 = atan2( S2_1, C2_1 ) 
#                q2_2 = atan2( S2_2, C2_2 )
#        
#        return q2_1, q2_2, q3_1, q3_2
#            
#
#    def GetIGM( self, Pos, mode='deg' ):
#        x = Pos[0]; y = Pos[1]; z = Pos[2]
#        q1_1, q1_2 = self.getQ1( x, y )
#        
#        q2_1, q2_2, q3_1, q3_2 = self.getQ23( x, y, z, q1_1 )
#        q2_3, q2_4, q3_3, q3_4 = self.getQ23( x, y, z, q1_2 )
#
#        IGM = [ getIGMAngle( [q1_1,q2_1,q3_1] ),
#                getIGMAngle( [q1_1,q2_2,q3_2] ),
#                getIGMAngle( [q1_2,q2_3,q3_3] ),
#                getIGMAngle( [q1_2,q2_4,q3_4] ) ]
#        if mode == 'deg':
#            return self.toDegrees( IGM )
#        else:
#            return IGM
#
#    def toDegrees( self, IGM ):
#        nIGM = []
#        for sol in IGM:
#            solution = []
#            for q in sol:
#                if q != None:
#                    solution.append( degrees( q ) )
#                else:
#                    solution.append( None )
#            nIGM.append( solution )
#
#        return nIGM
#
#
#