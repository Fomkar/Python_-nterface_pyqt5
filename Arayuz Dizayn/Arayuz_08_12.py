# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:51:12 2022

@author: zeynep
"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    
    win.setWindowTitle("Veri Seti Oluşturma") # Başlık belirliyor
    win.setGeometry(1100, 100, 500, 500) # İL İKİ parametre pencerenin ekrandaki konumu
    win.setWindowIcon(QIcon('icon.png'))
    win.show()
    sys.exit(app.exec_())

window()