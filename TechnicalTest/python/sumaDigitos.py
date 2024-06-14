# En la variable numbers dispones de una lista de nuemros enteros.
# Debes implementar una fauncion que devuelva una diccionario con la suma de los digitos de cada numero 

# Ejemplo: {123: 6}

numbers = [123, 456, 789, 101, 202, 303]

def sum_digits(number):
    total:int = 0
    for digit in str(number):
        total += int(digit)
    return total 


def calculate_digit_sums(numbers):  
    sum_digits_dict = {}
    for number in numbers:
        sum_digits_dict[number] = sum_digits(number)
    return sum_digits_dict


result = calculate_digit_sums(numbers)

print(result)
