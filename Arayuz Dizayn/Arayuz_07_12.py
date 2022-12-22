# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:58:31 2022

@author: zeynep
"""
# Boş pencere oluşturma
from PyQt5.QtWidgets import *
import sys

uygulama =QApplication(sys.argv)

pencere = QWidget()
pencere.show()

uygulama.exec_()
