import sympy as sp

def derivada_simbolica(expresion):
    x = sp.symbols('x')
    expr = sp.sympify(expresion)
    return sp.diff(expr, x)

# Ejemplo de uso
resultado = derivada_simbolica('3*x**2 + 2*x')
print(resultado)
