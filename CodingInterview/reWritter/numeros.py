numero1 = 10
numero2 = 0b1010
numero3 = 0xA

print(numero1)
print(type(numero1))
print(numero2)
print(type(numero2))
print(numero3)
print(type(numero3))


##Shift left 
numero = 10       # binario: 0b1010
resultado = numero << 1  # desplazamiento a la izquierda por 1 bit
print(resultado)  # 10


numero = 10
print(bin(numero))  # Output: 0b1010
print(bin(numero)[2:])  # Output: 1010

## Byte
print(format(numero, '08b'))  # Output: 00001010

