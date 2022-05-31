from RUtils.RTypes import RPoint, RJoint, RFrame

class RLinearInterpolator():
    def __init__( self, prev : RPoint, pos : RPoint, res : float = 1 ):
        self.prev = prev
        self.pos = pos
        self.res = res
        v = pos - prev
        self.d = ~v
        if self.d:
            self.v = v / self.d
        else: 
            self.v = RPoint()

    def step( self, d : float ):
        return self.v * d + self.prev

    def lineal_interpol( self ):
        for i in range( int( self.d // self.res ) ):
            yield self.step( float( i * self.res ) )
        yield self.pos

    