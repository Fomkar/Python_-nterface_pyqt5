# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:33:01 2022

@author: fomkar
"""

from PyQt5 import QtWidgets
import sys
from Dialog import Ui_Dialog

class myApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_browse_files_current.clicked.connect(self.browsefiles) # Ana görüntü olan kısım
        self.ui.btn_savepath.clicked.connect(self.savefiles) # Veri setini kaydedilecek buton
        self.ui.btn_create_dataset.clicked.connect(self.islem) # Veri seti oluştur Butonu
        self.ui.btn_imaget.clicked.connect(self.islem) # Görüntü Alma butonu
        self.ui.btn_motor.clicked.connect(self.islem) #Vibrasyon motoru Calıstırma
        # self.ui.btn_motor.clicked.connect(self.islem2)
    def islem(self):
        sender = self.sender().text()
        # print(sender)
        text = ""
        if (sender == 'Veri Seti Oluştur'):
            text = "Sonuç: Veri Seti Kaydedildi"
        elif (sender == 'Görüntü Al'):
            text = "Sonuç: Görüntüler alındı"
        elif (sender == 'Vibrasyon Çalıştır'):
            text = "Sonuç: Motor Çalıştı"
            
        self.ui.snc_label.setText(text)
    def browsefiles(self):
        sender = self.sender().text()
        print(sender)
        # fname=QFileDialog.getOpenFileName(self, 'Open file', 'D:/',)
        self.fname = QtWidgets.QFileDialog()
        self.currentDir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select an awesome directory')
        self.currentDir = self.currentDir + "\\"
        # print( self.currentDir)
        self.ui.lineEdit_ana_images.setText( self.currentDir)
        # return currentDir
    def savefiles(self):
        # fname=QFileDialog.getOpenFileName(self, 'Open file', 'D:/',)
        self.fname = QtWidgets.QFileDialog()
        self.save_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select an awesome directory')
        self.save_path = self.save_path + "\\"
        print(self.save_path)
        self.ui.lineEdit_savepath.setText(self.save_path)
        # return save_path
    def getimages():
        
def app():        
    App = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(App.exec_())
app()       
