def factorial(numero):
    # Verificar si el número es negativo
    if numero < 0:
        return "El factorial no está definido para números negativos."
    # Inicializar el resultado del factorial
    resultado = 1
    # Calcular el factorial
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Ejemplo de uso
numero = int(input("Ingrese un número para calcular su factorial: "))
print("El factorial de", numero, "es:", factorial(numero))
