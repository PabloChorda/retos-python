'''
Planificador de Rutinas Diarias
Este programa permite al usuario organizar sus tareas diarias 
y llevar un seguimiento de lo que ha completado y lo que queda pendiente.

Características Principales:
Agregar Tareas: Permite agregar una tarea con una descripción, categoría 
(trabajo, personal, salud, etc.), y un tiempo estimado de duración.
Marcar como Completa: El usuario puede marcar una tarea como completada.
Ver Rutina por Categorías: Mostrar las tareas organizadas por categorías 
(pendientes y completadas)
'''

from datetime import datetime

# Lista para almacenar las tareas
tareas = []

# Función para agregar una nueva tarea
def agregar_tarea():
    descripcion = input("📋 Describe la tarea: ").strip()
    if not descripcion:
        print("❌ La descripción no puede estar vacía.")
        return

    categoria = input("🏷️ Categoría (Ej: Trabajo, Personal, Salud): ").strip()
    if not categoria:
        print("❌ La categoría no puede estar vacía.")
        return

    try:
        duracion = int(input("⏱️ Tiempo estimado en minutos: "))
        if duracion <= 0:
            print("❌ La duración debe ser un número positivo.")
            return
        tarea = {
            "descripcion": descripcion,
            "categoria": categoria,
            "duracion": duracion,
            "completada": False,
            "fecha": datetime.now().strftime("%d/%m/%Y")
        }
        tareas.append(tarea)
        print("✅ Tarea agregada correctamente.")
    except ValueError:
        print("❌ Entrada no válida. Introduce un número para la duración.")

# Función para mostrar tareas por estado
def mostrar_tareas(pendientes=True):
    estado = "Pendientes" if pendientes else "Completadas"
    print(f"\n--- Tareas {estado} ---")
    tareas_filtradas = [tarea for tarea in tareas if tarea["completada"] != pendientes]
    
    if not tareas_filtradas:
        print(f"🔹 No hay tareas {estado.lower()}.")
        return

    for i, tarea in enumerate(tareas_filtradas, start=1):
        print(f"{i}. {tarea['descripcion']} - {tarea['categoria']} ({tarea['duracion']} min)")
    print("------------------------")

# Función para marcar una tarea como completada
def completar_tarea():
    mostrar_tareas(pendientes=True)
    try:
        indice = int(input("🔢 Introduce el número de la tarea a completar: ")) - 1
        tareas_pendientes = [tarea for tarea in tareas if not tarea["completada"]]

        if 0 <= indice < len(tareas_pendientes):
            tarea_seleccionada = tareas_pendientes[indice]
            tarea_seleccionada["completada"] = True
            print(f"✅ Tarea '{tarea_seleccionada['descripcion']}' marcada como completada.")
        else:
            print("❌ Número de tarea no válido.")
    except (ValueError, IndexError):
        print("❌ Entrada no válida. Introduce un número correcto.")

# Función para generar un resumen diario
def generar_resumen():
    total_completadas = sum(1 for tarea in tareas if tarea["completada"])
    total_pendientes = sum(1 for tarea in tareas if not tarea["completada"])
    tiempo_total = sum(tarea["duracion"] for tarea in tareas if tarea["completada"])

    print("\n--- Resumen Diario ---")
    print(f"✅ Tareas completadas: {total_completadas}")
    print(f"❌ Tareas pendientes: {total_pendientes}")
    print(f"⏱️ Tiempo total dedicado: {tiempo_total} minutos")
    print("----------------------")

# Menú principal
def planificador_rutinas():
    while True:
        print("\n--- Planificador de Rutinas Diarias ---")
        print("1. Agregar Tarea")
        print("2. Ver Tareas Pendientes")
        print("3. Ver Tareas Completadas")
        print("4. Completar Tarea")
        print("5. Generar Resumen Diario")
        print("6. Salir")

        opcion = input("🔢 Elige una opción: ").strip()
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas(pendientes=True)
        elif opcion == "3":
            mostrar_tareas(pendientes=False)
        elif opcion == "4":
            completar_tarea()
        elif opcion == "5":
            generar_resumen()
        elif opcion == "6":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    planificador_rutinas()
