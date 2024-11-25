def factores_primos(n):
    factores = []
    # Dividir por 2 hasta que n sea impar
    while n % 2 == 0:
        factores.append(2)
        n //= 2
    # Comprobar los números impares desde 3 hasta la raíz cuadrada de n
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factores.append(i)
            n //= i
    # Si n es un número primo mayor que 2
    if n > 2:
        factores.append(n)
    return factores

# Ejemplo de uso
numero = 56
print(f"Los factores primos de {numero} son: {factores_primos(numero)}")
