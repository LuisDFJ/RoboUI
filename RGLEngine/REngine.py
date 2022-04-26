from OpenGL import GL, GLU
from OpenGL.GL import shaders
from OpenGL.arrays import vbo
import numpy as np
import os

class REngine( object ):
    def __init__(self):
        self.VShaderPath = os.path.join( os.path.dirname( __file__ ), r"Shaders\RVertexShader.gs" )
        self.FShaderPath = os.path.join( os.path.dirname( __file__ ), r"Shaders\RFragmentShader.gs" )
        self.float32size = 4
        GL.glClearColor( 0.0, 0.0, 1.0, 1.0 )
        GL.glEnable(GL.GL_DEPTH_TEST)

    def _readShader(self, path):
        with open( path ) as shader:
            text = shader.read()
        return text
        
    def createShaderProgram(self):
        vertex      = shaders.compileShader( self._readShader(self.VShaderPath), GL.GL_VERTEX_SHADER )
        fragment    = shaders.compileShader( self._readShader(self.FShaderPath), GL.GL_FRAGMENT_SHADER )
        self.shader = shaders.compileProgram( vertex, fragment )

    def useShaderProgram(self, mode=True):
        if mode:
            GL.glUseProgram( self.shader )
        else:
            GL.glUseProgram( 0 )

    def setUniformMatrix4fv(self, name, matrix):
        location = GL.glGetUniformLocation( self.shader, name )
        GL.glUniformMatrix4fv( location, 1, GL.GL_TRUE, matrix.astype( np.float32 ) )

    def createVAO(self, vertices, elements=None):
        
        vao = GL.glGenVertexArrays( 1 )
        GL.glBindVertexArray( vao )

        vVBO = vbo.VBO( vertices.astype( np.float32 ) )
        vVBO.bind()

        if isinstance( elements, np.ndarray ):
            eEBO = vbo.VBO( elements.astype( np.uint32 ), target=GL.GL_ELEMENT_ARRAY_BUFFER )
            eEBO.bind()
        
        GL.glVertexAttribPointer( 0, 3, GL.GL_FLOAT, False, 6 * self.float32size, vVBO )
        GL.glEnableVertexAttribArray( 0 )
        GL.glVertexAttribPointer( 1, 3, GL.GL_FLOAT, False, 6 * self.float32size, vVBO + 3 * self.float32size )
        GL.glEnableVertexAttribArray( 1 )

        GL.glBindVertexArray( 0 )
        return vao

    def useVAO(self, vao=0):
        GL.glBindVertexArray( vao )