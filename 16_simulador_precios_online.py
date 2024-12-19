'''
Simulador de Precios Dinámicos para un Mercado Online
Descripción:
Crea un programa que simule un mercado online donde los precios de los productos cambian dinámicamente según la demanda y la cantidad de stock disponible. El objetivo es manejar la oferta y demanda de productos de forma automática.

Requisitos del programa:

Productos iniciales:

Crea una lista de productos, cada uno con:
Nombre
Precio inicial
Stock disponible
Demanda inicial (valor entre 1 y 100, que representa qué tan popular es el producto)
Cálculo dinámico del precio:

Si la demanda aumenta (por encima de 70), el precio del producto debe subir un 10%.
Si la demanda disminuye (por debajo de 30), el precio debe bajar un 10%.
Si el stock llega a 0, mostrar que el producto está "agotado".
Interacción con el usuario:

El usuario puede:
Comprar productos (reduciendo el stock).
Consultar la lista actualizada de productos.
Finalizar el programa.
Simulación automática de demanda:

Cada vez que el usuario consulta la lista o compra un producto, la demanda de los productos debe cambiar aleatoriamente (aumentar o disminuir en un rango de 1-20).
Salida esperada: El programa debe mostrar claramente:

La lista de productos con sus precios y stock actualizados.
Mensajes dinámicos según las acciones del usuario (compra, agotado, cambios en precios, etc.).

'''

import random

# Definimos los productos iniciales
productos = [
    {"nombre": "Manzanas", "precio": 1.0, "stock": 50, "demanda": 50},
    {"nombre": "Leche", "precio": 1.5, "stock": 30, "demanda": 60},
    {"nombre": "Pan", "precio": 1.2, "stock": 40, "demanda": 40},
    {"nombre": "Huevos", "precio": 2.5, "stock": 20, "demanda": 70},
]

# Función para mostrar la lista de productos
def mostrar_productos():
    print("\n--- Lista de Productos ---")
    for idx, producto in enumerate(productos):
        estado = "Agotado" if producto["stock"] <= 0 else "Disponible"
        print(
            f"{idx + 1}. {producto['nombre']} - Precio: ${producto['precio']:.2f} - Stock: {producto['stock']} - Demanda: {producto['demanda']} ({estado})"
        )
    print("-------------------------")

# Función para ajustar precios en base a la demanda
def ajustar_precios():
    for producto in productos:
        if producto["demanda"] > 70:  # Alta demanda
            producto["precio"] *= 1.10
        elif producto["demanda"] < 30:  # Baja demanda
            producto["precio"] *= 0.90

# Función para cambiar la demanda aleatoriamente
def actualizar_demanda():
    for producto in productos:
        cambio = random.randint(-20, 20)
        producto["demanda"] = max(0, min(100, producto["demanda"] + cambio))

# Función para comprar productos
def comprar_producto():
    try:
        mostrar_productos()
        eleccion = int(input("¿Qué producto quieres comprar? (Introduce el número): ")) - 1
        if eleccion < 0 or eleccion >= len(productos):
            print("❌ Producto no válido.")
            return

        producto = productos[eleccion]
        if producto["stock"] <= 0:
            print(f"❌ Lo siento, {producto['nombre']} está agotado.")
            return

        cantidad = int(input(f"¿Cuántas unidades de {producto['nombre']} quieres comprar? "))
        if cantidad > producto["stock"]:
            print(f"❌ Solo hay {producto['stock']} unidades disponibles.")
            return

        # Reducir stock y mostrar mensaje
        producto["stock"] -= cantidad
        print(f"✅ Has comprado {cantidad} unidades de {producto['nombre']}. Gracias por tu compra.")
    except ValueError:
        print("❌ Entrada no válida. Intenta nuevamente.")

# Función principal para el simulador
def simulador_mercado():
    while True:
        print("\n--- Simulador de Mercado Online ---")
        print("1. Mostrar productos")
        print("2. Comprar producto")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            actualizar_demanda()
            ajustar_precios()
            mostrar_productos()
        elif opcion == "2":
            actualizar_demanda()
            ajustar_precios()
            comprar_producto()
        elif opcion == "3":
            print("👋 ¡Gracias por usar el simulador! Hasta pronto.")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

# Ejecutar el simulador
simulador_mercado()
