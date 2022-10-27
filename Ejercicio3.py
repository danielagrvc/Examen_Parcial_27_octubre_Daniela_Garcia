class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return "El alumno {} se ha creado con éxito".format(self.nombre)

clase=[]
nota=[]
clase.append(input("Como te llamas?"))
nota.append(input("Que has sacado en el examen"))

def calificacion(nombre, nota):
    for i in range(len(nota)):
        if int(nota[i]) >= 5:
            print(nombre, "Enhorabuena, has aprobado algoritmos, gracias a Ruben")
        elif int(nota[i]) >= 9:
            print(nombre, "WOW, te has ganado una matricula")
        else:
            print(nombre,"Eres un poco paquete, has suspendido")

calificacion(clase, nota)
        
