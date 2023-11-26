# Definir la diferencia minima absoluta entre 2 elementos de una lista
# Impirmir los pares que tengan esa diferencia de forma ascendente

# diferencia minuma 2 
# input = [6, 2, 4, 10]
# output = [2, 4], [4,6]

# [2, 5, 8, 10, 15, 20, 21, 30, 31]  

# Pasos 
#  1. Ordenar la lista 
#  2. Calcualmos la direfencia minima entre los elementos consecutivos
#  Se compara con su valos anterior y si es menor se actualiza
#  3. Creamos lista para agregar los pares que complan con la deferencia minima 

def closesNumber(arr):
    arrglo_ordenado = sorted(arr)
    diferencia_minima = arrglo_ordenado[1] - arrglo_ordenado[0]
    lista_pares = []

    for i in range(len(arrglo_ordenado)-1):
        diferencia_actual = arrglo_ordenado[i+1] - arrglo_ordenado[i]
        
        if (diferencia_actual < diferencia_minima):
            lista_pares = []

        if (diferencia_actual <= diferencia_minima):
            diferencia_minima = diferencia_actual
            lista_pares.append(arrglo_ordenado[i])
            lista_pares.append(arrglo_ordenado[i+1])

    for i in range(0, len(lista_pares)-1, 2):
        print(lista_pares[i], lista_pares[i+1])


if __name__ == '__main__':
    lista = [2, 5, 8, 10, 15, 20, 21, 30, 31]
    closesNumber(lista)