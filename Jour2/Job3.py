class Rectangle : 
    def __init__(self,longueur, largeur) -> None:
        self._longueur = longueur
        self._largeur = largeur

    def getlongueur(self):
        return self._longueur
    
    def getlargeur(self):
        return self._largeur
    

    def perimetre(self):
        resultat = (self._longueur + self._largeur) * 2
        print("Le périmètre de ce rectangle est de {} cm".format(resultat))
    def surface(self):
        resultat1 = self._longueur * self._largeur
        print("La surface de ce rectangle est de {} cm²".format(resultat1))


class Parallépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur) -> None:
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def gethauteur(self):
        return self.__hauteur
    

    def volume(self):
        resultat = self._longueur * self._largeur * self.__hauteur
        print("Le volume du parallélépipède est de {} cm3".format(resultat))


Rec = Rectangle(10,5)
Rec.perimetre()
Rec.surface()
Rec = Parallépipède(10, 5, 12)
Rec.volume()