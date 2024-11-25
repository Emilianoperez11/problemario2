import numpy as np

def encontrar_raices(p):
    raices = np.roots(p)
    raices_reales = [r for r in raices if np.isreal(r)]
    return np.real(raices_reales)

# Coeficientes del polinomio de tercer grado
coeficientes = [1, -6, 11, -6]  # Ejemplo: x^3 - 6x^2 + 11x - 6
raices = encontrar_raices(coeficientes)
print("Las raíces reales del polinomio son:", raices)
