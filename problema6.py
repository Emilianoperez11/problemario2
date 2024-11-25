def suma_fibonacci(n):
    a, b = 0, 1
    suma = 0
    for _ in range(n):
        suma += a
        a, b = b, a + b
    return suma

# Ejemplo de uso
n = 10
resultado = suma_fibonacci(n)
print(f"La suma de los primeros {n} términos de Fibonacci es: {resultado}")
