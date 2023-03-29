class Forme:
    def __init__(self) -> None:
        pass

    def aire(self):
        return 0
    

class Rectangle(Forme):
    def __init__(self, longueur, largeur) -> None:
        Forme.__init__(self)
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        resultat = self.longueur * self.largeur
        print("L'air du rectangle est de {} cm²".format(resultat))

For = Forme()
For.aire()
For = Rectangle(10,5)
For.aire()