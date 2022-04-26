from PyQt5.QtWidgets import QStatusBar

class RStatusBar( QStatusBar ):
    def __init__(self, parent=None, Max=10, Min=1 ):
        super( QStatusBar, self ).__init__(parent=parent)
        self.tps = 1
        self.Max = Max
        self.Min = Min
    def increaseTps(self):
        self.tps = min( self.Max, self.tps + 1 )
    def decreaseTps(self):
        self.tps = max( self.Min, self.tps - 1 )
    def getTps(self):
        return self.tps
    def show(self):
        message = f"Ticks per second (+/-): {self.tps}"
        self.showMessage( message )