import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
x = np.linspace(0, 10, 1000)
frecuencia1 = 1
frecuencia2 = 2
amplitud1 = 1
amplitud2 = 0.5

# Generación de las ondas
onda1 = amplitud1 * np.sin(2 * np.pi * frecuencia1 * x)
onda2 = amplitud2 * np.sin(2 * np.pi * frecuencia2 * x)

# Superposición de las ondas
onda_superpuesta = onda1 + onda2

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(x, onda1, label='Onda 1 (f=1 Hz)', color='blue')
plt.plot(x, onda2, label='Onda 2 (f=2 Hz)', color='red')
plt.plot(x, onda_superpuesta, label='Onda Superpuesta', color='green', linestyle='--')
plt.title('Superposición de Dos Ondas')
plt.xlabel('Posición')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()
plt.show()
