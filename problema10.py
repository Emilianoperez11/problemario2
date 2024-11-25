def integral_trapecio(funcion, a, b, n):
    h = (b - a) / n
    suma = 0.5 * (funcion(a) + funcion(b))

    for i in range(1, n):
        suma += funcion(a + i * h)

    return suma * h


# Ejemplo de uso
import math

resultado = integral_trapecio(math.sin, 0, math.pi, 1000)
print(resultado)
