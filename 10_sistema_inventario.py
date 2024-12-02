'''
Crea un programa que permita gestionar un inventario de productos 
en una tienda. Deberás realizar las siguientes operaciones con un diccionario que represente el inventario:

Mostrar el inventario actual: Cada producto tiene un nombre, un precio y una cantidad disponible.
Agregar nuevos productos al inventario.
Actualizar el stock de un producto existente.
Eliminar un producto del inventario.
Buscar información de un producto específico.
Listar todos los productos disponibles y calcular el valor total del inventario.
'''

# Inventario inicial
inventario = {
    "manzanas": {"precio": 1.2, "cantidad": 50},
    "naranjas": {"precio": 0.8, "cantidad": 30},
    "plátanos": {"precio": 0.5, "cantidad": 100},
}

# 1. Mostrar el inventario actual
def mostrar_inventario():
    print("\nInventario actual:")
    for producto, datos in inventario.items():
        print(f"{producto.capitalize()} - Precio: {datos['precio']}€ | Cantidad: {datos['cantidad']} unidades")

# 2. Agregar un nuevo producto
def agregar_producto(nombre, precio, cantidad):
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe. Usa la función de actualización.")
    else:
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}
        print(f"Producto '{nombre}' agregado al inventario.")

# 3. Actualizar el stock de un producto existente
def actualizar_producto(nombre, nueva_cantidad):
    if nombre in inventario:
        inventario[nombre]["cantidad"] += nueva_cantidad
        print(f"Cantidad de '{nombre}' actualizada a {inventario[nombre]['cantidad']} unidades.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

# 4. Eliminar un producto
def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

# 5. Buscar información de un producto específico
def buscar_producto(nombre):
    if nombre in inventario:
        datos = inventario[nombre]
        print(f"{nombre.capitalize()} - Precio: {datos['precio']}€ | Cantidad: {datos['cantidad']} unidades")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")

# 6. Calcular el valor total del inventario
def calcular_valor_total():
    total = sum(datos["precio"] * datos["cantidad"] for datos in inventario.values())
    print(f"\nValor total del inventario: {total:.2f}€")

# Ejemplo de uso
mostrar_inventario()
agregar_producto("peras", 1.5, 40)
actualizar_producto("manzanas", 20)
eliminar_producto("naranjas")
buscar_producto("plátanos")
calcular_valor_total()
