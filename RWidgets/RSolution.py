from PyQt5 import QtCore, QtGui, QtWidgets
from math import degrees
import numpy as np


class RSolution( QtWidgets.QWidget ):
    def __init__( self, parent=None ):
        super(RSolution,self).__init__( parent=parent )
        layout = QtWidgets.QHBoxLayout( self )
        sublayout_1 = QtWidgets.QVBoxLayout()
        sublayout_2 = QtWidgets.QVBoxLayout()
        sublayout_sol_1 = QtWidgets.QHBoxLayout()
        sublayout_sol_2 = QtWidgets.QHBoxLayout()
        sublayout_sol_3 = QtWidgets.QHBoxLayout()
        sublayout_sol_4 = QtWidgets.QHBoxLayout()
        layout.addLayout( sublayout_1 )
        layout.addLayout( sublayout_2 )
        sublayout_2.addLayout( sublayout_sol_1 )
        sublayout_2.addLayout( sublayout_sol_2 )
        sublayout_2.addLayout( sublayout_sol_3 )
        sublayout_2.addLayout( sublayout_sol_4 )
        
        solution_1 = QtWidgets.QLabel()
        solution_2 = QtWidgets.QLabel()
        solution_3 = QtWidgets.QLabel()
        solution_4 = QtWidgets.QLabel()

        selector_1 = QtWidgets.QRadioButton()
        selector_2 = QtWidgets.QRadioButton()
        selector_3 = QtWidgets.QRadioButton()
        selector_4 = QtWidgets.QRadioButton()
        
        selector_1.setAutoExclusive( False )
        selector_2.setAutoExclusive( False )
        selector_3.setAutoExclusive( False )
        selector_4.setAutoExclusive( False )

        selector_1.toggled.connect( lambda: self.radioHandler(0) )
        selector_2.toggled.connect( lambda: self.radioHandler(1) )
        selector_3.toggled.connect( lambda: self.radioHandler(2) )
        selector_4.toggled.connect( lambda: self.radioHandler(3) )

        self.solution = [ solution_1, solution_2, solution_3, solution_4 ]
        self.selector = [ selector_1, selector_2, selector_3, selector_4 ]

        sublayout_1.addWidget( QtWidgets.QLabel( "IGM solutions" ) )
        sublayout_sol_1.addWidget( solution_1 )
        sublayout_sol_1.addWidget( selector_1 )
        sublayout_sol_2.addWidget( solution_2 )
        sublayout_sol_2.addWidget( selector_2 )
        sublayout_sol_3.addWidget( solution_3 )
        sublayout_sol_3.addWidget( selector_3 )
        sublayout_sol_4.addWidget( solution_4 )
        sublayout_sol_4.addWidget( selector_4 )
        empty = [ [None,None,None],
                  [None,None,None],
                  [None,None,None],
                  [None,None,None] ]
        self.setSolution( empty )
        self.setLayout( layout )

    def radioHandler( self, r ):
        if self.selector[r].isChecked():
            for i, b in enumerate( self.selector ):
                if i != r: b.setChecked( False )
        
    def getSelectorId( self ):
        for i, b in enumerate( self.selector ):
            if b.isChecked(): return True, i
        return False, -1

    def _arg_min( self, fom_q ):
        min_fom = fom_q[0]
        min_i = 0
        for i, fom in enumerate( fom_q ):
            if fom < min_fom:
                min_fom = fom
                min_i = i
        return min_i

    def getBestSolution( self, q_IGM, q_Curr, mode : str='rad' ):
        fix, id = self.getSelectorId()
        if not fix:
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
        else:
            return id

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
        
