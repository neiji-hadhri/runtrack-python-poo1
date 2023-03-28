class Animal :
    def __init__(self, age = 0, prenom = "") -> None:
        self.age = age
        self.prenom = prenom
        print("L'age de l'animal {} ans".format(self.age))
    def vieillir(self):
        self.age +=1
        print("L'age de l'animal {} ans".format(self.age))
    
    def nommer(self,prenom):
        self.prenom = prenom
        print("L'animal se nomme {}".format(self.prenom))

        

Ani = Animal()
Ani.nommer("Luna")
Ani.vieillir()
Ani.vieillir()
Ani.vieillir()