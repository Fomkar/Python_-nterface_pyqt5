# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:04:52 2022

@author: zeynep
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()           
            
        self.setWindowTitle('First Program')
        self.setGeometry(1100, 100, 500, 500) # İL İKİ parametre pencerenin ekrandaki konumu
        self.setWindowIcon(QIcon('icon.png'))
        self.initUI()
    def initUI(self):
            #label1 düzenleme
        self.lbl_name =QtWidgets.QLabel(self)
        self.lbl_name.setText('Adınız :')
        self.lbl_name.move(50, 30)
    
        #label2 düzenleme
        self.lbl_name =QtWidgets.QLabel(self)
        self.lbl_name.setText('SoyAdınız :')
        self.lbl_name.move(50, 70)
    
        self.txt_name =QtWidgets.QLineEdit(self)
        self.txt_name.move(150, 30)
    
    
        self.sur_name=QtWidgets.QLineEdit(self)
        self.sur_name.move(150,70)
        
        self.btn_save =QtWidgets.QPushButton(self)
        self.btn_save.setText('Kaydet')
        self.btn_save.move(150, 110)
        self.btn_save.clicked.connect(self.tiklandi)
    def tiklandi(self):
        print('Butona Tıklandı')
        print('butona',self.txt_name.text(),' ',self.sur_name.text(),' bastı')
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
window()
