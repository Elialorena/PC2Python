# Inicializamos una lista para almacenar los números que cumplen con las condiciones
numeros = []

# Iteramos sobre el rango especificado
for i in range(1500, 2701):
    # Verificamos si el número es divisible por 7 y múltiplo de 5
    if i % 7 == 0 and i % 5 == 0:
        # Si cumple, lo añadimos a la lista
        numeros.append(i)

# Imprimimos los números que cumplen con las condiciones
print("Los números que son divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:")
print(numeros)
