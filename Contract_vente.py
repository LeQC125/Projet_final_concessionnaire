####################################################################################
### 420-2G2-HU - Programmation Orienté objet
### Travail: Projet final concessionnaire
### Nom: Ludovic Boisclair
### No étudiant: 2126921
### No groupe: 01
### Description du fichier: Classe Contract_vente
####################################################################################

#######################################
###  IMPORTATIONS - Porté globale  ###
#######################################
from Vendeur import *
from Client import *

#######################################
########  CRÉATION - CLASSE ###########
#######################################
class Contract_vente:
    def __init__(self, pListVehicule=[], pCodeVente=0, pPrixVente=0, pFinancement="", pVendeur = Vendeur(), pClient = Client()):
        self.list_vehicule = pListVehicule
        self.__code_vente = pCodeVente
        self.__prix_vente = pPrixVente
        self.Financement = pFinancement
        self.Vendeur = pVendeur
        self.Client = pClient

    #######################################
    ########  Mutateur/asceseur ###########
    #######################################
    def __get_code_vente(self):
        """
        Ascesseur de __code_vente
        """
        return self.__code_vente

    def __set_code_vente(self, pCodeVente):
        """
        Mutateur de __code_vente
        """
        if len(pCodeVente) == 6 and pCodeVente.isnumeric() is True:
            self.__code_vente = pCodeVente

    CodeVente = property(__get_code_vente, __set_code_vente)

    def __get_prix_vente(self):
        """
        Ascesseur de __prix_vente
        """
        return self.__prix_vente

    def __set_prix_vente(self, pPrixVente):
        """
        Mutateur de __prix_vente
        """
        if len(pPrixVente) <= 50 and pPrixVente.isnumeric() is True:
            self.__prix_vente = pPrixVente

    PrixVente = property(__get_prix_vente, __set_prix_vente)

    #######################################
    ###### Méthode spéciale: __str__ ######
    #######################################
    def __str__(self):
        message = ""
        message += f"Voici le code de vente: {self.__code_vente}\n"
        message += f"Voici le prix de la vente: {self.__prix_vente}\n"
        message += f"Voici le financement: {self.Financement}\n"
        message += f"Voici la liste de vécule: {self.list_vehicule}\n"
        message += f"{self.Vendeur}\n"
        message += f"{self.Client}\n"
        return message
