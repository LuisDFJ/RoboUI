class RTrajectories():
    def __init__(self, file : str):
        self.file = file
    
    def readPath(self):
        with open( self.file, "r" ) as file:
            text = file.read()
        commands = text.split( ";" )
        for command in commands:
            print( command.replace( " ", "" ).replace( ";", "" ).replace( "\n", "" ) )