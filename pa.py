#El desafio de hoy va a tener relación con un hospital 
#programa ordinario

#Fila 3:
# Debe realizar un reporte que va a mostrar todos los pacientes que han sido ingresados durante la fecha que el paciente fue registrado, qué quiere decir,
# los que registran a los pacientes deben poner fecha...
# Mostrar todos los pacientes por fecha, registrar el total de pacientes que ingresó por mes. 

# Regla: 
# 1) Solo 1 encargado por fila encargado de hacer push/pull

mes_a_revisar = input("Ingrese el mes que quiere revisar: ").capitalize
print (f"{mes_a_revisar}")
fechas_registro = {
    "Enero": [],
    "Febrero": [],
    "Marzo": [],
    "Abril": [],
    "Mayo": [],
    "Junio": [],
    "Julio": [],
    "Agosto": [],
    "Septiembre": [],
    "Octubre": [],
    "Noviembre": [],
    "Diciembre": []
}

def pacientes(mes_a_revisar):
    if mes_a_revisar in fechas_registro:
        cantidad_registro = len(fechas_registro[mes_a_revisar])
        print("Cantidad de pacientes:", cantidad_registro)
    else:
        print("El mes ingresado no es válido.")

pacientes(mes_a_revisar)


