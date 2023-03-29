class Véhicule :
    def __init__(self, marque, modele, annee, prix) -> None:
        self.marque = marque 
        self.modele = modele
        self.annee = int(annee)
        self.prix = int(prix)

    def informationVehicule(self):

        print("Marque = {}".format(self.marque))
        print("Modèle = {}".format(self.modele))
        print("Année : {}".format(self.annee))
        print("Prix : {} euros".format(self.prix))

    def demarrer(self):
        print("Attention!!! Je roule")


class Voiture(Véhicule):
    def __init__(self, marque, modele, annee, prix, portes = 4) -> None:
        Véhicule.__init__(self, marque, modele, annee, prix)
        self.portes = int(portes)

    def informationVehicule(self):
        print("Marque = {}".format(self.marque))
        print("Modèle = {}".format(self.modele))
        print("Année : {}".format(self.annee))
        print("Prix : {} euros".format(self.prix))
        print("Nombre de portes du véhicule : {}".format(self.portes))

class Moto(Véhicule) :
    def __init__(self, marque, modele, annee, prix, roue = 2) -> None:
        Véhicule.__init__(self, marque, modele, annee, prix)
        self.roue = int(roue)

    def informationVehicule(self):
        print("Marque = {}".format(self.marque))
        print("Modèle = {}".format(self.modele))
        print("Année : {}".format(self.annee))
        print("Prix : {} euros".format(self.prix))
        print("Nombre de roues : {}".format(self.roue))


        
        
    
Véh = Véhicule("Citroën","C3",2010, 12000)
Véh.informationVehicule()
print("----------------------------------------------------------------")
Véh = Voiture("Citroën","C3",2010, 12000)
Véh.informationVehicule()      
Véh.demarrer()
print("----------------------------------------------------------------")
Véh = Moto("Yamaha","1200 Vmax", 1987, 4500)
Véh.informationVehicule()
Véh.demarrer()
