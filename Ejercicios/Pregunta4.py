def ingresar_alumnos(n):
    alumnos = []
    for i in range(n):
        nombre = input("Nombre del alumno {}: ".format(i + 1))
        notas = []
        for j in range(3):
            nota = float(input("Ingrese la nota {} del alumno {}: ".format(j + 1, nombre)))
            notas.append(nota)
        alumnos.append((nombre, notas))
    return alumnos

def mostrar_listado(alumnos):
    print("\nListado de Alumnos:")
    for nombre, notas in alumnos:
        print("Alumno:", nombre)
        print("Notas:", notas)

n_alumnos = int(input("Ingrese el número de alumnos: "))
lista_alumnos = ingresar_alumnos(n_alumnos)
mostrar_listado(lista_alumnos)
