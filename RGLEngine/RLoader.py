import numpy
from pywavefront import Wavefront

class RLoader():
    def __init__(self, path, scale=1):
        self.scene = Wavefront( path, collect_faces=True )
        self.genVertices(scale)
        self.genElements()
        self.genNormals()
        self.genArray()

    def genArray(self):
        array = []
        for i, face in enumerate( self.elements ):
            for vertex in face:
                ver = self.vertices[ vertex ].tolist()
                nor = self.normals[ i ].tolist()
                array.append( ver + nor )
        self.array = numpy.array( array ).astype( numpy.float32 )

    def genVertices(self, scale):
        self.vertices = numpy.array( self.scene.vertices ).astype( numpy.float32 )
        self.vertices = self.vertices / scale

    def genElements(self):
        elements = []
        for mesh in self.scene.mesh_list:
            for face in mesh.faces:
                elements.append( face )
        self.elements = numpy.array( elements ).astype( numpy.int32 )

    def genNormals(self):
        normals = []
        for face in self.elements:
            P   = self.vertices[ face ]
            U   = P[ 1 ] - P[ 0 ]
            V   = P[ 2 ] - P[ 0 ]
            N   = numpy.cross( U, V )
            N   = N / numpy.sqrt(numpy.sum(N**2))
            normals.append( N )
        self.normals = numpy.array( normals ).astype( numpy.float32 )
        