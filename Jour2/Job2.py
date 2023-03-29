class Personne :
    def __init__(self,age =14) -> None:
        self.age = int(age)


    def afficherAge(self):
        print("L'âge de la personne est de {} ans ".format(self.age))

    def bonjour(self):
        print("Hello")

    def modifierage(self,nouvelleAge):
        
        self.age = int(nouvelleAge)
        print("Lâge a été modifié par l'âge de {} ans".format(nouvelleAge))

class Eleve(Personne):
    def __init__(self,age=14) -> None:
        Personne.__init__(self,age)

    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai {} ans".format(self.age))
        

class Professeur(Personne):
    def __init__(self, age, matiereEnseignee) -> None:
        Personne.__init__(self, age)
        self.matiere = matiereEnseignee

    def enseigner(self):
        print("Le cours de {} va commencer".format(self.matiere))
        


Per = Personne(18)
Per.bonjour()
Per.afficherAge()
Per.modifierage(16)
Per = Eleve()
Per.bonjour()
Per.allerEnCours()
Per.modifierage(15)
Per.affichageAge()
Per = Professeur(40,"mathématique")
Per.bonjour()
Per.afficherAge()
Per.enseigner()