####################################################################################
### 420-2G2-HU - Programmation Orienté objet
### Travail: Projet final concessionnaire
### Nom: Ludovic Boisclair
### No étudiant: 2126921
### No groupe: 01
### Description du fichier: Classe Vehicule
####################################################################################
from Contract_vente import *


#######################################
########  CRÉATION - CLASSE ###########
#######################################
class Vehicule:
    def __init__(self, pNumeroSerie=0, pAnnee=0, pMarque="", pSousModel="", pKilometrage=0, pImmatriculation="",
                 pTypeVehicule="", pCouleur="", pVente=Contract_vente()):
        self.__numero_serie = pNumeroSerie
        self.__annee = pAnnee
        self.__marque = pMarque
        self.__sous_model = pSousModel
        self.__kilometrage = pKilometrage
        self.__immatriculation = pImmatriculation
        self.Type_vehicule = pTypeVehicule
        self.Couleur = pCouleur
        self.ContractVente = pVente

    #######################################
    ########  Mutateur/asceseur ###########
    #######################################
    def __get_numero_serie(self):
        """
        Ascesseur de __numero_serie
        """
        return self.__numero_serie

    def __set_numero_serie(self, pNumeroSerie):
        """
        Mutateur de __numero_serie
        """
        if len(pNumeroSerie) <= 12:
            self.__numero_serie = pNumeroSerie

    NumeroSerie = property(__get_numero_serie, __set_numero_serie)

    def __get_annee(self):
        """
        ascesseur de __annee
        """
        return self.__annee

    def __set_annee(self, pAnnee):
        """
        Mutateur de __annee
        """
        if len(pAnnee) == 4:
            self.__annee = pAnnee

    Annee = property(__get_annee, __set_annee)

    def __get_marque(self):
        """
        ascesseur de __marque
        """
        return self.__marque

    def __set_marque(self, pMarque):
        """
        Mutateur de __marque
        """
        if pMarque.isalpha() is True and len(pMarque) <= 50:
            self.__marque = pMarque

    Marque = property(__get_marque, __set_marque)

    def __get_sous_model(self):
        """
        ascesseur de __sous_model
        """
        return self.__sous_model

    def __set_sous_model(self, pSousModel):
        """
        Mutateur de __sous_model
        """
        if pSousModel.isalpha() is True and len(pSousModel) <= 50:
            self.__sous_model = pSousModel

    SousModel = property(__get_sous_model, __set_sous_model)

    def __get_kilometrage(self):
        """
        Ascesseur de __kilometrage
        """
        return self.__kilometrage

    def __set_kilometrage(self, pKilometrage):
        """
        Mutateur de __kilometrage
        """
        if pKilometrage.isnumeric() is True:
            self.__kilometrage = pKilometrage

    Kilometrage = property(__get_kilometrage, __set_kilometrage)

    def __get_immatriculation(self):
        """
        Ascesseur de __immatriculation
        """
        return self.__immatriculation

    def __set_immatriculation(self, pImmatriculation):
        """
        Mutateur de __immatriculation
        """
        for carac in pImmatriculation:
            if len(pImmatriculation) == 6 and carac[0].isalpha() and carac[1].isnumeric() and carac[2].isalpha() \
                    and carac[3].isnumeric() and carac[4].isalpha() and carac[5].isnumeric():
                self.__immatriculation = pImmatriculation

    Immatriculation = property(__get_immatriculation, __set_immatriculation)

    #######################################
    ###### Méthode spéciale: __str__ ######
    #######################################
    def __str__(self):
        message = ""
        message += f"Voici le numero de serie du véhicule: {self.__numero_serie}\n"
        message += f"Voici l'année du véhicule: {self.__annee}\n"
        message += f"Voici la marque du véhicule: {self.__marque}\n"
        message += f"Voici le sous model du véhicule: {self.__sous_model}\n"
        message += f"Voici le kilometrage du véhicule: {self.__kilometrage}\n"
        message += f"Voici l'immatriculation du véhicule: {self.__immatriculation}\n"
        return message
