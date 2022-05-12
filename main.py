####################################################################################
### 420-2G2-HU - Programmation Orienté objet
### Travail: Projet final concessionnaire
### Nom: Ludovic Boisclair
### No étudiant: 2126921
### No groupe: 01
### Description du fichier: Classe Main
####################################################################################

#######################################
###  IMPORTATIONS - Porté globale  ###
#######################################
from Camion import *
from Auto import *
from Contract_vente import *
# importation module pour l'interface graphique
import sys
from pyqt5.QtGui import QStandardItemModel, QStandardItem
import


##########################################################
###  DéCLARATIONS ET INITIALISATIONS - Porté globale  ####
##########################################################

#######################################
###### DéFINITIONS DES FONCTIONS ######
#######################################


#################################
###### PROGRAMME PRINCIPAL ######
#################################

#################################
######## Programme test #########
#################################
Vehicule1 = Vehicule("123456789123", 2018, "Subaru", "Sti", 76800, "J8M 5R2", "Auto", "Noir")
Auto1 = Auto(5, "Manuel", "Sedan")
Camion1 = Camion(4, "6 pied")
Contract_vente1 = Contract_vente(["Subaru","Brz","2015"], 154689, 20000, "3 mois")
Vendeur1 = Vendeur(123456, "Boisclair", "Ludovic")
Client1 = Client(123456, "Ludovic", "Boisclair")

print(f"{Vehicule1.__str__()}\n {Auto1.__str__()}\n {Camion1.__str__()}\n {Contract_vente1.__str__()}\n"
      f"{Client1.__str__()}\n {Vendeur1.__str__()}\n")
