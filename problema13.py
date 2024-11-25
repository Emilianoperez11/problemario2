import numpy as np

# Definir la matriz 2x2
matriz = np.array([[4, 2], [1, 3]])

# Calcular los autovalores y autovectores
autovalores, autovectores = np.linalg.eig(matriz)

# Mostrar los resultados
print("Autovalores:", autovalores)
print("Autovectores:\n", autovectores)

