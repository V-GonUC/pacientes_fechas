#El desafio de hoy va a tener relación con un hospital 
#programa ordinario

#Fila 3:
# Debe realizar un reporte que va a mostrar todos los pacientes que han sido ingresados durante la fecha que el paciente fue registrado, qué quiere decir,
# los que registran a los pacientes deben poner fecha...
# Mostrar todos los pacientes por fecha, registrar el total de pacientes que ingresó por mes. 

# Regla: 
# 1) Solo 1 encargado por fila encargado de hacer push/pull

mes_a_revisar = input("Ingrese el mes que quiere revisar: ")

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
        print(f"Cantidad de pacientes en {mes_a_revisar}:", cantidad_registro)
    else:
        print("El mes ingresado no es válido.")

pacientes(mes_a_revisar)

pacientes = {
    12345678: {"nombre": "María José Fuentes Rojas", "edad": 34, "telefono": "+56 9 1111 2222",
               "direccion": "Av. Los Pinos 123, Santiago", "ingreso": "02/10/2026", "salida": "07/10/2026"},
    15987654: {"nombre": "Carlos Andrés Soto Vega", "edad": 52, "telefono": "+56 9 3333 4444",
               "direccion": "Calle Las Rosas 456, Valparaíso", "ingreso": "10/10/2026", "salida": "15/10/2026"},
    18456123: {"nombre": "Camila Antonia Pérez Díaz", "edad": 27, "telefono": "+56 9 5555 6666",
               "direccion": "Pasaje Los Olivos 78, Concepción", "ingreso": "18/10/2026", "salida": "20/10/2026"},
    9876543: {"nombre": "Luis Alberto Muñoz Castro", "edad": 68, "telefono": "+56 9 7777 8888",
              "direccion": "Av. Central 910, Temuco", "ingreso": "20/10/2026", "salida": "23/10/2026"},
}

def buscar():
    try:
        run = int(input("RUN a buscar (sin puntos ni dígito verificador): "))
    except ValueError:
        print("El RUN debe ser un número")
        return
    if run in pacientes:
        p = pacientes[run]
        print("RUN:", run)
        print("Nombre:", p["nombre"])
        print("Edad:", p["edad"])
        print("Teléfono:", p["telefono"])
        print("Dirección:", p["direccion"])
        print("Ingreso:", p["ingreso"])
        print("Salida:", p["salida"])
    else:
        print("Paciente no encontrado")

buscar()


