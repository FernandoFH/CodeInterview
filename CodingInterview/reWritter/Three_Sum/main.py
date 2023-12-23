#  Dada una Lista, listar de 3 numeros que sumen el numero suma_objetivo
#  lista_original / suma_objetivo 

# lista_original = [-7, -1, 8, -10, 6, 4, -8, 1, 7]
# suma_objetivo = 0
# respuesta [-10, 4, 6], [-8, 1, 7], [-7, -1, 8], [-7, 1, 6]
# 
# # Pasos 
    # [] Ordenar lista_original
    # [] Usamos 2 punteros para convinar (pi, pd)
    # [] Si suma_temporal < suma_objetivo movemos pi hacia la derecha
    # [] Si suma_temporal > suma_objetivo movemos pd hacia la izquierda
    # [] Si pd y pi se cruzan movemos pi uno mas del base y pd hacia la derecha
    # [] Si el numero es igual a suma_objetivo sumarlo 

def three_number_sum(lista_original, suma_objetivo):
    lista_original.sort()
    tripletas = []

    for numero_actual in range(len(lista_original) - 2):
        pi = numero_actual + 1
        pd = len(lista_original) - 1

        while pi < pd:
            suma_temporal = lista_original[numero_actual] + lista_original[pi] + lista_original[pd]

            if suma_temporal == suma_objetivo:
                tripletas.append([lista_original[numero_actual], lista_original[pi], lista_original[pd]])
                pi += 1
                pd -= 1
            elif suma_temporal < suma_objetivo:
                pi += 1
            else:
                pd -= 1
    
    return tripletas


## Punto de entrada
if __name__ == "__main__":
    lista_original = [-7, -1, 8, -10, 6, 4, -8, 1, 7]
    suma_objetivo = 0
    respuesta = three_number_sum(lista_original, suma_objetivo)
    print(respuesta)