def contar_digitos(numero, digito):
    numero_str = str(numero)  # Convertir el número a una cadena de caracteres
    cantidad = numero_str.count(str(digito))  # Contar la cantidad de veces que aparece el dígito
    return cantidad

# Ejemplo de uso
numero = 15789000
digito = 0
cantidad = contar_digitos(numero, digito)
print("Cantidad de veces {} en el número {}: {}".format(digito, numero, cantidad))
