# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(756, 589)
        self.btn_imaget = QtWidgets.QPushButton(Dialog)
        self.btn_imaget.setGeometry(QtCore.QRect(50, 280, 141, 41))
        self.btn_imaget.setObjectName("btn_imaget")
        self.btn_motor = QtWidgets.QPushButton(Dialog)
        self.btn_motor.setGeometry(QtCore.QRect(240, 280, 141, 41))
        self.btn_motor.setObjectName("btn_motor")
        self.btn_create_dataset = QtWidgets.QPushButton(Dialog)
        self.btn_create_dataset.setGeometry(QtCore.QRect(430, 280, 141, 41))
        self.btn_create_dataset.setObjectName("btn_create_dataset")
        self.snc_label = QtWidgets.QLabel(Dialog)
        self.snc_label.setGeometry(QtCore.QRect(60, 360, 321, 31))
        self.snc_label.setObjectName("snc_label")
        self.btn_browse_files_current = QtWidgets.QPushButton(Dialog)
        self.btn_browse_files_current.setGeometry(QtCore.QRect(50, 120, 141, 41))
        self.btn_browse_files_current.setObjectName("btn_browse_files_current")
        self.btn_savepath = QtWidgets.QPushButton(Dialog)
        self.btn_savepath.setGeometry(QtCore.QRect(50, 190, 141, 41))
        self.btn_savepath.setObjectName("btn_savepath")
        self.lineEdit_ana_images = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ana_images.setGeometry(QtCore.QRect(230, 120, 341, 31))
        self.lineEdit_ana_images.setObjectName("lineEdit_ana_images")
        self.lineEdit_savepath = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_savepath.setGeometry(QtCore.QRect(230, 190, 341, 31))
        self.lineEdit_savepath.setObjectName("lineEdit_savepath")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Veri seti Oluştur"))
        self.btn_imaget.setText(_translate("Dialog", "Görüntü Al"))
        self.btn_motor.setText(_translate("Dialog", "Vibrasyon Çalıştır"))
        self.btn_create_dataset.setText(_translate("Dialog", "Veri Seti Oluştur"))
        self.snc_label.setText(_translate("Dialog", "Sonuç : "))
        self.btn_browse_files_current.setText(_translate("Dialog", "Klasör Seç"))
        self.btn_savepath.setText(_translate("Dialog", "Veri Seti Klasörü Seç"))

