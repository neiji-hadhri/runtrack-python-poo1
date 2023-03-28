class Operation :
    def __init__(self, nombre1 , nombre2 ) -> None:
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        

Ope = Operation(1, 4)
print("Le nombre 1 est {}".format(Ope.nombre1))
print("Le nombre 2 est {}".format(Ope.nombre2))