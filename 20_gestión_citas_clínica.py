'''
Sistema de Gestión de Citas para una Clínica
Este ejercicio está diseñado para simular un sistema de gestión 
de citas sencillo para una clínica médica. 
Incluye funcionalidades como registrar pacientes, agendar citas, 
cancelar citas y consultar el calendario.
'''

import datetime

# Estructuras de datos
pacientes = []
citas = []

# Función para registrar un nuevo paciente
def registrar_paciente():
    nombre = input("Introduce el nombre del paciente: ")
    dni = input("Introduce el DNI del paciente: ")
    if any(paciente["dni"] == dni for paciente in pacientes):
        print("❌ Este paciente ya está registrado.")
        return
    pacientes.append({"nombre": nombre, "dni": dni})
    print(f"✅ Paciente '{nombre}' registrado correctamente.")

# Función para mostrar la lista de pacientes
def mostrar_pacientes():
    if not pacientes:
        print("\n📋 No hay pacientes registrados.")
        return
    print("\n--- Lista de Pacientes ---")
    for paciente in pacientes:
        print(f"Nombre: {paciente['nombre']} | DNI: {paciente['dni']}")
    print("--------------------------")

# Función para agendar una cita
def agendar_cita():
    dni = input("Introduce el DNI del paciente: ")
    paciente = next((p for p in pacientes if p["dni"] == dni), None)
    if not paciente:
        print("❌ Paciente no encontrado. Registra primero al paciente.")
        return

    try:
        fecha_str = input("Introduce la fecha de la cita (DD/MM/AAAA): ")
        hora_str = input("Introduce la hora de la cita (HH:MM): ")
        fecha_hora = datetime.datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M")

        # Verificar si ya hay una cita en esa fecha y hora
        if any(cita["fecha_hora"] == fecha_hora for cita in citas):
            print("❌ Ya existe una cita programada para esa fecha y hora.")
            return

        citas.append({"paciente": paciente, "fecha_hora": fecha_hora})
        print(f"✅ Cita agendada para {paciente['nombre']} el {fecha_hora.strftime('%d/%m/%Y a las %H:%M')}.")
    except ValueError:
        print("❌ Formato de fecha u hora no válido. Intenta nuevamente.")

# Función para cancelar una cita
def cancelar_cita():
    try:
        fecha_str = input("Introduce la fecha de la cita a cancelar (DD/MM/AAAA): ")
        hora_str = input("Introduce la hora de la cita a cancelar (HH:MM): ")
        fecha_hora = datetime.datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M")

        cita = next((c for c in citas if c["fecha_hora"] == fecha_hora), None)
        if not cita:
            print("❌ No se encontró ninguna cita para la fecha y hora indicadas.")
            return

        citas.remove(cita)
        print(f"✅ Cita de {cita['paciente']['nombre']} el {fecha_hora.strftime('%d/%m/%Y a las %H:%M')} cancelada correctamente.")
    except ValueError:
        print("❌ Formato de fecha u hora no válido. Intenta nuevamente.")

# Función para mostrar todas las citas
def mostrar_citas():
    if not citas:
        print("\n📅 No hay citas programadas.")
        return

    print("\n--- Lista de Citas Programadas ---")
    for cita in sorted(citas, key=lambda x: x["fecha_hora"]):
        fecha_hora = cita["fecha_hora"].strftime("%d/%m/%Y a las %H:%M")
        print(f"Paciente: {cita['paciente']['nombre']} | Fecha y Hora: {fecha_hora}")
    print("----------------------------------")

# Menú principal
def sistema_gestion_citas():
    print("📅 Sistema de Gestión de Citas para Clínicas 📅")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar un nuevo paciente")
        print("2. Mostrar lista de pacientes")
        print("3. Agendar una cita")
        print("4. Cancelar una cita")
        print("5. Mostrar todas las citas")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            mostrar_pacientes()
        elif opcion == "3":
            agendar_cita()
        elif opcion == "4":
            cancelar_cita()
        elif opcion == "5":
            mostrar_citas()
        elif opcion == "6":
            print("👋 ¡Gracias por usar el sistema de gestión de citas! Hasta pronto.")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

# Ejecutar el programa
sistema_gestion_citas()
