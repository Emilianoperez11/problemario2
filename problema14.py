import numpy as np
from scipy.sparse import csr_matrix


def multiplicar_matrices_disersas(matriz_a, matriz_b):
    # Convertir las matrices a formato disperso
    sparse_a = csr_matrix(matriz_a)
    sparse_b = csr_matrix(matriz_b)

    # Multiplicar las matrices dispersas
    resultado = sparse_a.dot(sparse_b)

    return resultado.toarray()


# Ejemplo de uso
matriz_a = np.array([[1, 0, 0], [0, 0, 2], [0, 3, 0]])
matriz_b = np.array([[0, 4, 0], [5, 0, 0], [0, 0, 6]])

resultado = multiplicar_matrices_disersas(matriz_a, matriz_b)
print(resultado)
