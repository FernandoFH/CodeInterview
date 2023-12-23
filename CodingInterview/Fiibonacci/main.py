def fibonacci_iterativo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

# Ejemplo de uso
# n = 8  # Valor de Fibbo 
# print(f"Fibonacci({n}) =", fibonacci_iterativo(n))
    
def fibonacci_iterativo_serie(n):
    serie = []
    a, b = 0, 1
    for i in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie

# Ejemplo de uso
# n = 10  # Valor de Fibbo 
# print(f"Serie de Fibonacci hasta el término {n}:", fibonacci_iterativo_serie(n))

def fibonacci_recursiva_serie(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        serie = fibonacci_recursiva_serie(n - 1)
        serie.append(serie[-1] + serie[-2])
        return serie

# Ejemplo de uso
# n = 10  # Cambia este valor para obtener más o menos términos de la serie
# print(f"Serie de Fibonacci hasta el término {n}:", fibonacci_recursiva_serie(n))
