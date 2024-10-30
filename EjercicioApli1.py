import numpy as np

# Parámetros del problema
L = 10  # Longitud del abrevadero en cm
r = 1   # Radio en cm
V_dado = 12.4  # Volumen dado en cm^3
tolerancia = 0.01  # Tolerancia en cm

# Definición de la función V(h) - V_dado para encontrar la raíz
def volumen(h):
    term1 = 0.5 * np.pi * r**2
    term2 = r**2 * np.arcsin(h / r)
    term3 = h * np.sqrt(r**2 - h**2)
    return L * (term1 - term2 - term3)

def funcion_objetivo(h):
    return volumen(h) - V_dado

# Método de Bisección para encontrar h tal que volumen(h) ≈ V_dado
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

# Rango inicial para h
a = 0  # h mínima posible
b = r  # h máxima posible, que es el radio

# Calcular h con la tolerancia deseada
h_aproximado = biseccion(funcion_objetivo, a, b, tolerancia)
print(f"La profundidad del agua h en el abrevadero es aproximadamente: {h_aproximado:.2f} cm")
