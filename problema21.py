import numpy as np
import matplotlib.pyplot as plt

# Definición de la función
def f(x):
    return x**3 - 4*x**2 + 6*x

# Derivada de la función
def df(x):
    return 3*x**2 - 8*x + 6

# Punto en el que se calculará la tangente
x0 = 2
y0 = f(x0)
slope = df(x0)

# Ecuación de la recta tangente
def tangent_line(x):
    return slope * (x - x0) + y0

# Valores para la gráfica
x = np.linspace(0, 4, 100)
y = f(x)
tangent_y = tangent_line(x)

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = x^3 - 4x^2 + 6x', color='blue')
plt.plot(x, tangent_y, label='Recta Tangente en x=2', color='red', linestyle='--')
plt.scatter(x0, y0, color='green')  # Punto de tangencia
plt.title('Gráfica de la función y su recta tangente')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
