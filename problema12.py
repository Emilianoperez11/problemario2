import numpy as np


def gauss_elimination(A, b):
    n = len(b)
    # Eliminación hacia adelante
    for i in range(n):
        # Hacer que el pivote sea 1
        A[i] = A[i] / A[i][i]
        b[i] = b[i] / A[i][i]

        for j in range(i + 1, n):
            factor = A[j][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]

    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i] - np.dot(A[i][i + 1:], x[i + 1:])

    return x


# Ejemplo de uso
A = np.array([[3, 2, -4], [2, 3, 3], [5, -3, 1]], dtype=float)
b = np.array([3, 15, 14], dtype=float)
solucion = gauss_elimination(A, b)
print(solucion)
