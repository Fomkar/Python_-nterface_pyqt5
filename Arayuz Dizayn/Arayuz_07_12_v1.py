# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:01:00 2022

@author: zeynep
"""
# Gerekli kütüphaneler ekleniyor
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    ekran = QDialog()
    
    # Button 1in düzenlenmesi
    button1 =QPushButton(ekran)
    button1.setText("Başlat")
    button1.move(20, 20)
    button1.clicked.connect(button1_tiklandi)
    
    # Button 2in düzenlenmesi
    button2 =QPushButton(ekran)
    button2.setText("Durdur")
    button2.move(120, 20)
    button2.clicked.connect(button2_tiklandi)
    
    #Ekran Düzenlemesi
    ekran.setGeometry(100, 100, 200, 50)
    ekran.setWindowTitle("Veri seti oluşturma")
    ekran.show()
    sys.exit(app.exec_())
    
    
def button1_tiklandi():
    print("Birinci butona tikladik")

def button2_tiklandi():
    print("Durdur butonuna tikladik")
    
if __name__ == '__main__':
    window()
