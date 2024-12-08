'''
Diseña un programa que simule un sistema de optimización de rutas para un servicio de reparto, ayudando a reducir costos y tiempo.

Funcionalidades Requeridas:
Registro de Pedidos:

Cada pedido debe incluir:
Dirección de entrega.
Hora de solicitud.
Prioridad (normal, urgente).
Opcionalmente, puedes usar una API de mapas (como Google Maps o OpenStreetMap) para geolocalizar direcciones reales.
Simulación de Repartidores:

Crear un número limitado de repartidores (ejemplo: 5).
Cada repartidor tiene un radio máximo de cobertura (ejemplo: 10 km desde su punto de inicio).
Un repartidor no puede aceptar más pedidos de los que pueda llevar en su vehículo (capacidad máxima).
Optimización de Rutas:

Calcular la ruta más corta para cada repartidor utilizando un algoritmo como Dijkstra o *A (A-star)**.
Considerar la prioridad de los pedidos (los urgentes se entregan primero).
Si no hay pedidos urgentes, optimizar para reducir la distancia total recorrida.
Reporte en Tiempo Real:

Mostrar el estado de cada repartidor:
Pedidos en curso.
Tiempo estimado para cada entrega.
Permitir consultar qué pedidos están siendo procesados y cuáles están pendientes.
Historial de Entregas:

Almacenar un registro de todas las entregas realizadas, incluyendo:
Tiempo total de la entrega.
Distancia recorrida.
Fecha y hora.

'''

import math

# Base de datos simulada
pedidos = []
repartidores = []

# Simulación de datos geográficos (coordenadas ficticias)
ciudad = {
    "Centro": (0, 0),
    "Norte": (0, 10),
    "Sur": (0, -10),
    "Este": (10, 0),
    "Oeste": (-10, 0),
    "Barrio 1": (5, 5),
    "Barrio 2": (-5, -5),
}

# Función para calcular distancia entre dos puntos (usando fórmula de Euclides)
def calcular_distancia(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Función para registrar un pedido
def registrar_pedido():
    print("\n--- Registrar Pedido ---")
    cliente = input("Nombre del cliente: ").strip()
    direccion = input(f"Dirección del pedido (opciones: {', '.join(ciudad.keys())}): ").strip()
    if direccion not in ciudad:
        print("Dirección no válida. Intente de nuevo.")
        return
    prioridad = input("Prioridad (normal/urgente): ").strip().lower()
    if prioridad not in ["normal", "urgente"]:
        print("Prioridad no válida. Use 'normal' o 'urgente'.")
        return
    pedido = {
        "cliente": cliente,
        "direccion": direccion,
        "coordenadas": ciudad[direccion],
        "prioridad": prioridad,
    }
    pedidos.append(pedido)
    print(f"Pedido de '{cliente}' registrado exitosamente.")

# Función para registrar repartidores
def registrar_repartidor():
    print("\n--- Registrar Repartidor ---")
    nombre = input("Nombre del repartidor: ").strip()
    if any(r["nombre"].lower() == nombre.lower() for r in repartidores):
        print("Este nombre de repartidor ya está registrado. Intente con otro.")
        return
    repartidor = {
        "nombre": nombre,
        "ubicacion": ciudad["Centro"],
        "pedidos": [],
    }
    repartidores.append(repartidor)
    print(f"Repartidor '{nombre}' registrado exitosamente.")

# Función para asignar pedidos a repartidores
def asignar_pedidos():
    print("\n--- Asignar Pedidos a Repartidores ---")
    if not pedidos:
        print("No hay pedidos pendientes.")
        return
    if not repartidores:
        print("No hay repartidores disponibles.")
        return

    # Ordenar pedidos por prioridad (urgentes primero)
    pedidos_ordenados = sorted(pedidos, key=lambda p: p["prioridad"] == "urgente", reverse=True)

    for pedido in pedidos_ordenados:
        mejor_opcion = None
        menor_distancia = float("inf")

        for repartidor in repartidores:
            distancia = calcular_distancia(repartidor["ubicacion"], pedido["coordenadas"])
            if distancia < menor_distancia:
                menor_distancia = distancia
                mejor_opcion = repartidor

        if mejor_opcion:
            mejor_opcion["pedidos"].append(pedido)
            mejor_opcion["ubicacion"] = pedido["coordenadas"]
            print(f"Pedido de '{pedido['cliente']}' asignado a {mejor_opcion['nombre']}.")
            pedidos.remove(pedido)
        else:
            print(f"No se pudo asignar el pedido de '{pedido['cliente']}'.")

# Función para mostrar el estado de repartidores
def estado_repartidores():
    print("\n--- Estado de Repartidores ---")
    if not repartidores:
        print("No hay repartidores registrados.")
        return
    for repartidor in repartidores:
        print(f"\nRepartidor: {repartidor['nombre']}")
        print(f"  Ubicación actual: {repartidor['ubicacion']}")
        if repartidor["pedidos"]:
            print("  Pedidos asignados:")
            for pedido in repartidor["pedidos"]:
                print(f"    - {pedido['cliente']} ({pedido['direccion']})")
        else:
            print("  Sin pedidos asignados.")

# Función para listar pedidos pendientes
def listar_pedidos_pendientes():
    print("\n--- Pedidos Pendientes ---")
    if not pedidos:
        print("No hay pedidos pendientes.")
        return
    for pedido in pedidos:
        print(f"- {pedido['cliente']} en {pedido['direccion']} (Prioridad: {pedido['prioridad']})")

# Menú principal
def menu():
    while True:
        print("\n--- Sistema de Optimización de Reparto ---")
        print("1. Registrar Pedido")
        print("2. Registrar Repartidor")
        print("3. Asignar Pedidos")
        print("4. Ver Estado de Repartidores")
        print("5. Listar Pedidos Pendientes")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_pedido()
        elif opcion == "2":
            registrar_repartidor()
        elif opcion == "3":
            asignar_pedidos()
        elif opcion == "4":
            estado_repartidores()
        elif opcion == "5":
            listar_pedidos_pendientes()
        elif opcion == "6":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
