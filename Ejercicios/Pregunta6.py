# Inicializamos los primeros dos números de la serie
a, b = 0, 1

# Imprimimos los primeros dos números de la serie
print(a)
print(b)

# Generamos la serie hasta que el siguiente número sea mayor que 50
for _ in range(50):
    # Calculamos el siguiente número de la serie sumando los dos anteriores
    a, b = b, a + b
    # Verificamos si el número calculado es mayor que 50
    if b > 50:
        break
    # Imprimimos el siguiente número de la serie
    print(b)