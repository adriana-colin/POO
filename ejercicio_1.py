#Creación de la clase "Estudiante" con atributos
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f'El estudiante {self.nombre} esta estudiando')

#Obtención de los datos del usuario
nombre = input("Ingresa un nombre: ")
edad = input("Ahora la edad edad: ")
grado = input("Por último el grado: ")

#Asignación de valores en propiedades de objeto clase 'Estudiante'
estudiante = Estudiante(nombre, edad, grado)

print(f"""
    DATOS DEL ESTUDIANTE:
    Nombre: {estudiante.nombre}
    Edad: {estudiante.edad}
    Grado: {estudiante.grado}
""")

while True:
    estado = input("Ingresa la palabra 'estudiar' para actualizar el estado del estudiante \n")
   
    if estado.lower() == "estudiar":
        estudiante.estudiar()
        break
    