def es_primo(numero):
    # Verificar si el número es menor o igual a 1
    if numero <= 1:
        return False
    # Iterar desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero ** 0.5) + 1):
        # Verificar si el número es divisible por algún número en ese rango
        if numero % i == 0:
            return False
    return True

# Ejemplo de uso
numero = int(input("Ingrese un número para verificar si es primo: "))
if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")
