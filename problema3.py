def fibonacci_position(n):
    a, b = 0, 1
    position = 0
    while a < n:
        a, b = b, a + b
        position += 1
    return position if a == n else -1

# Ejemplo de uso
numero = 21
resultado = fibonacci_position(numero)
print(f"La posición de {numero} en la serie de Fibonacci es: {resultado}")


