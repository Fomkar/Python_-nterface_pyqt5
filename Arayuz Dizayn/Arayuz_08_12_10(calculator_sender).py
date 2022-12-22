# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:43:33 2022

@author: zeynep
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 14:30:32 2022

@author: zeynep
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        
        self.setWindowTitle('Hesap Makinesi')
        self.setGeometry(200, 200, 500, 500)
        self.initUI()
        
    def initUI(self):
        
        #Label1 'in düzenlenmesi
        self.lbl_sayi1=QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Sayı 1: ')
        self.lbl_sayi1.move(50, 30)
        
        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200, 32)
        
        #Label2'in düzenlenmesi
        self.lbl_sayi2=QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('Sayı 2: ')
        self.lbl_sayi2.move(50, 80)
        
        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200, 32)
        
        #button düzenlenmesi
        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('Topla')
        self.btn_topla.move(150, 130)
        self.btn_topla.clicked.connect(self.hesapla)
        
        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText('Çarp')
        self.btn_carp.move(150, 170)
        self.btn_carp.clicked.connect(self.hesapla)
        
        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText('Böl')
        self.btn_bol.move(150, 210)
        self.btn_bol.clicked.connect(self.hesapla)
        
        self.btn_cıkar = QtWidgets.QPushButton(self)
        self.btn_cıkar.setText('Çıkar')
        self.btn_cıkar.move(150, 250)
        self.btn_cıkar.clicked.connect(self.hesapla)
        
        self.lbl_sonuc=QtWidgets.QLabel(self)
        self.lbl_sonuc.setText('Sonuç: ')
        self.lbl_sonuc.move(150, 290)
        
    def hesapla(self):
        sender = self.sender()
        print(sender.text())
        if sender.text() == 'Topla':
            
            result =int(self.txt_sayi1.text()) + int(self.txt_sayi2.text()) 
            self.lbl_sonuc.setText('Sonuç: '+ str(result))
        elif sender.text() == 'Çarp':
            result =int(self.txt_sayi1.text()) * int(self.txt_sayi2.text()) 
            self.lbl_sonuc.setText('Sonuç: '+ str(result))
        elif sender.text() == 'Böl':
        
            result =int(self.txt_sayi1.text()) / int(self.txt_sayi2.text()) 
            self.lbl_sonuc.setText('Sonuç: '+ str(result)) 
        elif sender.text() == 'Çıkar':
            result =int(self.txt_sayi1.text()) - int(self.txt_sayi2.text()) 
            self.lbl_sonuc.setText('Sonuç: '+ str(result))  
def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
app()
        
        
        
        
        
        
        
        