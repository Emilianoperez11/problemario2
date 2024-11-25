import numpy as np

def determinante_matriz(matriz):
    if matriz.shape[0] > 4 or matriz.shape[1] > 4:
        raise ValueError("La matriz debe ser de tamaño 4x4 o menor.")
    return np.linalg.det(matriz)

# Ejemplo de uso
matriz_2x2 = np.array([[1, 2], [3, 4]])
matriz_3x3 = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
matriz_4x4 = np.array([[1, 0, 2, -1], [3, 0, 0, 5], [2, 1, 3, 4], [1, 2, 0, 0]])

print(determinante_matriz(matriz_2x2))
print(determinante_matriz(matriz_3x3))
print(determinante_matriz(matriz_4x4))
