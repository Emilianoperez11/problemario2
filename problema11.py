import sympy as sp

def tangente_a_curva(funcion, punto):
    x = sp.symbols('x')
    f = funcion(x)
    derivada = sp.diff(f, x)
    pendiente = derivada.subs(x, punto)
    y_intercepto = f.subs(x, punto) - pendiente * punto
    ecuacion_tangente = pendiente * x + y_intercepto
    return ecuacion_tangente

# Ejemplo de uso
funcion = lambda x: x**2
punto = 1
print(tangente_a_curva(funcion, punto))
