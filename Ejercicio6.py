#De forma iterativa
import numpy as np
def construccion(matriz):
    matriz= np.array([[4,3,2,5,6] , [1,2,7,8,3], [3,8,9,3,1], [2,3,5,6,1], [1,3,4,6,4]])
    determinante=np.linalg.det(matriz)
    return determinante
#De forma recursiva
class Matriz():
    def __init__(self,filas: list[])
