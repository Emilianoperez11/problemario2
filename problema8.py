def derivada(funcion, x, h=1e-5):
    return (funcion(x + h) - funcion(x - h)) / (2 * h)

# Ejemplo de uso
def f(x):
    return x**2

punto = 2
resultado = derivada(f, punto)
print(f"La derivada de f en x={punto} es aproximadamente {resultado}")

