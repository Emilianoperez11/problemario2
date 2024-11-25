def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def son_amigables(num1, num2):
    return suma_divisores(num1) == num2 and suma_divisores(num2) == num1

# Ejemplo de uso
numero1 = 220
numero2 = 284
if son_amigables(numero1, numero2):
    print(f"{numero1} y {numero2} son números amigables.")
else:
    print(f"{numero1} y {numero2} no son números amigables.")
