import numpy as np
import matplotlib.pyplot as plt

# Definición del polinomio
coefficients = [1, -3, 2]  # Coeficientes de P(x) = x^2 - 3x + 2
p = np.poly1d(coefficients)

# Generación de puntos para la gráfica
x = np.linspace(-1, 4, 400)
y = p(x)

# Cálculo de las raíces
roots = np.roots(coefficients)

# Visualización
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='P(x)', color='blue')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.scatter(roots, p(roots), color='red', zorder=5, label='Raíces')
plt.title('Visualización de raíces de un polinomio')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.legend()
plt.grid()
plt.show()
