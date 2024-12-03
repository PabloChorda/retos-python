'''
Crea un programa para gestionar los pedidos de un negocio local con 
entregas a domicilio. Podrás realizar operaciones como registrar nuevos 
pedidos, asignar repartidores, actualizar el estado de los pedidos y 
alcular estadísticas clave, como el tiempo promedio de entrega.

Cada pedido tiene los siguientes datos:

Cliente: Nombre del cliente que realizó el pedido.
Producto: Producto solicitado (ejemplo: "Pizza Margarita").
Estado: Puede ser pendiente, en camino o entregado.
Repartidor: Nombre del repartidor asignado al pedido (opcional al momento 
del registro).
Hora: Fecha y hora en que se registró el pedido.
Tu programa debe incluir las siguientes funcionalidades:

Mostrar todos los pedidos registrados: Listar todos los pedidos, mostrando el estado actual y el repartidor asignado (si lo hay).
Registrar un nuevo pedido: Permitir registrar un pedido nuevo solicitando los datos necesarios.
Asignar un repartidor: Asignar un repartidor a un pedido pendiente. Al asignar, el estado debe cambiar a en camino.
Actualizar el estado de un pedido: Permitir cambiar el estado de un pedido a pendiente, en camino o entregado.
Calcular el tiempo promedio de entrega: Mostrar el tiempo promedio que tardan los pedidos en ser entregados (considerando solo los pedidos marcados como entregado).
Buscar pedidos por repartidor: Mostrar todos los pedidos asignados a un repartidor específico.
'''
from datetime import datetime, timedelta

# Lista de pedidos
pedidos = []

# 1. Mostrar todos los pedidos
def mostrar_pedidos():
    if not pedidos:
        print("\nNo hay pedidos registrados todavía.")
    else:
        print("\nPedidos registrados:")
        for i, pedido in enumerate(pedidos, start=1):
            print(f"{i}. Cliente: {pedido['cliente']} | Producto: {pedido['producto']} | Estado: {pedido['estado']} | Repartidor: {pedido['repartidor']} | Hora: {pedido['hora']}")

# 2. Registrar un nuevo pedido
def registrar_pedido(cliente, producto):
    nuevo_pedido = {
        "cliente": cliente,
        "producto": producto,
        "estado": "pendiente",
        "repartidor": None,
        "hora": datetime.now()
    }
    pedidos.append(nuevo_pedido)
    print(f"\nPedido de '{producto}' para '{cliente}' registrado con éxito.")

# 3. Asignar un repartidor a un pedido
def asignar_repartidor(cliente, repartidor):
    for pedido in pedidos:
        if pedido["cliente"] == cliente and pedido["estado"] == "pendiente":
            pedido["repartidor"] = repartidor
            pedido["estado"] = "en camino"
            print(f"\nRepartidor '{repartidor}' asignado al pedido de '{cliente}'.")
            return
    print(f"\nNo se encontró un pedido pendiente para el cliente '{cliente}'.")

# 4. Actualizar el estado de un pedido
def actualizar_estado(cliente, nuevo_estado):
    for pedido in pedidos:
        if pedido["cliente"] == cliente:
            pedido["estado"] = nuevo_estado
            if nuevo_estado == "entregado":
                pedido["hora_entrega"] = datetime.now()
            print(f"\nEl estado del pedido de '{cliente}' se actualizó a '{nuevo_estado}'.")
            return
    print(f"\nNo se encontró un pedido para el cliente '{cliente}'.")

# 5. Calcular tiempo promedio de entrega
def tiempo_promedio_entrega():
    tiempos = []
    for pedido in pedidos:
        if pedido["estado"] == "entregado" and "hora_entrega" in pedido:
            tiempo = (pedido["hora_entrega"] - pedido["hora"]).seconds
            tiempos.append(tiempo)
    
    if tiempos:
        promedio = sum(tiempos) // len(tiempos)
        print(f"\nEl tiempo promedio de entrega es de {promedio // 60} minutos.")
    else:
        print("\nNo hay suficientes pedidos entregados para calcular el promedio.")

# 6. Buscar pedidos por repartidor
def buscar_pedidos_por_repartidor(repartidor):
    pedidos_repartidor = [p for p in pedidos if p["repartidor"] == repartidor]
    if pedidos_repartidor:
        print(f"\nPedidos asignados a '{repartidor}':")
        for pedido in pedidos_repartidor:
            print(f"Cliente: {pedido['cliente']} | Producto: {pedido['producto']} | Estado: {pedido['estado']} | Hora: {pedido['hora']}")
    else:
        print(f"\nNo se encontraron pedidos asignados a '{repartidor}'.")

# Ejemplo de uso
registrar_pedido("Juan", "Pizza Margarita")
registrar_pedido("Ana", "Hamburguesa Doble")
registrar_pedido("Luis", "Ensalada César")

asignar_repartidor("Juan", "Carlos")
asignar_repartidor("Ana", "Sofía")

actualizar_estado("Juan", "entregado")
mostrar_pedidos()

tiempo_promedio_entrega()
buscar_pedidos_por_repartidor("Sofía")
