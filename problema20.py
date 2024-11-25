import matplotlib.pyplot as plt

def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series

def suma_acumulada(series):
    return [sum(series[:i+1]) for i in range(len(series))]

n = 10
fib_series = fibonacci(n)
acumulada = suma_acumulada(fib_series)

plt.bar(range(n), acumulada)
plt.xlabel('Índices de Fibonacci')
plt.ylabel('Suma Acumulada')
plt.title('Gráfica de Fibonacci Acumulativo')
plt.xticks(range(n))
plt.show()
