"""
EJERCICIO:
- Diseña un programa para gestionar los pedidos de un restaurante.
- Cada pedido debe incluir:
  1. Nombre del cliente.
  2. Lista de platos (nombre y precio unitario).
  3. Cantidad de cada plato.
- Permite realizar las siguientes operaciones:
  1. Crear un nuevo pedido.
  2. Buscar un pedido por el nombre del cliente.
  3. Actualizar la cantidad de un plato en un pedido.
  4. Eliminar un plato de un pedido o cancelar el pedido completo.
  5. Mostrar todos los pedidos con sus respectivos totales.
DIFICULTAD EXTRA (opcional):
- Implementa una funcionalidad para aplicar un descuento a un pedido.
- Valida que los precios y cantidades sean números positivos.
- Proporciona una opción para calcular el total de ingresos acumulados del restaurante.
"""

def restaurant_orders():
    orders = {}

    def get_valid_name(prompt="Introduce el nombre del cliente: "):
        """Solicita un nombre válido (no vacío)."""
        while True:
            name = input(prompt).strip()
            if name:
                return name
            else:
                print("El nombre no puede estar vacío.")

    def get_valid_quantity():
        """Solicita una cantidad válida (entero positivo)."""
        while True:
            try:
                quantity = int(input("Introduce la cantidad: ").strip())
                if quantity > 0:
                    return quantity
                else:
                    print("La cantidad debe ser un número positivo.")
            except ValueError:
                print("Por favor, introduce un número entero válido.")

    def get_valid_price():
        """Solicita un precio válido (número positivo)."""
        while True:
            try:
                price = float(input("Introduce el precio unitario: ").strip())
                if price >= 0:
                    return price
                else:
                    print("El precio no puede ser negativo.")
            except ValueError:
                print("Por favor, introduce un número válido.")

    def create_order():
        """Crea un nuevo pedido para un cliente."""
        customer_name = get_valid_name()
        if customer_name in orders:
            print(f"Ya existe un pedido para el cliente '{customer_name}'.")
        else:
            orders[customer_name] = []
            while True:
                dish_name = get_valid_name("Introduce el nombre del plato: ")
                quantity = get_valid_quantity()
                price = get_valid_price()
                orders[customer_name].append({"dish": dish_name, "quantity": quantity, "price": price})
                print(f"Plato '{dish_name}' añadido al pedido de {customer_name}.")
                if input("¿Quieres añadir otro plato? (s/n): ").strip().lower() != "s":
                    break

    def search_order():
        """Busca un pedido por el nombre del cliente."""
        customer_name = get_valid_name()
        if customer_name in orders:
            print(f"Pedido de {customer_name}:")
            for item in orders[customer_name]:
                print(f"- {item['dish']}: {item['quantity']} unidades, {item['price']:.2f}€/unidad")
        else:
            print(f"No se encontró un pedido para el cliente '{customer_name}'.")

    def update_order():
        """Actualiza la cantidad de un plato en un pedido."""
        customer_name = get_valid_name()
        if customer_name in orders:
            dish_name = get_valid_name("Introduce el nombre del plato a actualizar: ")
            for item in orders[customer_name]:
                if item["dish"] == dish_name:
                    item["quantity"] = get_valid_quantity()
                    print(f"Cantidad del plato '{dish_name}' actualizada con éxito.")
                    return
            print(f"El plato '{dish_name}' no está en el pedido de {customer_name}.")
        else:
            print(f"No se encontró un pedido para el cliente '{customer_name}'.")

    def delete_order():
        """Elimina un plato de un pedido o un pedido completo."""
        customer_name = get_valid_name()
        if customer_name in orders:
            print("1. Eliminar un plato")
            print("2. Cancelar el pedido completo")
            option = input("Selecciona una opción: ").strip()
            if option == "1":
                dish_name = get_valid_name("Introduce el nombre del plato a eliminar: ")
                for item in orders[customer_name]:
                    if item["dish"] == dish_name:
                        orders[customer_name].remove(item)
                        print(f"Plato '{dish_name}' eliminado del pedido de {customer_name}.")
                        if not orders[customer_name]:
                            del orders[customer_name]
                            print(f"El pedido de {customer_name} ha sido cancelado (sin platos).")
                        return
                print(f"El plato '{dish_name}' no está en el pedido de {customer_name}.")
            elif option == "2":
                del orders[customer_name]
                print(f"Pedido de {customer_name} cancelado con éxito.")
            else:
                print("Opción no válida.")
        else:
            print(f"No se encontró un pedido para el cliente '{customer_name}'.")

    def show_orders():
        """Muestra todos los pedidos con sus totales."""
        if not orders:
            print("No hay pedidos registrados.")
            return
        total_income = 0
        print("\nPedidos actuales:")
        for customer_name, items in orders.items():
            print(f"\nPedido de {customer_name}:")
            order_total = 0
            for item in items:
                value = item["quantity"] * item["price"]
                order_total += value
                print(f"- {item['dish']}: {item['quantity']} unidades, {item['price']:.2f}€/unidad, Total: {value:.2f}€")
            print(f"Total del pedido: {order_total:.2f}€")
            total_income += order_total
        print(f"\nIngresos totales del restaurante: {total_income:.2f}€")

    def menu():
        """Muestra el menú y retorna la opción seleccionada."""
        print("\n1. Crear pedido")
        print("2. Buscar pedido")
        print("3. Actualizar pedido")
        print("4. Eliminar pedido")
        print("5. Mostrar todos los pedidos")
        print("6. Salir")
        return input("Selecciona una opción: ")

    while True:
        option = menu()

        match option:
            case "1":
                create_order()
            case "2":
                search_order()
            case "3":
                update_order()
            case "4":
                delete_order()
            case "5":
                show_orders()
            case "6":
                print("Saliendo del sistema de gestión de pedidos.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 6.")

restaurant_orders()
