class Voiture:
    def __init__(self, marque, modèle, annee,kilometrage) -> None:
        self.__marque = marque
        self.__modele = modèle
        self.__annee =annee
        self.__kilometrage = kilometrage
        self.en_marche = False
        self.__reservoir = 3


    def getmarque(self):
        return self.__marque
    
    def getmodele(self):
        return self.__modele
    
    def getannee(self):
        return self.__annee
    
    def getkilometrage(self):
        return self.__kilometrage



    def demarrer(self):
        self.en_marche = not self.en_marche
        print(self.en_marche)
        if self.__verifier_plein() > 5:
            print("La voiture démarre . . .")
            print("L'essence est de {} Litres".format(self.__verifier_plein()) )
        else :
            print("La voiture ne peut pas démarrer . . . ")
            print("Le véhicule ne possède que {} Litres d'essence".format(self.__reservoir))
            print("L'essence requis pour démarrer le véhicule est d'au minimum 5 Litres")
    
    def arreter(self):
        self.en_marche = not self.en_marche
        print(self.en_marche)
        print("La voiture s'arrête . . . ")


    def __verifier_plein(self):
        return self.__reservoir


Voi = Voiture("gh","er","1001",12)
Voi.demarrer()
Voi.arreter()