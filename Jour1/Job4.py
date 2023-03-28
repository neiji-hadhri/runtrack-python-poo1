class Personne :
    def __init__(self, nom, prenom) -> None:
        self.prenom = prenom
        self.nom = nom 

    def SePresenter(self):
        print("Je suis {} {}".format(self.prenom, self.nom))

Per = Personne("Doe", "John")
Per.SePresenter()
Per = Personne("Dupond", "Jean")
Per.SePresenter()

        