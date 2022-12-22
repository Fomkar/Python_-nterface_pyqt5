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
        self.ui.btn_browse_files_current.clicked.connect(self.browsefiles)
        self.ui.btn_savepath
        self.ui.btn_create_dataset.clicked.connect(self.islem)
        self.ui.btn_imaget.clicked.connect(self.islem)
        self.ui.btn_motor.clicked.connect(self.islem)
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
def app():        
    App = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(App.exec_())
app()       
