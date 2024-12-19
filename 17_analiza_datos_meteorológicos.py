'''
Analizador de Datos Meteorológicos
Este programa permitirá al usuario analizar datos meteorológicos (como temperaturas, humedad, viento, etc.) de un archivo CSV. El programa ofrecerá funcionalidades como:

Cargar datos desde un archivo CSV.
Mostrar estadísticas básicas (media, máximo, mínimo).
Generar gráficos simples para visualizar tendencias (usando matplotlib).
Filtrar datos por rango de fechas.
'''

import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Función para cargar datos desde un archivo CSV
def cargar_datos(archivo):
    datos = []
    try:
        with open(archivo, "r") as file:
            lector = csv.DictReader(file)
            for fila in lector:
                datos.append({
                    "fecha": datetime.strptime(fila["Fecha"], "%Y-%m-%d"),
                    "temperatura": float(fila["Temperatura"]),
                    "humedad": float(fila["Humedad"]),
                    "viento": float(fila["Viento"])
                })
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo '{archivo}'.")
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
    return datos

# Función para mostrar estadísticas básicas
def mostrar_estadisticas(datos, clave):
    valores = [d[clave] for d in datos]
    print(f"\n--- Estadísticas para {clave.capitalize()} ---")
    print(f"Media: {sum(valores) / len(valores):.2f}")
    print(f"Mínimo: {min(valores):.2f}")
    print(f"Máximo: {max(valores):.2f}")
    print("--------------------------------")

# Función para generar un gráfico
def generar_grafico(datos, clave):
    fechas = [d["fecha"] for d in datos]
    valores = [d[clave] for d in datos]

    plt.figure(figsize=(10, 5))
    plt.plot(fechas, valores, marker="o", label=clave.capitalize())
    plt.title(f"Tendencia de {clave.capitalize()}")
    plt.xlabel("Fecha")
    plt.ylabel(clave.capitalize())
    plt.grid(True)
    plt.legend()
    plt.show()

# Función para filtrar datos por rango de fechas
def filtrar_por_fecha(datos, fecha_inicio, fecha_fin):
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    return [d for d in datos if fecha_inicio <= d["fecha"] <= fecha_fin]

# Menú principal
def simulador_datos_meteorologicos():
    print("🌤️ Analizador de Datos Meteorológicos 🌤️")
    archivo = input("Introduce el nombre del archivo CSV (incluyendo la extensión): ")

    # Cargar datos
    datos = cargar_datos(archivo)
    if not datos:
        return

    while True:
        print("\n--- Menú Principal ---")
        print("1. Mostrar estadísticas")
        print("2. Generar gráfico")
        print("3. Filtrar datos por fecha")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\n¿Qué estadística quieres ver?")
            print("1. Temperatura")
            print("2. Humedad")
            print("3. Viento")
            clave_opcion = input("Elige una opción: ")
            if clave_opcion == "1":
                mostrar_estadisticas(datos, "temperatura")
            elif clave_opcion == "2":
                mostrar_estadisticas(datos, "humedad")
            elif clave_opcion == "3":
                mostrar_estadisticas(datos, "viento")
            else:
                print("❌ Opción no válida.")

        elif opcion == "2":
            print("\n¿Qué gráfico quieres generar?")
            print("1. Temperatura")
            print("2. Humedad")
            print("3. Viento")
            clave_opcion = input("Elige una opción: ")
            if clave_opcion == "1":
                generar_grafico(datos, "temperatura")
            elif clave_opcion == "2":
                generar_grafico(datos, "humedad")
            elif clave_opcion == "3":
                generar_grafico(datos, "viento")
            else:
                print("❌ Opción no válida.")

        elif opcion == "3":
            fecha_inicio = input("Introduce la fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Introduce la fecha de fin (YYYY-MM-DD): ")
            datos_filtrados = filtrar_por_fecha(datos, fecha_inicio, fecha_fin)
            if datos_filtrados:
                print(f"\nDatos filtrados entre {fecha_inicio} y {fecha_fin}:")
                for d in datos_filtrados:
                    print(f"{d['fecha'].strftime('%Y-%m-%d')} - Temp: {d['temperatura']}°C, Hum: {d['humedad']}%, Viento: {d['viento']} km/h")
            else:
                print("❌ No se encontraron datos en ese rango de fechas.")

        elif opcion == "4":
            print("👋 ¡Gracias por usar el analizador! Hasta pronto.")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

# Ejecutar el programa
simulador_datos_meteorologicos()
