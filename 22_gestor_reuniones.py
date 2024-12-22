'''
Diseña un programa en Python que permita gestionar las reservas de salas de reuniones en una oficina. El sistema debe incluir las siguientes funcionalidades:

Registrar reservas: El usuario podrá seleccionar una sala, 
indicar la fecha y hora de la reserva, y proporcionar su nombre. Antes de confirmar la reserva, el sistema debe verificar que no exista otra reserva para la misma sala, fecha y hora.
Mostrar reservas actuales: Se deberá listar todas las reservas registradas, mostrando información como la sala, fecha, hora y nombre del usuario.
Eliminar reservas: El usuario podrá seleccionar una reserva existente para eliminarla del sistema.
Generar un resumen por sala: El programa debe contar con una opción para mostrar cuántas reservas hay en total por cada sala registrada.
Validaciones: El sistema debe verificar que las fechas sean válidas (no se pueden realizar reservas en fechas pasadas) y que los datos ingresados por el usuario estén en un formato adecuado.
El programa debe ser interactivo, basado en un menú que permita navegar fácilmente entre las opciones. Además, debe ser robusto ante entradas incorrectas y mostrar mensajes claros para guiar al usuario.

Ejemplo de uso:

Un usuario reserva la sala "A1" para el 25/12/2024 a las 10:00 AM bajo su nombre.
Al intentar reservar nuevamente la sala "A1" en el mismo horario, el sistema informa que no está disponible.
El usuario consulta todas las reservas existentes y decide eliminar una de ellas.
Finalmente, genera un resumen que muestra cuántas reservas hay en cada sala.
'''

import datetime

# Diccionario para almacenar las reservas
reservas = {}

# Función para mostrar el menú
def mostrar_menu():
    print("\nGestor de Reservas de Salas de Reunión")
    print("1. Registrar una reserva")
    print("2. Mostrar todas las reservas")
    print("3. Eliminar una reserva")
    print("4. Generar resumen por sala")
    print("5. Salir")

# Función para registrar una reserva
def registrar_reserva():
    sala = input("Introduce el nombre de la sala: ").strip()
    nombre_usuario = input("Introduce tu nombre: ").strip()
    
    try:
        fecha = input("Introduce la fecha de la reserva (YYYY-MM-DD): ").strip()
        hora = input("Introduce la hora de la reserva (HH:MM): ").strip()
        fecha_hora_reserva = datetime.datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")
        
        if fecha_hora_reserva < datetime.datetime.now():
            print("Error: No puedes realizar reservas en fechas pasadas.")
            return
        
        # Comprobación de conflictos
        if sala in reservas:
            for reserva in reservas[sala]:
                if reserva['fecha_hora'] == fecha_hora_reserva:
                    print("Error: La sala ya está reservada en esa fecha y hora.")
                    return
        else:
            reservas[sala] = []
        
        # Registrar la reserva
        reservas[sala].append({
            'nombre_usuario': nombre_usuario,
            'fecha_hora': fecha_hora_reserva
        })
        print(f"Reserva realizada con éxito para la sala {sala} el {fecha_hora_reserva}.")
    except ValueError:
        print("Error: Formato de fecha u hora inválido.")

# Función para mostrar todas las reservas
def mostrar_reservas():
    if not reservas:
        print("No hay reservas registradas.")
        return
    
    for sala, lista_reservas in reservas.items():
        print(f"\nSala: {sala}")
        for reserva in lista_reservas:
            print(f"- {reserva['fecha_hora']} | Usuario: {reserva['nombre_usuario']}")

# Función para eliminar una reserva
def eliminar_reserva():
    sala = input("Introduce el nombre de la sala de la reserva que deseas eliminar: ").strip()
    if sala not in reservas or not reservas[sala]:
        print("Error: No hay reservas para esta sala.")
        return
    
    try:
        fecha = input("Introduce la fecha de la reserva (YYYY-MM-DD): ").strip()
        hora = input("Introduce la hora de la reserva (HH:MM): ").strip()
        fecha_hora_reserva = datetime.datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")
        
        for reserva in reservas[sala]:
            if reserva['fecha_hora'] == fecha_hora_reserva:
                reservas[sala].remove(reserva)
                print("Reserva eliminada con éxito.")
                if not reservas[sala]:
                    del reservas[sala]
                return
        print("Error: No se encontró ninguna reserva en esa fecha y hora.")
    except ValueError:
        print("Error: Formato de fecha u hora inválido.")

# Función para generar resumen por sala
def generar_resumen():
    if not reservas:
        print("No hay reservas registradas.")
        return
    
    print("\nResumen de reservas por sala:")
    for sala, lista_reservas in reservas.items():
        print(f"- Sala {sala}: {len(lista_reservas)} reservas")

# Bucle principal
def gestor_reservas():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ").strip()
        if opcion == "1":
            registrar_reserva()
        elif opcion == "2":
            mostrar_reservas()
        elif opcion == "3":
            eliminar_reserva()
        elif opcion == "4":
            generar_resumen()
        elif opcion == "5":
            print("Saliendo del gestor de reservas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

# Ejecutar el programa
gestor_reservas()
