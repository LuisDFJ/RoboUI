from PyQt5 import  QtWidgets
from RWindows.RoboWIndow import RoboWindow


if __name__ == "__main__":
    app     = QtWidgets.QApplication([])
    window = RoboWindow()
    window.show()
    app.exec_()