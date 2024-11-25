import sympy as sp

# Definimos la variable y la función cuadrática
x = sp.symbols('x')
funcion = x**2 - 4*x + 3

# Calculamos la derivada de la función
derivada = sp.diff(funcion, x)

# Encontramos los puntos críticos
puntos_criticos = sp.solve(derivada, x)

# Evaluamos la función en los puntos críticos
valores = [funcion.subs(x, pc) for pc in puntos_criticos]

# Determinamos el mínimo o máximo
resultado = list(zip(puntos_criticos, valores))
resultado
