def convertir_fecha(fecha):
    # Definir el diccionario de mapeo de meses
    meses = {
        "Enero": "01",
        "Febrero": "02",
        "Marzo": "03",
        "Abril": "04",
        "Mayo": "05",
        "Junio": "06",
        "Julio": "07",
        "Agosto": "08",
        "Septiembre": "09",
        "Octubre": "10",
        "Noviembre": "11",
        "Diciembre": "12"
    }

    # Dividir la fecha en mes, día y año
    partes = fecha.split()
    if len(partes) == 3:  # Formato "Septiembre 8, 1636"
        mes = partes[0]
        dia = partes[1][:-1]  # Eliminar la coma al final del día
        anio = partes[2]
    else:  # Formato "9/8/1636"
        mes, dia, anio = fecha.split('/')

    # Ajustar el formato del día y el año
    dia = dia.zfill(2)
    anio = anio.zfill(4)

    # Obtener el número del mes
    if mes.isdigit():  # Si el mes está en formato numérico
        mes_num = mes.zfill(2)
    else:  # Si el mes está en formato de nombre
        mes_num = meses[mes]

    # Construir la fecha en el formato AAAA-MM-DD
    fecha_convertida = f"{anio}-{mes_num}-{dia}"
    return fecha_convertida

# Ejemplo de uso
fecha = input("Ingrese una fecha en uno de los formatos especificados: ")
fecha_convertida = convertir_fecha(fecha)
print("Fecha convertida:", fecha_convertida)
