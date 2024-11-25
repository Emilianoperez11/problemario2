def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

def primo_fibonacci(n):
    fib = fibonacci(n)
    for num in reversed(fib):
        if es_primo(num):
            return num
    return None

# Ejemplo de uso
n = 10
resultado = primo_fibonacci(n)
print(f"El número primo más cercano en la serie de Fibonacci hasta el índice {n} es: {resultado}")
