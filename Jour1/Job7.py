class Livre :
    def __init__(self, titre, auteur, nombrePage) -> None:
        self.__titre = titre
        self.__auteur = auteur
        self.__page = nombrePage
        if self.__page > 0 :
            print("Le livre nommé {} écrit par {} a {} pages".format(self.__titre, self.__auteur, self.__page))
        else : 
            print("Erreur : Vous devez indiquer un nombre de page positif, recommencer à nouveau")
            return Livre 
            
    def gettitre(self):
        return self.__titre
    
    def getauteur(self):
        return self.__auteur
    
    def getnombrePage(self):
        return self.__page
    
    def setpage(self,nouvellePage):
        page = self.__page
        self.__page = nouvellePage
        if self.__page > 0 :
            print("Les {} pages ont été modifiées par : {} pages".format(page, nouvellePage))
        
        else :
            print("Erreur : Vous devez indiquer un nombre de page positif")
            return Livre
        
    
    def settitre(self,nouveauTitre):
        titre = self.__titre
        self.__titre = nouveauTitre
        print("Le titre {} a été modifié par le titre suivant : {}".format(titre, nouveauTitre))

    def setauteur(self,nouvelleAuteur):
        auteur = self.__auteur
        self.__auteur = nouvelleAuteur
        print("L'auteur {} a été modifié par l'auteur' suivant : {}".format(auteur, nouvelleAuteur))

    
        

    def nouveauLivre(self):
        if self.__page > 0 :
            print("Le nouveau livre se nomme {} écrit par {} et contient {} pages".format(self.__titre,self.__auteur, self.__page))
        else : 
            print("Le nouveau livre se nomme {} écrit par {} et les pages indiquées ne peuvent pas être négatif ".format(self.__titre,self.__auteur, self.__page))
Li = Livre("Le casse-tête", "Jean Dupond", 120)
Li.settitre("La noisette")
Li.setauteur("John Doe")
Li.setpage(-200)
Li.nouveauLivre()


