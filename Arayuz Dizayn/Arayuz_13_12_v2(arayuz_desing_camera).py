# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:33:01 2022

@author: fomkar
"""
# importing libraries
from pypylon import pylon
import cv2
import numpy as np
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
        # self.ui.btn_imaget.clicked.connect(self.getimages)
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
    def getimages(self):
        self.serial_number = '40038474'
        self.info = None
        for i in pylon.TlFactory.GetInstance().EnumerateDevices():
            if i.GetSerialNumber() == self.serial_number:
                self.info = i
                break
        else:
            print('Camera with {} serial number not found'.format(self.serial_number))
        
        # VERY IMPORTANT STEP! To use Basler PyPylon OpenCV viewer you have to call .Open() method on you camera
        if self.info is not None:
            self.camera = self.pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateDevice(self.info))
            self.camera.Open()
    
        # # Grabing Continusely (video) with minimal delay
        # self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
        # self.camera.AcquisitionFrameRateAbs.SetValue(True)
        # # camera.AcquisitionFrameRateEnable.SetValue = True
        # self.camera.AcquisitionFrameRateAbs.SetValue(30.0)
        # camera.AcquisitionFrameRateAbs.SetValue = 5.0
        # camera.Width.SetValue(720)
        # camera.Height.SetValue = 540.0
        # camera.Width.SetValue = 720.0
        # camera.Width = 720
        converter = pylon.ImageFormatConverter()
        
        # converting to opencv bgr format
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        
        
        images = np.zeros((1000, 1080, 1440, 3), dtype=int)
        # images = np.zeros((100, 540, 720, 3), dtype=int)
        
        counter = 0
        while self.camera.IsGrabbing():
            grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
    
    
    
            if grabResult.GrabSucceeded():
                    # Access the image data
                image = converter.Convert(grabResult)
                img = image.GetArray()
        # Get grabbed image
        
                if counter < 1000:
                    images[counter] = img
                    cv2.imwrite(self.save_path + str(counter) + '.jpg', img)
                else:
                    break
        
                counter += 1
        
        # if counter <= 100:
        #     cv2.imwrite('C:/Users/Hasan/Desktop/test/Spyder/temp_' + str(counter) + '.jpg', img)
            cv2.namedWindow('title', cv2.WINDOW_NORMAL)
            cv2.imshow('title', img)
        
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        grabResult.Release()
    
        # Releasing the resource    
        self.camera.StopGrabbing()
        # camera.Release()
        self.camera.Close()
        cv2.destroyAllWindows()
        
def app():        
    App = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(App.exec_())
app()       
