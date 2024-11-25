N = int(input("Ingrese un número entero N: "))
factorial = 1

for i in range(1, N + 1):
    factorial *= i

print(f"El factorial de {N} es: {factorial}")
