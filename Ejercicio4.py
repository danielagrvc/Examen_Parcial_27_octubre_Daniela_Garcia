class Alumno():
    def __init__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota
    def __str__(self):
        return "El alumno {} ha sacado {} ".format(self.nombre, self.nota)

class Deporte(Alumno):
    def __init__(self, nombre, nota, deporte):
        super().__init__(nombre, nota)
        self.deporte= deporte
    def __str__(self):
        return Alumno.__str__(self)+" En el deporte{}".format(self.deporte)
class Deporte(Alumno):
    def __init__(self, nombre, nota, deporte):
        super().__init__(nombre, nota)
        self.deporte = deporte
    def __str__(self):
        return Alumno. __str__ (self)+"en el deporte {}".format(self.deporte)

a =Deporte("Daniela", 9, "Voleibol")
print(a)
b= Deporte("Maria", 6,"Futbol")
print(b)
c= Deporte("Ruben", "la mejor puntuación", "De..... motos")
print(c)


