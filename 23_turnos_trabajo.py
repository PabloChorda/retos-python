'''
Gestión de Turnos de Trabajo

Desarrolla un programa en Python que permita gestionar los turnos de trabajo de empleados de una empresa. El programa debe ofrecer un menú 
interactivo para realizar las siguientes acciones:
Registrar un turno de trabajo: Permite registrar un turno ingresando el nombre del empleado, la fecha, la hora de inicio y la hora de fin. 
Valida que la hora de inicio sea anterior a la hora de fin y que los formatos ingresados sean correctos.
Ver turnos de un empleado: Muestra todos los turnos registrados para un empleado específico.
Mostrar todos los turnos: Lista todos los turnos registrados con la información del empleado, fecha, hora de inicio y hora de fin.
Actualizar un turno: Permite modificar la hora de inicio y fin de un turno existente, especificando el nombre del empleado y la fecha del turno a actualizar.
Eliminar un turno: Elimina un turno específico indicando el nombre del empleado y la fecha correspondiente.
Salir del programa: Termina la ejecución del programa.
El programa debe manejar errores comunes, como formatos de entrada incorrectos, turnos inexistentes y validaciones lógicas (por ejemplo, la hora de inicio no puede ser posterior a la hora de fin).
'''

import datetime

def menu_principal():
    print("\n=== GESTIÓN DE TURNOS DE TRABAJO ===")
    print("1. Registrar un turno de trabajo")
    print("2. Ver turnos de un empleado")
    print("3. Mostrar todos los turnos")
    print("4. Actualizar un turno")
    print("5. Eliminar un turno")
    print("6. Salir")

def validar_fecha(fecha):
    try:
        return datetime.datetime.strptime(fecha, "%Y-%m-%d").date()
    except ValueError:
        print("Error: Formato de fecha inválido. Use el formato YYYY-MM-DD.")
        return None

def validar_hora(hora):
    try:
        return datetime.datetime.strptime(hora, "%H:%M").time()
    except ValueError:
        print("Error: Formato de hora inválido. Use el formato HH:MM.")
        return None

turnos = []

def registrar_turno():
    empleado = input("Ingrese el nombre del empleado: ").strip()
    if not empleado:
        print("Error: El nombre del empleado no puede estar vacío.")
        return

    fecha = validar_fecha(input("Ingrese la fecha del turno (YYYY-MM-DD): ").strip())
    if not fecha:
        return

    hora_inicio = validar_hora(input("Ingrese la hora de inicio del turno (HH:MM): ").strip())
    if not hora_inicio:
        return

    hora_fin = validar_hora(input("Ingrese la hora de fin del turno (HH:MM): ").strip())
    if not hora_fin:
        return

    if hora_inicio >= hora_fin:
        print("Error: La hora de inicio debe ser anterior a la hora de fin.")
        return

    turno = {
        "empleado": empleado,
        "fecha": fecha,
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin
    }
    turnos.append(turno)
    print("Turno registrado exitosamente.")

def ver_turnos_empleado():
    empleado = input("Ingrese el nombre del empleado: ").strip()
    if not empleado:
        print("Error: El nombre del empleado no puede estar vacío.")
        return

    turnos_empleado = [t for t in turnos if t["empleado"].lower() == empleado.lower()]

    if not turnos_empleado:
        print(f"No se encontraron turnos para {empleado}.")
        return

    print(f"\nTurnos de {empleado}:")
    for t in turnos_empleado:
        print(f"Fecha: {t['fecha']} | Inicio: {t['hora_inicio']} | Fin: {t['hora_fin']}")

def mostrar_todos_los_turnos():
    if not turnos:
        print("No hay turnos registrados.")
        return

    print("\n=== TODOS LOS TURNOS ===")
    for t in turnos:
        print(f"Empleado: {t['empleado']} | Fecha: {t['fecha']} | Inicio: {t['hora_inicio']} | Fin: {t['hora_fin']}")

def actualizar_turno():
    empleado = input("Ingrese el nombre del empleado: ").strip()
    if not empleado:
        print("Error: El nombre del empleado no puede estar vacío.")
        return

    fecha = validar_fecha(input("Ingrese la fecha del turno a actualizar (YYYY-MM-DD): ").strip())
    if not fecha:
        return

    for turno in turnos:
        if turno["empleado"].lower() == empleado.lower() and turno["fecha"] == fecha:
            print("Turno encontrado:")
            print(f"Inicio: {turno['hora_inicio']} | Fin: {turno['hora_fin']}")

            nuevo_inicio = validar_hora(input("Ingrese la nueva hora de inicio (HH:MM): ").strip())
            if not nuevo_inicio:
                return

            nuevo_fin = validar_hora(input("Ingrese la nueva hora de fin (HH:MM): ").strip())
            if not nuevo_fin:
                return

            if nuevo_inicio >= nuevo_fin:
                print("Error: La hora de inicio debe ser anterior a la hora de fin.")
                return

            turno["hora_inicio"] = nuevo_inicio
            turno["hora_fin"] = nuevo_fin
            print("Turno actualizado exitosamente.")
            return

    print("No se encontró un turno para esa combinación de empleado y fecha.")

def eliminar_turno():
    empleado = input("Ingrese el nombre del empleado: ").strip()
    if not empleado:
        print("Error: El nombre del empleado no puede estar vacío.")
        return

    fecha = validar_fecha(input("Ingrese la fecha del turno a eliminar (YYYY-MM-DD): ").strip())
    if not fecha:
        return

    for turno in turnos:
        if turno["empleado"].lower() == empleado.lower() and turno["fecha"] == fecha:
            turnos.remove(turno)
            print("Turno eliminado exitosamente.")
            return

    print("No se encontró un turno para esa combinación de empleado y fecha.")

while True:
    menu_principal()
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        registrar_turno()
    elif opcion == "2":
        ver_turnos_empleado()
    elif opcion == "3":
        mostrar_todos_los_turnos()
    elif opcion == "4":
        actualizar_turno()
    elif opcion == "5":
        eliminar_turno()
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
