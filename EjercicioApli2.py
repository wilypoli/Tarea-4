import numpy as np

# Definición de constantes
g = 9.81  # Gravedad en m/s^2
s0 = 300  # Altura inicial en metros
m = 0.25  # Masa en kg
k = 0.1   # Coeficiente de resistencia en Ns/m
tolerancia = 0.01  # Tolerancia en segundos

# Definición de la función s(t) - altura del objeto en función del tiempo
def s(t):
    term1 = s0
    term2 = -(m * g / k) * t
    term3 = (m**2 * g / k**2) * (1 - np.exp(-k * t / m))
    return term1 + term2 + term3

# Definición de la función objetivo f(t) = s(t) - 0, para que busquemos f(t) = 0
def funcion_objetivo(t):
    return s(t)

# Método de Bisección para encontrar t tal que s(t) ≈ 0
def biseccion(f, a, b, tol):
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c  # Encontramos la raíz exacta
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Rango inicial para t
a = 0  # Tiempo inicial
b = 100  # Estimación de tiempo máximo (ajústalo si es necesario)

# Calcular t con la tolerancia deseada
t_aproximado = biseccion(funcion_objetivo, a, b, tolerancia)
print(f"El tiempo aproximado que tarda el objeto en caer al suelo es: {t_aproximado:.2f} segundos")
