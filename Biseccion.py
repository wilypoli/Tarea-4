import numpy as np

# Definición de la función f(x)
def f(x):
    return x**3 - 7 * x**2 + 14 * x - 6

# Método de bisección para encontrar una raíz de f(x) en el intervalo [a, b] con precisión de 10^-2
def metodo_biseccion(f, a, b, tol=1e-2):
    # Verificamos que haya un cambio de signo en los extremos del intervalo
    if f(a) * f(b) >= 0:
        print("El intervalo no contiene una raíz, ya que no hay un cambio de signo en sus extremos.")
        return None  # No garantiza que haya una raíz en el intervalo

    # Inicializamos variables
    c = (a + b) / 2.0  # Punto medio
    iter_count = 0  # Contador de iteraciones para seguimiento

    # Iteramos hasta alcanzar la precisión deseada
    while (b - a) / 2.0 > tol:
        iter_count += 1  # Actualizar el contador de iteraciones
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

# Aplicamos el método en un intervalo que contenga la raíz
raiz, iteraciones = metodo_biseccion(f, 3.2, 4)  # Usamos el intervalo [2, 3]
if raiz is not None:
    print(f"La raíz aproximada con el método de bisección con una precisión de 10^-2 es: {raiz}, obtenida en {iteraciones} iteraciones.")
else:
    print("No se encontró una raíz en el intervalo dado.")