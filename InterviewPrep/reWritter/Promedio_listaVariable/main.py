# Calcular el promedio de una lista de numeros ingresadas por el usuario

# Variable que almacena la longitud de la lista
longitud = int(input("Ingrese la longitud de la lista: "))

# Hacer un ciclo para que el usuario ingrese los numeros
acumulado = 0

for i in range(longitud):
    numero = int(input("Ingrese el numero: "))
    acumulado += numero

# Calcular el promedio
promedio = acumulado / longitud

# Informar el promedio
print("El promedio de los numeros es: ", promedio)
