#De forma iterativa
import numpy as np
def construccion(matriz):
    matriz= np.array([[4,3,2,5,6] , [1,2,7,8,3], [3,8,9,3,1], [2,3,5,6,1], [1,3,4,6,4]])
    determinante=np.linalg.det(matriz)
    return determinante
#De forma recursiva
class Matriz():
    def __init__(self,filas: list[list[int]]):
        self.filas = filas
        self.filas = []

    def columns(self, columnas: list[list[int]]):
        self.columnas = columnas
        return [[fila[i] for fila in self.filas] for i in range(len(self.filas[0]))]

    def numero_filas(self):
        return len(self.filas)
    def numero_columnas(self):
        return len(self.filas[0])

    def order(self):
        return (self.numero_filas, self.numero_columnas)
    
    def determinante(self):
        if self.order ==(0,0):
            return 1
        elif self.order ==(1,1):
            return int(self.filas[0][0])
        elif self.orden == (2, 2):
            return int((self.filas[0][0] * self.filas[1][1])
                - (self.filas[0],[1]* self.filas[1],[0])
        else:
            return sum(self.filas[0][self.filas[0]]* self.filas[0][columna])
                for columna in range(self.numero_columnas))
