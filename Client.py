####################################################################################
### 420-2G2-HU - Programmation Orienté objet
### Travail: Projet final concessionnaire
### Nom: Ludovic Boisclair
### No étudiant: 2126921
### No groupe: 01
### Description du fichier: Classe Client
####################################################################################

#######################################
########  CRÉATION - CLASSE ###########
#######################################
class Client:
    def __init__(self, pCodeClient = 0, pNomClient = "", pPrenomClient = ""):
        self.__code_client = pCodeClient
        self.__nom_client = pNomClient
        self.__prenom_client = pPrenomClient

    #######################################
    ########  Mutateur/asceseur ###########
    #######################################
    def __get_code_client(self):
        """
        Ascesseur de __code_client
        """
        return self.__code_client

    def __set_code_client(self, pCodeClient):
        """
        Mutateur de __code_client
        """
        if len(pCodeClient) == 6 and pCodeClient.isnumeric is True:
            self.__code_client = pCodeClient

    CodeClient = property(__get_code_client, __set_code_client)

    def __get_nom_client(self):
        """
        Ascesseur de __nom_client
        """
        return self.__nom_client

    def __set_nom_client(self,pNomClient):
        """
        Mutateur de __nom_client
        """
        if len(pNomClient) <= 60 and pNomClient.isalpha() is True:
            self.__nom_client = pNomClient

    NomClient = property(__get_nom_client, __set_nom_client)

    def __get_prenom_client(self):
        """
        Ascesseur de __prenom_client
        """
        return self.__prenom_client

    def __set_prenom_client(self,pPrenomClient):
        """
        Mutateur de __prenom_client
        """
        if len(pPrenomClient) <= 20 and pPrenomClient.isalpha() is True:
            self.__prenom_client = pPrenomClient

    PrenomClient = property(__get_prenom_client, __set_prenom_client)

    #######################################
    ###### Méthode spéciale: __str__ ######
    #######################################
    def __str__(self):
        message = ""
        message += f"Voici le nom du client:{self.__nom_client} {self.__prenom_client}\n"
        message += f"Voici le code client: {self.__code_client}\n"
        return message
