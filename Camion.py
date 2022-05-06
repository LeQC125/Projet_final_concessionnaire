####################################################################################
### 420-2G2-HU - Programmation Orienté objet
### Travail: Projet final concessionnaire
### Nom: Ludovic Boisclair
### No étudiant: 2126921
### No groupe: 01
### Description du fichier: Classe Camion
####################################################################################

#######################################
###  IMPORTATIONS - Porté globale  ###
#######################################
from Vehicule import *


#######################################
########  CRÉATION - CLASSE ###########
#######################################
class Camion(Vehicule):
    def __init__(self, pNbrPortes=0, pLongueurBoite=0):
        super().__init__()
        self.__longueur_boite = pLongueurBoite
        self.Nbr_portes = pNbrPortes

    #######################################
    ########  Mutateur/asceseur ###########
    #######################################
    def __get_longueur_boite(self):
        """
        Ascesseur de __longueur_boite
        """
        return self.__longueur_boite

    def __set_longueur_boite(self, pLongueurBoite):
        """
        Mutateur de __longueur_boite
        """
        if pLongueurBoite.isnumeric() is True:
            self.__longueur_boite = pLongueurBoite

    LongueurBoite = property(__get_longueur_boite, __set_longueur_boite)

    #######################################
    ###### Méthode spéciale: __str__ ######
    #######################################
    def __str__(self):
        message = ""
        message += f"Voici la longueur de la boite du camion: {self.__longueur_boite}\n"
        message += f"Voici le nombre de porte: {self.Nbr_portes}\n"
        message += f"Voicie l'immatriculation du camion: {self.Immatriculation}\n"
        return message
