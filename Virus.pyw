
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QLabel, QVBoxLayout, QFrame, QPushButton
from random import randint
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QRect
import sys
from functools import partial

class Window(QWidget):
    def __init__(self):
        super().__init__()
        global numofWin 
        numofWin = numofWin + 1
        print(numofWin)

        self.avalHeight = QDesktopWidget().availableGeometry().height()
        self.avalWidth = QDesktopWidget().availableGeometry().width()

        self.height = 200
        self.width = 500

        self.left = randint(100, self.avalWidth - self.width)
        self.top = randint(100, self.avalHeight - self.height)
        print("left: {}\t top: {}".format(self.left, self.top))

        self.windowTitle = 'Hail Hydra!!'
        self.hydraLogoImg = './hydra.png'
        

        self.setWindowTitle(self.windowTitle)
        self.setWindowIcon(QIcon(self.hydraLogoImg))

        self.move(self.left, self.top)
        self.setFixedSize( self.width, self.height)

        self.mainFrame = QFrame(self)
        self.mainFrame.setGeometry(QRect(10, 10, 480, 180))
        font = QFont()
        font.setFamily("Unica One")
        font.setPointSize(11)
        self.mainFrame.setFont(font)
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")

        self.hydraLogo = QLabel(self.mainFrame)
        self.hydraLogo.setGeometry(QRect(190, 10, 100, 100))
        self.hydraLogo.setText("")
        self.hydraLogo.setPixmap(QPixmap(self.hydraLogoImg))
        self.hydraLogo.setScaledContents(True)
        self.hydraLogo.setObjectName("hydraLogo")

        self.punchLine = QLabel(self.mainFrame)
        self.punchLine.setGeometry(QRect(10, 140, 461, 31))
        self.punchLine.setAlignment(Qt.AlignCenter)
        self.punchLine.setWordWrap(True)
        self.punchLine.setText("We shall never be destroyed! Cut off a limb and two more shall take its place!")

        self.slogan = QLabel(self.mainFrame)
        self.slogan.setGeometry(QRect(20, 110, 451, 31))
        self.slogan.setAlignment(Qt.AlignCenter)
        self.slogan.setWordWrap(True)
        self.slogan.setText("Hail, Hydra! Immortal Hydra!")

        self.closeBtn = QPushButton(self.mainFrame)
        self.closeBtn.setGeometry(QRect(410, 0, 70, 30))
        self.closeBtn.setText("Close")
        self.closeBtn.clicked.connect(partial(self.closed, self))

        #--------------------------------------------ADDITIONAL CODE-----------------------------------------------#
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        #self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint , False)

        self.show()

    def closed(self, currentWin):
        self._ = Window()
        self._1 = Window()
        currentWin.close()
#----------------------------------------------------------IF DON'T WANT TO CLOSE WINDOWS------------------------------------------#
#    def closeEvent(self, event):
#        event.ignore()

numofWin = 1

def main(App):
    App.setStyle('fusion')
    for __ in range(numofWin):
        _ = Window()
    closed = App.exec()
    if closed == 0:
        main(App)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    main(App)