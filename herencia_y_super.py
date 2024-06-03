class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def indentificar(self):
        print(f'Mi nombre es {self.nombre} y tengo {self.edad} años')

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def cursar(self):
        print(f'Estoy cursando {self.grado} grado')

estudiante = Estudiante("Miguel", "19", "2do")

estudiante.indentificar()
estudiante.cursar()
