class Rectangle :
    def __init__(self, longueur, largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur
        print("Longueur = {}cm    Largeur = {}cm".format(self.__longueur , self.__largeur))
    def getlongueur(self):
        return self.__longueur
    
    def getlargeur(self):
        return self.__largeur
    
    def setlongueur(self, nouvelleLongueur):
        self.__longueur = nouvelleLongueur
        print("La longueur du rectangle à été modifié par {} cm.".format(nouvelleLongueur))
    def setlargeur(self, nouvelleLargeur):
        self.__largeur = nouvelleLargeur
        print("La largeur du rectangle à été modifié par {} cm.".format(nouvelleLargeur))

Rec = Rectangle(10,6)
Rec.setlongueur(7)
Rec.setlargeur(3)