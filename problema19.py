def numero_de_caminos(n):
    # Crear una matriz para almacenar los resultados
    caminos = [[0] * (n + 1) for _ in range(n + 1)]

    # Hay un solo camino para llegar a cualquier celda en la primera fila o columna
    for i in range(n + 1):
        caminos[i][0] = 1
        caminos[0][i] = 1

    # Calcular el número de caminos
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            caminos[i][j] = caminos[i - 1][j] + caminos[i][j - 1]

    return caminos[n][n]


# Ejemplo de uso
n = 3
print(f"Número de caminos en una cuadrícula de {n}x{n}: {numero_de_caminos(n)}")
