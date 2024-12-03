'''
Crea un programa para gestionar las reservas de clases en un gimnasio. Los usuarios podrán registrarse en clases específicas, cancelar sus reservas, y el programa deberá mostrar estadísticas como cuántas plazas quedan disponibles por clase.

Cada reserva tiene los siguientes datos:

Nombre del usuario: Persona que hace la reserva.
Clase reservada: Nombre de la clase (ejemplo: "Yoga", "Spinning", "CrossFit").
Horario: Fecha y hora de la clase.
Estado: Puede ser reservado o cancelado.
Cada clase tiene un número limitado de plazas disponibles.

Tu programa debe incluir las siguientes funcionalidades:

Mostrar las clases disponibles: Listar las clases, sus horarios y las 
plazas disponibles.
Registrar una reserva: Permitir que un usuario registre su nombre en una 
clase, verificando si aún hay plazas disponibles.
Cancelar una reserva: Permitir que un usuario cancele su reserva, 
liberando una plaza en la clase correspondiente.
Ver reservas de un usuario: Mostrar todas las clases en las que un 
usuario específico está registrado.
Estadísticas de ocupación: Calcular el porcentaje de ocupación por 
clase y mostrar cuáles están a punto de llenarse (menos de 3 plazas disponibles).
Requisitos adicionales:
Las clases se deben organizar por fecha y hora para que siempre se muestren 
en orden cronológico.
Si un usuario intenta registrarse en una clase que ya está llena, se debe 
mostrar un mensaje indicando que no hay plazas disponibles.
Implementa una funcionalidad para listar las clases más populares 
(con mayor porcentaje de ocupación).
'''

from datetime import datetime

# Lista de clases disponibles
clases = [
    {"nombre": "Yoga", "fecha_hora": "2024-12-05 18:00", "capacidad": 20, "reservas": [], "lista_espera": []},
    {"nombre": "Spinning", "fecha_hora": "2024-12-06 19:00", "capacidad": 15, "reservas": [], "lista_espera": []},
    {"nombre": "CrossFit", "fecha_hora": "2024-12-07 17:00", "capacidad": 20, "reservas": [], "lista_espera": []},
]

# Mostrar las clases disponibles
def mostrar_clases():
    print("\nClases Disponibles:")
    for i, clase in enumerate(clases, 1):
        ocupacion = len(clase["reservas"]) / clase["capacidad"] * 100
        print(f"{i}. {clase['nombre']} - Fecha: {clase['fecha_hora']}, "
              f"Plazas disponibles: {clase['capacidad'] - len(clase['reservas'])}/{clase['capacidad']} "
              f"({ocupacion:.0f}% ocupación)")

# Registrar una reserva
def registrar_reserva(nombre_usuario, indice_clase):
    clase = clases[indice_clase - 1]
    if len(clase["reservas"]) < clase["capacidad"]:
        clase["reservas"].append({"nombre_usuario": nombre_usuario, "estado": "confirmada"})
        print(f"\nReserva confirmada para {nombre_usuario} en la clase {clase['nombre']}.")
    else:
        print(f"\nLa clase {clase['nombre']} está llena.")
        respuesta = input("¿Desea unirse a la lista de espera? (S/N): ").strip().upper()
        if respuesta == "S":
            clase["lista_espera"].append(nombre_usuario)
            print(f"{nombre_usuario} ha sido añadido a la lista de espera para {clase['nombre']}.")

# Cancelar una reserva
def cancelar_reserva(nombre_usuario, indice_clase):
    clase = clases[indice_clase - 1]
    for reserva in clase["reservas"]:
        if reserva["nombre_usuario"] == nombre_usuario:
            clase["reservas"].remove(reserva)
            print(f"\nReserva cancelada para {nombre_usuario} en la clase {clase['nombre']}.")
            if clase["lista_espera"]:
                siguiente_usuario = clase["lista_espera"].pop(0)
                clase["reservas"].append({"nombre_usuario": siguiente_usuario, "estado": "confirmada"})
                print(f"\n¡Plaza reasignada automáticamente a {siguiente_usuario} de la lista de espera!")
            return
    print(f"\nNo se encontró una reserva para {nombre_usuario} en la clase {clase['nombre']}.")

# Mostrar las reservas de un usuario
def mostrar_reservas_usuario(nombre_usuario):
    print(f"\nReservas de {nombre_usuario}:")
    encontrado = False
    for clase in clases:
        for reserva in clase["reservas"]:
            if reserva["nombre_usuario"] == nombre_usuario:
                print(f"- {clase['nombre']} - {clase['fecha_hora']} (Estado: {reserva['estado']})")
                encontrado = True
    if not encontrado:
        print("No tiene reservas registradas.")

# Mostrar estadísticas de ocupación
def estadisticas_clases():
    print("\nEstadísticas de ocupación:")
    for clase in clases:
        ocupacion = len(clase["reservas"]) / clase["capacidad"] * 100
        print(f"{clase['nombre']} - Ocupación: {ocupacion:.0f}% "
              f"(Plazas disponibles: {clase['capacidad'] - len(clase['reservas'])})")

# Menú principal
def menu():
    while True:
        print("\n¿Qué desea hacer?")
        print("1. Mostrar todas las clases")
        print("2. Registrar una reserva")
        print("3. Cancelar una reserva")
        print("4. Consultar mis reservas")
        print("5. Ver estadísticas de clases")
        print("6. Salir")
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            mostrar_clases()
        elif opcion == "2":
            mostrar_clases()
            try:
                indice = int(input("\nSeleccione el número de la clase: "))
                nombre = input("Ingrese su nombre: ").strip()
                registrar_reserva(nombre, indice)
            except (ValueError, IndexError):
                print("Selección inválida.")
        elif opcion == "3":
            mostrar_clases()
            try:
                indice = int(input("\nSeleccione el número de la clase: "))
                nombre = input("Ingrese su nombre: ").strip()
                cancelar_reserva(nombre, indice)
            except (ValueError, IndexError):
                print("Selección inválida.")
        elif opcion == "4":
            nombre = input("\nIngrese su nombre: ").strip()
            mostrar_reservas_usuario(nombre)
        elif opcion == "5":
            estadisticas_clases()
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema de reservas del gimnasio!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()

