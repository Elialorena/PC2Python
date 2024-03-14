def patron(n):
    for i in range(n):  # Iterar sobre el número de filas
        for j in range(i + 1):  # Iterar sobre el número de columnas en cada fila
            print("*", end=" ")  # Imprimir asteriscos
        print()  # Saltar a una nueva línea después de imprimir una fila
    
    for i in range(n - 1, 0, -1):  # Iterar en reversa para imprimir la parte inferior del patrón
        for j in range(i):  # Iterar sobre el número de columnas en cada fila
            print("*", end=" ")  # Imprimir asteriscos
        print()  # Saltar a una nueva línea después de imprimir una fila

# Llamar a la función para construir el patrón con 5 filas en la parte superior
patron(5)
