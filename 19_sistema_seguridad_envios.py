'''
Sistema de Seguimiento de Envíos

El programa permitirá:

Registrar nuevos paquetes con detalles como destinatario, 
dirección y estado del envío.
Actualizar el estado de un paquete en cualquier momento.
Consultar el historial completo de paquetes registrados.
Filtrar paquetes por estado (pendiente, en tránsito, entregado).
Exportar los datos a un archivo CSV para seguimiento externo.
'''

import csv

# Función para registrar un nuevo paquete
def registrar_paquete(envios):
    id_paquete = len(envios) + 1
    destinatario = input("Introduce el nombre del destinatario: ")
    direccion = input("Introduce la dirección del destinatario: ")
    estado = "Pendiente"  # Estado inicial por defecto
    envios.append({"id": id_paquete, "destinatario": destinatario, "direccion": direccion, "estado": estado})
    print(f"✅ Paquete {id_paquete} registrado correctamente.")

# Función para mostrar todos los paquetes
def mostrar_envios(envios):
    if not envios:
        print("\n📦 No hay paquetes registrados.")
        return

    print("\n--- Lista de Paquetes ---")
    for envio in envios:
        print(f"ID: {envio['id']} | Destinatario: {envio['destinatario']} | Dirección: {envio['direccion']} | Estado: {envio['estado']}")
    print("-------------------------")

# Función para actualizar el estado de un paquete
def actualizar_estado(envios):
    try:
        id_paquete = int(input("Introduce el ID del paquete que deseas actualizar: "))
        paquete = next((envio for envio in envios if envio["id"] == id_paquete), None)

        if paquete:
            print(f"Estado actual: {paquete['estado']}")
            nuevo_estado = input("Introduce el nuevo estado (Pendiente, En tránsito, Entregado): ").capitalize()
            if nuevo_estado in ["Pendiente", "En tránsito", "Entregado"]:
                paquete["estado"] = nuevo_estado
                print(f"✅ Estado del paquete {id_paquete} actualizado a '{nuevo_estado}'.")
            else:
                print("❌ Estado no válido. Intenta nuevamente.")
        else:
            print("❌ Paquete no encontrado.")
    except ValueError:
        print("❌ El ID debe ser un número.")

# Función para filtrar envíos por estado
def filtrar_envios(envios):
    estado_filtro = input("Introduce el estado para filtrar (Pendiente, En tránsito, Entregado): ").capitalize()
    envios_filtrados = [envio for envio in envios if envio["estado"] == estado_filtro]

    if envios_filtrados:
        print(f"\n--- Paquetes con estado '{estado_filtro}' ---")
        for envio in envios_filtrados:
            print(f"ID: {envio['id']} | Destinatario: {envio['destinatario']} | Dirección: {envio['direccion']} | Estado: {envio['estado']}")
        print("---------------------------------------------")
    else:
        print(f"❌ No se encontraron paquetes con estado '{estado_filtro}'.")

# Función para buscar envíos por destinatario o dirección
def buscar_envios(envios):
    criterio = input("Introduce el destinatario o dirección para buscar: ").lower()
    resultados = [envio for envio in envios if criterio in envio["destinatario"].lower() or criterio in envio["direccion"].lower()]

    if resultados:
        print(f"\n--- Resultados de la búsqueda para '{criterio}' ---")
        for envio in resultados:
            print(f"ID: {envio['id']} | Destinatario: {envio['destinatario']} | Dirección: {envio['direccion']} | Estado: {envio['estado']}")
        print("---------------------------------------------------")
    else:
        print(f"❌ No se encontraron resultados para '{criterio}'.")

# Función para exportar envíos a un archivo CSV
def exportar_a_csv(envios, archivo):
    try:
        with open(archivo, "w", newline="") as file:
            escritor = csv.DictWriter(file, fieldnames=["id", "destinatario", "direccion", "estado"])
            escritor.writeheader()
            escritor.writerows(envios)
        print(f"✅ Envíos exportados correctamente a '{archivo}'.")
    except Exception as e:
        print(f"❌ Error al exportar el archivo: {e}")

# Menú principal
def sistema_seguimiento():
    envios = []
    print("📦 Sistema de Seguimiento de Envíos 📦")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar un nuevo paquete")
        print("2. Mostrar todos los paquetes")
        print("3. Actualizar estado de un paquete")
        print("4. Filtrar paquetes por estado")
        print("5. Buscar envíos por destinatario o dirección")
        print("6. Exportar envíos a archivo CSV")
        print("7. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_paquete(envios)
        elif opcion == "2":
            mostrar_envios(envios)
        elif opcion == "3":
            actualizar_estado(envios)
        elif opcion == "4":
            filtrar_envios(envios)
        elif opcion == "5":
            buscar_envios(envios)
        elif opcion == "6":
            archivo = input("Introduce el nombre del archivo CSV (incluye la extensión .csv): ")
            exportar_a_csv(envios, archivo)
        elif opcion == "7":
            print("👋 ¡Gracias por usar el sistema de seguimiento! Hasta pronto.")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

# Ejecutar el programa
sistema_seguimiento()

