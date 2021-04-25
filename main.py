from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5 import Qt
from GUI import MainWindow
import Sprite
import GUI
from Sprite import State, FaceDir, SpriteObject
import sys
import copy
import random
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie, QPainter, QPixmap

class Sprite_Controls (QtWidgets.QMainWindow, MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setGeometry(100, 100, 1200, 450)
        self.setFixedSize(600, 450)
        self.movie = QMovie("yeahboi1.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()
        self.setWindowTitle("Yeah Boi!")

        self.FlameStag = Sprite.FlameStag
        self.FlameStag.currentState = State.intro
        self.FlameStag.posX = 450
        self.FlameStag.posY = 0

        self.gravitation = 50

        self.counterForRespawn = 0

        self.timer = QtCore.QTimer()

        self.timer.start(100)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Sprite_Controls()
    controller.platform()
    controller.definelabels()
    controller.show()
    sys.exit(app.exec_())
