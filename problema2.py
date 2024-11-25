def fibonacci_generalizado(a, b, n):
    serie = [a, b]
    for i in range(2, n):
        siguiente = serie[i-1] + serie[i-2]
        serie.append(siguiente)
    return serie

# Ejemplo de uso
resultado = fibonacci_generalizado(3, 5, 10)
print(resultado)
