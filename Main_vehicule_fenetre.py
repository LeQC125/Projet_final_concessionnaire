#######################################
###  IMPORTATIONS - Porté globale  ###
#######################################
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

import Main_vehicule


class FenetreMainVehicule(QtWidgets.QDialog, Main_vehicule.Ui_Dialog):
    def __init__(self,parent=None):
        super(Main_vehicule.Ui_Dialog).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Main véhicule")
