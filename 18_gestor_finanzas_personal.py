'''
Análisis Financiero Personal
Este programa permitirá al usuario gestionar sus finanzas personales. 
Las funcionalidades incluyen:

Registrar ingresos y gastos.
Calcular el balance actual.
Mostrar estadísticas (gastos totales, ingresos totales).
Exportar el registro a un archivo CSV para un seguimiento externo.
'''

import csv

# Función para registrar una transacción (ingreso o gasto)
def registrar_transaccion(registro, tipo):
    monto = float(input(f"Introduce el monto del {'ingreso' if tipo == 'ingreso' else 'gasto'}: "))
    descripcion = input("Introduce una breve descripción: ")
    registro.append({"tipo": tipo, "monto": monto, "descripcion": descripcion})
    print(f"✅ {tipo.capitalize()} registrado correctamente.")

# Función para mostrar el balance actual
def mostrar_balance(registro):
    ingresos = sum(item["monto"] for item in registro if item["tipo"] == "ingreso")
    gastos = sum(item["monto"] for item in registro if item["tipo"] == "gasto")
    balance = ingresos - gastos

    print("\n--- Resumen Financiero ---")
    print(f"Total de ingresos: {ingresos:.2f}€")
    print(f"Total de gastos: {gastos:.2f}€")
    print(f"Balance actual: {balance:.2f}€")
    print("--------------------------")

# Función para mostrar el registro completo
def mostrar_registro(registro):
    if not registro:
        print("\n📒 No hay transacciones registradas.")
        return

    print("\n--- Registro de Transacciones ---")
    for i, item in enumerate(registro, 1):
        print(f"{i}. {item['tipo'].capitalize()} - {item['monto']:.2f}€ - {item['descripcion']}")
    print("---------------------------------")

# Función para exportar el registro a un archivo CSV
def exportar_a_csv(registro, archivo):
    try:
        with open(archivo, "w", newline="") as file:
            escritor = csv.DictWriter(file, fieldnames=["tipo", "monto", "descripcion"])
            escritor.writeheader()
            escritor.writerows(registro)
        print(f"✅ Registro exportado correctamente a '{archivo}'.")
    except Exception as e:
        print(f"❌ Error al exportar el archivo: {e}")

# Menú principal
def gestor_financiero():
    registro = []
    print("💰 Gestor Financiero Personal 💰")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar un ingreso")
        print("2. Registrar un gasto")
        print("3. Mostrar balance actual")
        print("4. Mostrar registro completo")
        print("5. Exportar registro a archivo CSV")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_transaccion(registro, "ingreso")
        elif opcion == "2":
            registrar_transaccion(registro, "gasto")
        elif opcion == "3":
            mostrar_balance(registro)
        elif opcion == "4":
            mostrar_registro(registro)
        elif opcion == "5":
            archivo = input("Introduce el nombre del archivo CSV (incluye la extensión .csv): ")
            exportar_a_csv(registro, archivo)
        elif opcion == "6":
            print("👋 ¡Gracias por usar el gestor financiero! Hasta pronto.")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

# Ejecutar el programa
gestor_financiero()
