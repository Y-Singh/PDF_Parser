import sys, os, qdarkstyle
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtGui import *

class Parser(QtWidgets.QMainWindow):

    def __init__(self, path=None):





def main ():
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QtWidgets.QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    application = 