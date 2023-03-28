class Student : 
    def __init__(self, nom, prenom,numEtudiant , nombreCredit = 0) -> None:
        self.__nom = nom 
        self.__prenom = prenom 
        self.__numEtudiant = numEtudiant
        self.__Credit = nombreCredit
        self.__level = self.__studentEval()

    def getnom(self):
        return self.__nom
    
    def getprenom(self):
        return self.__prenom
    
    def getnumEtudiant(self):
        return self.__numEtudiant
    
    def getCredit(self):
        return self.__Credit
    
    def getlevel(self):
        return self.__level
    
    def add_credits(self,ajoutCredit):
        self.__Credit +=ajoutCredit
        self.__level = self.__studentEval()
        print("Le nombre de crédits de {} {} avec l'ID {} est de {} points".format(self.__prenom, self.__nom, self.__numEtudiant, self.__Credit))

    def __studentEval(self):
        if self.__Credit >= 90:
            return "Excellent"
        if self.__Credit >= 80:
            return "Très bien"
        if self.__Credit >= 70:
            return "Bien"
        if self.__Credit >= 60:
            return "Passable"
        
    def studentInfo(self):
        print("Nom : {}".format(self.__nom))
        print("Prenom : {}".format(self.__prenom))
        print("Id : {}".format(self.__numEtudiant))
        print("Niveau = {}".format(self.__level))
Stu = Student("Doe","John",145)
Stu.add_credits(23)
Stu.add_credits(50)
Stu.add_credits(10)
Stu.studentInfo()