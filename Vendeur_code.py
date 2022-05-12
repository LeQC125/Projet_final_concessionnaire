####################################################################################
### 420-2G2-HU - Programmation Orienté objet
### Travail: Projet final concessionnaire
### Nom: Ludovic Boisclair
### No étudiant: 2126921
### No groupe: 01
### Description du fichier: Classe Vendeur
####################################################################################

#######################################
########  CRÉATION - CLASSE ###########
#######################################
class Vendeur:
    def __init__(self, pCodeVendeur=0, pNomVendeur="", pPrenomVendeur = ""):
        self.__code_vendeur = pCodeVendeur
        self.__nom_vendeur = pNomVendeur
        self.__prenom_vendeur = pPrenomVendeur

    #######################################
    ########  Mutateur/asceseur ###########
    #######################################
    def __get_code_vendeur(self):
        """
        Ascesseur de __code_vendeur
        """
        return self.__code_vendeur

    def __set_code_vendeur(self, pCodeVendeur):
        """
        Mutateur de __code_vendeur
        """
        if len(pCodeVendeur) == 6 and pCodeVendeur.isnumeric() is True:
            self.__code_vendeur = pCodeVendeur

    CodeVendeur = property(__get_code_vendeur, __set_code_vendeur)

    def __get_nom_vendeur(self):
        """
        Ascesseur de __nom_vendeur
        """
        return self.__nom_vendeur

    def __set_nom_vendeur(self, pNomVendeur):
        """
        Mutateur de __nom_vendeur
        """
        if len(pNomVendeur) <= 60 and pNomVendeur.isalpha() is True:
            self.__nom_vendeur = pNomVendeur

    NomVendeur = property(__get_nom_vendeur, __set_nom_vendeur)

    def __get_prenom_vendeur(self):
        """
        Ascesseur de __prenom_client
        """
        return self.__prenom_vendeur

    def __set_prenom_vendeur(self, pPrenomVendeur):
        """
        Mutateur de __prenom_vendeur
        """
        if len(pPrenomVendeur) <= 20 and pPrenomVendeur.isalpha() is True:
            self.__prenom_vendeur = pPrenomVendeur

    PrenomVendeur = property(__get_prenom_vendeur, __set_prenom_vendeur)

    #######################################
    ###### Méthode spéciale: __str__ ######
    #######################################
    def __str__(self):
        message = ""
        message += f"Voici le nom du vendeur: {self.__nom_vendeur} {self.__prenom_vendeur}\n"
        message += f"Voici le code du vendeur: {self.__code_vendeur}\n"
        return message
