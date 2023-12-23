# Validate Subsequence
# Validar que la lista segundaria es una subsecuencia de la primaria

# principal: [8 , 30, 10, 15, -1, 4, 22]
# secondary: [8, 30, 4, 22]


def validate_subsequence(principal, secondary):
    index_principal = 0
    index_secondary = 0

    if len(secondary) > len(principal):
        return False
    else:
        while index_principal < len(principal) and index_secondary < len(secondary):
            if principal[index_principal] == secondary[index_secondary]:
                index_secondary += 1
            index_principal += 1
    
        return index_secondary == len(secondary)

# Punto de entrada
# print(validate_sub_sequence([8, 30, 10, 15, -1, 4, 22], [8, 30, 4, 22]))
if __name__ == '__main__':
    principal = [8, 30, 10, 15, -1, 4, 22]
    secondary = [8, 30, 4, 22]

    respuesta = validate_subsequence(principal, secondary)
    print(respuesta)