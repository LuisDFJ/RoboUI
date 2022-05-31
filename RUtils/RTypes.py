from math import sqrt, radians, degrees

class RPoint():
    def __init__( self, x: float=0.0, y: float=0.0, z: float=0.0 ):
        self.x = x
        self.y = y
        self.z = z
    def __str__( self ):
        return "{:0.4f}, {:0.4f}, {:0.4f}".format( self.x,self.y,self.z )
    def __iter__( self ):
        yield self.x
        yield self.y
        yield self.z
    def __add__( self, P ):
        return RPoint( self.x + P.x , self.y + P.y, self.z + P.z )
    def __sub__( self, P ):
        return RPoint( self.x - P.x , self.y - P.y, self.z - P.z )
    def __truediv__( self, a : float ):
        return RPoint( self.x / a, self.y / a, self.z / a )
    def __neg__( self ):
        return RPoint( -self.x, -self.y, -self.z )
    def __invert__( self ):
        return sqrt( self.x ** 2 + self.y ** 2 + self.z ** 2 )
    def __mod__( self, P ):
        x = self.y * P.z - self.z * P.y
        y = self.z * P.x - self.x * P.z
        z = self.x * P.y - self.y * P.x
        return RPoint( x,y,z )
    def __mul__( self, P ):
        if isinstance( P, self.__class__ ):
            return self.x * P.x + self.y * P.y + self.z * P.z
        if isinstance( P, float ):
            return RPoint( self.x * P, self.y * P, self.z * P )

class RFrame():
    def __init__( self, Nx: RPoint, Ny: RPoint, Nz: RPoint ):
        self.Nx = Nx
        self.Ny = Ny
        self.Nz = Nz
    def __str__( self ):
        line =  "{:0.4f}, {:0.4f}, {:0.4f}\n".format( self.Nx.x,self.Ny.x,self.Nz.x )
        line += "{:0.4f}, {:0.4f}, {:0.4f}\n".format( self.Nx.y,self.Ny.y,self.Nz.y )
        line += "{:0.4f}, {:0.4f}, {:0.4f}"  .format( self.Nx.z,self.Ny.z,self.Nz.z )
        return line
    def __iter__( self ):
        yield list( self.Nx )
        yield list( self.Ny )
        yield list( self.Nz )
    def __invert__( self ):
        Nx = RPoint( self.Nx.x, self.Ny.x, self.Nz.x, )
        Ny = RPoint( self.Nx.y, self.Ny.y, self.Nz.y, )
        Nz = RPoint( self.Nx.z, self.Ny.z, self.Nz.z, )
        return RFrame( Nx, Ny, Nz )
    def __mod__( self, P : RPoint ):
        F = ~self
        x = F.Nx * P
        y = F.Ny * P
        z = F.Nz * P
        return RPoint( x, y, z )

class RJoint():
    def __init__( self, x: float=0.0, y: float=0.0, z: float=0.0 ):
        self.x = x
        self.y = y
        self.z = z
    def __str__( self ):
        return "j{}, {}, {}".format( self.x,self.y,self.z )
    def __iter__( self ):
        yield self.x
        yield self.y
        yield self.z
    def parse( self, mode : str = 'rad' ):
        if mode == 'rad':
            self.x = radians( self.x )
            self.y = radians( self.y )
            self.z = radians( self.z )
        elif mode == 'deg':
            self.x = degrees( self.x )
            self.y = degrees( self.y )
            self.z = degrees( self.z )
