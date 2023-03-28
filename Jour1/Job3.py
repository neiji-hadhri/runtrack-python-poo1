class Operation :
    def __init__(self, nombre1 , nombre2 ) -> None:
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def addition(self):
       resultat =  self.nombre1 + self.nombre2
       print("{} + {} = {}".format(self.nombre1, self.nombre2 , resultat))
Ope = Operation(1, 4)
Ope.addition()
