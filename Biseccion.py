import numpy as np

# Definición de la función f(x)
def f(x):
    return x**3 - 7 * x**2 + 14 * x - 6

# Método de bisección para encontrar una raíz de f(x) en el intervalo [a, b] con precisión de 10^-10
def bisection_method(f, a, b, tol=1e-10):
    # Verificamos que haya un cambio de signo en los extremos del intervalo
    if f(a) * f(b) >= 0:
        return None  # No garantiza que haya una raíz en el intervalo

    # Inicializamos variables
    c = (a + b) / 2.0  # Punto medio
    iter_count = 0  # Contador de iteraciones para seguimiento

    # Iteramos hasta alcanzar la precisión deseada
    while (b - a) / 2.0 > tol:
        iter_count += 1 #Actualizar el contador de iteraciones:
        c = (a + b) / 2.0  # Punto medio
        fc = f(c)
        
        # Si la función en el punto medio es 0, encontramos la raíz exacta
        if fc == 0 or (b - a) / 2.0 < tol:
            break
        
        # Redefinimos el intervalo
        if f(a) * fc < 0:
            b = c  # La raíz está en [a, c]
        else:
            a = c  # La raíz está en [c, b]

    return c, iter_count  # Retornamos la raíz aproximada y el número de iteraciones

# Aplicamos el método en el intervalo [0, 1]
root, iterations = bisection_method(f, 0, 1)
print(root, iterations)
print(f"La raiz aproximada con el metodo de biseccion con una presicion de 10*-10 es:{root}, ademas se lo hizo en {iterations} iteraciones")