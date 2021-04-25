import sys
from PyQt5 import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie, QPainter, QPixmap

class MainWindow(QWidget):
    def __init__(self):
       QWidget.__init__(self)
       self.setGeometry(100,100,1200,450)
       self.setFixedSize(600, 450)
       self.movie = QMovie("yeahboi1.gif")
       self.movie.frameChanged.connect(self.repaint)
       self.movie.start()
       self.setWindowTitle("Yeah Boi!")
      
    def defineLabels(self):
        self.lbl_Control = QLabel("Hello",self)
        self.lbl_Control.setGeometry(QtCore.QRect(480, 320, 400, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Control.setFont(font)
        self.lbl_Control.setStyleSheet("background-color: black;border: 1px solid black;")
        self.lbl_Control.setObjectName("lbl_Movement")
        self.lbl_Control.setText("<font color='white'><b>Controls</b></font>")
        
        self.lbl_Leap = QLabel("Hello",self)
        self.lbl_Leap.setGeometry(QtCore.QRect(480, 360, 400, 20))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Leap.setFont(font)
        self.lbl_Leap.setStyleSheet("background-color: black;border: 1px solid black;")
        self.lbl_Leap.setObjectName("lbl_Movement")
        self.lbl_Leap.setText("<font color='white'>Leap: </font>")
        
        self.lbl_Shoot = QLabel("Hello",self)
        self.lbl_Shoot.setGeometry(QtCore.QRect(480, 380, 400, 20))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Shoot.setFont(font)
        self.lbl_Shoot.setStyleSheet("background-color: black;border: 1px solid black;")
        self.lbl_Shoot.setObjectName("lbl_Movement")
        self.lbl_Shoot.setText("<font color='white'>Shoot: </font>")
        
        self.lbl_Uppercut = QLabel("Hello",self)
        self.lbl_Uppercut.setGeometry(QtCore.QRect(480, 400, 400, 20))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Uppercut.setFont(font)
        self.lbl_Uppercut.setStyleSheet("background-color: black;border: 1px solid black;")
        self.lbl_Uppercut.setObjectName("lbl_Movement")
        self.lbl_Uppercut.setText("<font color='white'>Uppercut: </font>")
        
        self.lbl_Dash = QLabel("Hello",self)
        self.lbl_Dash.setGeometry(QtCore.QRect(480, 420, 400, 20))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Dash.setFont(font)
        self.lbl_Dash.setStyleSheet("background-color: black;border: 1px solid black;")
        self.lbl_Dash.setObjectName("lbl_Movement")
        self.lbl_Dash.setText("<font color='white'>Dash: </font>")
    
    def platform(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('platform.jpg'))
        self.label.setGeometry(0,390,600,180)
        
    def leftWall(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Leftwall.png'))
        self.label.setGeometry(-20,-20,100,680)
        
    def rightWall(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Rightwall.png'))
        self.label.setGeometry(530,-20,80,680)
        
    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Mainwindow = MainWindow()
    
    Mainwindow.platform()
    Mainwindow.leftWall()
    Mainwindow.rightWall()
    Mainwindow.defineLabels()
    Mainwindow.show()
    sys.exit(app.exec_())
    