####################################################################################
### 420-2G2-HU - Programmation Orienté objet
### Travail: Projet final concessionnaire
### Nom: Ludovic Boisclair
### No étudiant: 2126921
### No groupe: 01
### Description du fichier: Classe Auto
####################################################################################

#######################################
###  IMPORTATIONS - Porté globale  ###
#######################################
from Vehicule import *

#######################################
########  CRÉATION - CLASSE ###########
#######################################
class Auto(Vehicule):
    def __init__(self, pNbrPlaces=0, pTransmission="", pTypeCarosserie=""):
        super().__init__()
        self.__nbr_places = pNbrPlaces
        self.Tranmission = pTransmission
        self.Type_carosserie = pTypeCarosserie

    #######################################
    ########  Mutateur/asceseur ###########
    #######################################
    def __get_nbr_places(self):
        """
        Ascesseur de __nbr_places
        """
        return self.__nbr_places

    def __set_nbr_places(self, pNbrPlaces):
        if len(pNbrPlaces) == 1 and pNbrPlaces.isnumeric() is True:
            self.__nbr_places = pNbrPlaces

    NbrPlaces = property(__get_nbr_places, __set_nbr_places)

    #######################################
    ###### Méthode spéciale: __str__ ######
    #######################################
    def __str__(self):
        message = ""
        message += f"Voici le nombre de places de l'auto: {self.__nbr_places}\n"
        message += f"Voici le type de tansmission: {self.Tranmission}\n"
        message += f"Voici le type de carosserie: {self.Type_carosserie}\n"
        message += f"Voice l'immatriculation de l'auto: {Vehicule.Immatriculation}\n"
        return message
