class Animal():
    def __init__(self):
        pass

    def comer(self):
        print("El animal esta comiendo")


class Mamífero(Animal):
     def amamantar(self):
         print("El animal esta amamantando")

   
class Ave(Animal):
     def volar(self):
         print("El animal esta volando")

class Murciélago(Mamífero, Ave):
    pass

murcielago = Murciélago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()