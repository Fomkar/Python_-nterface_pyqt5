# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:48:37 2022

@author: zeynep
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
import cv2
import os

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("veriseti2.ui",self)
        self.browse.clicked.connect(self.browsefiles)
        self.btn_save.clicked.connect(self.savefiles)
        self.btn_veri.clicked.connect(self.veri_seti_olustur)
    def browsefiles(self):
        # fname=QFileDialog.getOpenFileName(self, 'Open file', 'D:/',)
        fname = QFileDialog()
        self.currentDir = QFileDialog.getExistingDirectory(self, 'Select an awesome directory')
        self.currentDir = self.currentDir + "\\"
        # print( self.currentDir)
        self.filename.setText( self.currentDir)
        # return currentDir
    def savefiles(self):
        # fname=QFileDialog.getOpenFileName(self, 'Open file', 'D:/',)
        fname = QFileDialog()
        self.save_path = QFileDialog.getExistingDirectory(self, 'Select an awesome directory')
        self.save_path = self.save_path + "\\"
        print(self.save_path)
        self.filename_save.setText(self.save_path)
        # return save_path
    def veri_seti_olustur(self):
        # currentDir = self.currentDir
        # save_path =  MainWindow.savefiles(self)
        print(self.currentDir)
        files = os.chdir(self.currentDir)
        files = os.listdir() 
        a = 0
        for f in files:
            if f.endswith(".bmp"):
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
                k_bosluk = 10
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
        
app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(300)
widget.show()
sys.exit(app.exec_())



