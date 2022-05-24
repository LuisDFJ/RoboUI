from PyQt5 import QtCore, QtGui, QtWidgets
from math import degrees
import numpy as np


class RSolution( QtWidgets.QWidget ):
    def __init__( self, parent=None ):
        super(RSolution,self).__init__( parent=parent )
        layout = QtWidgets.QHBoxLayout( self )
        sublayout_1 = QtWidgets.QVBoxLayout()
        sublayout_2 = QtWidgets.QVBoxLayout()
        layout.addLayout( sublayout_1 )
        layout.addLayout( sublayout_2 )
        
        solution_1 = QtWidgets.QLabel()
        solution_2 = QtWidgets.QLabel()
        solution_3 = QtWidgets.QLabel()
        solution_4 = QtWidgets.QLabel()

        self.solution = [ solution_1, solution_2, solution_3, solution_4 ]

        sublayout_1.addWidget( QtWidgets.QLabel( "IGM solutions" ) )
        sublayout_2.addWidget( solution_1 )
        sublayout_2.addWidget( solution_2 )
        sublayout_2.addWidget( solution_3 )
        sublayout_2.addWidget( solution_4 )
        empty = [ [None,None,None],
                  [None,None,None],
                  [None,None,None],
                  [None,None,None] ]
        self.setSolution( empty )
        self.setLayout( layout )

    def _arg_min( self, fom_q ):
        min_fom = fom_q[0]
        min_i = 0
        for i, fom in enumerate( fom_q ):
            if fom < min_fom:
                min_fom = fom
                min_i = i
        return min_i

    def getBestSolution( self, q_IGM, q_Curr, mode : str='rad' ):
        fom_q = []
        for q in q_IGM:
            if None not in q:
                fom = 0
                for i in range( len( q ) ):
                    if mode == 'deg': fom = fom + ( q[ i ] - q_Curr[ i ] ) ** 2
                    elif mode == 'rad': fom = fom + ( degrees( q[ i ] ) - q_Curr[ i ] ) ** 2
                fom_q.append( fom )
        if len( fom_q ):
            return self._arg_min( fom_q )
        else:
            return 0

    def setSolution( self, matrix, mode : str='rad', index : int=0 ):
        for n, sol in enumerate( self.solution ):
            smatrix = ""
            for val in matrix[n]:
                if val != None:
                    if mode == 'rad':
                        line = "{:<12}".format( "{:.2f}".format( degrees( val ) ) )
                    else:
                        line = "{:<12}".format( "{:.2f}".format( val ) )
                else:
                    line = "{:<12}".format( "NaN" )
                smatrix = smatrix + line
            sol.setText( smatrix )
            if n == index: sol.setStyleSheet( "color: blue" )
            else: sol.setStyleSheet( "color: black" )
        
