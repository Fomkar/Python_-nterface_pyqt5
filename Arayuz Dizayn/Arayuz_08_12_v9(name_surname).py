# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:43:20 2022

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
    
    #label1 düzenleme
    lbl_name =QtWidgets.QLabel(win)
    lbl_name.setText('Adınız :')
    lbl_name.move(50, 30)
    
    #label2 düzenleme
    lbl_name =QtWidgets.QLabel(win)
    lbl_name.setText('SoyAdınız :')
    lbl_name.move(50, 70)
    

        
    txt_name =QtWidgets.QLineEdit(win)
    txt_name.move(150, 30)
    
    
    sur_name=QtWidgets.QLineEdit(win)
    sur_name.move(150,70)
    
    def tiklandi(self):
        print('Butona Tıklandı')
        print('butona',txt_name.text(),' ',sur_name.text(),' bastı')
    #button ayarlaması
    btn_save =QtWidgets.QPushButton(win)
    btn_save.setText('Kaydet')
    btn_save.move(150, 110)
    btn_save.clicked.connect(tiklandi)
    
    
    
    win.show()
    sys.exit(app.exec_())

window()

# QLabel
# QComboBox
# QCheckBox
# QRadioButton
# QPushButton
# QTableWidget
# QLineEdit
# QSlider
# QProgressBar