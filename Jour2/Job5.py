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


class Cercle(Forme):
    def __init__(self, radius) -> None:
        Forme.__init__(self)
        self.radius = radius
        
    def aire(self):
        resultat = 3.14159265359 * (self.radius**2)
        print("Le rayon de ce cercle est de {} cm".format(resultat))


For = Rectangle(10,5)
For.aire()
For = Cercle(2)
For.aire()