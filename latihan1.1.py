#QtGui QTCore QtWidgets
# ====================== cara 1=====================

from PyQt5 import QtGui, QtCore, QtWidgets

app = QtWidgets.QApplication([])
window = QtWidgets.QPushButton("MyButton")
window.show()
app.exec_()

#=================== cara 2 ========================
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication([])
window = QPushButton("MyButton2")
window.show()
app.exec_()

#================== cara 3 =========================
from PyQt5 import QtWidgets as qtw

app = qtw.QApplication([])
window = qtw.QPushButton("MyButton3")
window.show()
app.exec_()

#================== cara 4 ========================
from PyQt5.QtWidgets import QApplication, QPushButton

app = QApplication([])
window = QPushButton("Mybutton4")
window.show()
app.exec_()