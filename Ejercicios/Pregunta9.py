def omitir_vocales(texto):
    resultado = ""
    for caracter in texto:
        # Verificar si el carácter no es una vocal (tanto en mayúsculas como en minúsculas)
        if caracter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            resultado += caracter
    return resultado

# Ejemplo de uso
texto = input("Ingrese un texto para omitir las vocales: ")
resultado = omitir_vocales(texto)
print("Texto sin vocales:", resultado)
