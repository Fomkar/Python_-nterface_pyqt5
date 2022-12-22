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
import os
    

class myApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_browse_files_current.clicked.connect(self.browsefiles) # Ana görüntü olan kısım
        self.ui.btn_savepath.clicked.connect(self.savefiles) # Veri setini kaydedilecek buton
        self.ui.btn_imaget.clicked.connect(self.getimages)  # Görüntü Alma Butonu
        self.ui.btn_create_dataset.clicked.connect(self.veriseti_olustur) # Veri seti oluşturma Butonu 
        self.ui.btn_stop_camera.clicked.connect(self.stop_kamera) # Kamerayı durdurma kodu
        self.ui.btn_create_dataset.clicked.connect(self.islem) # Veri seti oluştur Butonu
        self.ui.btn_imaget.clicked.connect(self.islem) # Görüntü Alma butonun Sonucu
        self.ui.btn_motor.clicked.connect(self.islem) #Vibrasyon motoru Calıstırma
        self.ui.btn_stop_camera.clicked.connect(self.islem)        

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
        elif (sender == 'Kamerayı Durdur'):
            text = "Sonuç: Kamera Durdu"
            
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
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateDevice(self.info))
            self.camera.Open()
    
        # # Grabing Continusely (video) with minimal delay
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
        self.camera.AcquisitionFrameRateAbs.SetValue(True)
        # # camera.AcquisitionFrameRateEnable.SetValue = True
        self.camera.AcquisitionFrameRateAbs.SetValue(30.0)
        # camera.AcquisitionFrameRateAbs.SetValue = 5.0
        # camera.Width.SetValue(720)
        # camera.Height.SetValue = 540.0
        # camera.Width.SetValue = 720.0
        # camera.Width = 720
        converter = pylon.ImageFormatConverter()
        
        # converting to opencv bgr format
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        
        
        self.images = np.zeros((1000, 1080, 1440, 3), dtype=int)
        # images = np.zeros((100, 540, 720, 3), dtype=int)
        
        self.counter = 0
        while self.camera.IsGrabbing():
            grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
    
    
    
            if grabResult.GrabSucceeded():
                    # Access the image data
                self.image = converter.Convert(grabResult)
                self.img = self.image.GetArray()
        # Get grabbed image
        
                if self.counter < 50: # Kaçtane frame alınacaksa ( Number of Frames)
                    self.images[self.counter] = self.img
                    
                else:
                    break
        
                self.counter += 1
                self.img =cv2.flip(self.img, 1)
                cv2.imwrite(self.currentDir +"images"+ str(self.counter) + '.jpg', self.img)
                cv2.namedWindow('title', cv2.WINDOW_NORMAL)
                cv2.imshow('title', self.img)
        
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            grabResult.Release()
    
        # Releasing the resource    
        self.camera.StopGrabbing()
        # camera.Release()
        self.camera.Close()
        cv2.destroyAllWindows()
    def veriseti_olustur(self):
        # currentDir = self.currentDir
        # save_path =  MainWindow.savefiles(self)
        print(self.currentDir)
        files = os.chdir(self.currentDir)
        files = os.listdir() 
        a = 0
        for f in files:
            if f.endswith(".jpg"):
                print(f)
# app=QApplication(sys.argv)
# mainwindow=MainWindow()
# widget=QtWidgets.QStackedWidget()
# widget.addWidget(mainwindow)
# widget.setFixedWidth(400)
# widget.setFixedHeight(300)
# widget.show()
# sys.exit(app.exec_())

                # x = f.split("_")
                # # print(x[7])
                # y  = x[7].split(".")
                # # print(y)
                # # print(y[0])
                # a = int(y[0])
                # print(a)
                a +=1
                image = cv2.imread(f,1)
                # if image.shape[3] == 3:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                #orijinal görüntü
                # cv2.namedWindow('Original image',cv2.WINDOW_NORMAL)
                # cv2.imshow('Original image',image)
                # cv2.namedWindow('Gray image',cv2.WINDOW_NORMAL)
                # cv2.imshow('Gray image',gray)
                _,trehsold = cv2.threshold(gray, 55, 255, cv2.THRESH_BINARY)
                # cv2.imwrite('treshold.jpg', trehsold)
                dilate = cv2.dilate(trehsold, (5,5),iterations = 15)
                # cv2.namedWindow('Thresh image',cv2.WINDOW_NORMAL)
                # cv2.imshow('Thresh image',trehsold)
                # cv2.namedWindow('Dilate image',cv2.WINDOW_NORMAL)
                # cv2.imshow('Dilate image',dilate)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
        
                # if a == 1:
                #     break
        
                contours, hierarchy = cv2.findContours(dilate,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2:]
        #       cnt = contours[0]
                k_bosluk = 20
                idx =0 
                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    x,y,w,h = cv2.boundingRect(cnt)
                    print(area)
                    # print("X0 : " ,x, "Y0 : ",y,"\nX1: ",x+w," Y1 : ",y+h)
                    if(area >10000 and (y+h) != image.shape[0] and y > 10 and x > 0):
                        idx += 1
                        print("X0 : " ,x, "Y0 : ",y,"\nX1: ",x+w," Y1 : ",y+h)
                        
                        roi=image[y-k_bosluk:y+h+k_bosluk,x-k_bosluk:x+w+k_bosluk]
                        cv2.imwrite(self.save_path + str(a) + str(idx) + '.jpg', roi)
                        
                    elif(y<30 or (y + h) ==1024):
                            roi=image[y:y+h + 20,x-k_bosluk:x+w+k_bosluk]
                            print("yukarı ya veya aşağı değdi")
                            #cv2.imshow('img crop'+str(a)+str(idx),roi)
                            #cv2.rectangle(image,(x,y),(x+w,y+h),(255,250,255),1)
                            # cv2.imwrite('Kesik_elma/elma_kesik' + "_"+ str(idx)+".jpg", roi)
                          
                            #cv2.imshow('img bounding',image)
                    else:
                        print("Kenara Değmedi"+str(idx))
                            
            
        cv2.waitKey(0)  
        cv2.destroyAllWindows()
    def stop_kamera(self):
        self.camera.StopGrabbing()
        self.camera.Release()
        self.camera.Close()
        print("Kmaera Durdu")
        cv2.destroyAllWindows()
                   
        
def app():        
    App = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(App.exec_())
app()       
