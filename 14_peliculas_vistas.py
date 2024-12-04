'''
Crea un programa que permita gestionar un registro de películas vistas, junto con su calificación y estado. El sistema debe incluir:

Registrar una nueva película:

Nombre de la película.
Género.
Fecha en la que fue vista.
Calificación (del 1 al 10).
Actualizar la calificación de una película:

Cambiar la nota de una película previamente registrada.
Buscar películas por género:

Mostrar todas las películas de un género específico.
Mostrar estadísticas:

Promedio de calificaciones.
Película mejor calificada.
Película peor calificada.
Listar todas las películas:

Mostrar todos los datos de las películas registradas ordenadas por fecha vista.

'''

# Sistema de gestión de películas vistas

# Lista para almacenar las películas
peliculas = []

# Función para registrar una nueva película
def registrar_pelicula():
    print("\n--- Registrar Película ---")
    nombre = input("Nombre de la película: ").strip()
    genero = input("Género: ").strip()
    fecha = input("Fecha vista (YYYY-MM-DD): ").strip()
    calificacion = int(input("Calificación (1-10): ").strip())
    if calificacion < 1 or calificacion > 10:
        print("Calificación inválida. Debe estar entre 1 y 10.")
        return
    pelicula = {
        "nombre": nombre,
        "genero": genero,
        "fecha": fecha,
        "calificacion": calificacion
    }
    peliculas.append(pelicula)
    print(f"\nPelícula '{nombre}' registrada exitosamente.")

# Función para actualizar la calificación de una película
def actualizar_calificacion():
    print("\n--- Actualizar Calificación ---")
    nombre = input("Nombre de la película: ").strip()
    for pelicula in peliculas:
        if pelicula["nombre"].lower() == nombre.lower():
            nueva_calificacion = int(input(f"Nueva calificación para '{nombre}' (1-10): ").strip())
            if nueva_calificacion < 1 or nueva_calificacion > 10:
                print("Calificación inválida. Debe estar entre 1 y 10.")
                return
            pelicula["calificacion"] = nueva_calificacion
            print(f"Calificación actualizada para '{nombre}'.")
            return
    print(f"No se encontró la película '{nombre}'.")

# Función para buscar películas por género
def buscar_por_genero():
    print("\n--- Buscar Películas por Género ---")
    genero = input("Ingrese el género: ").strip()
    peliculas_genero = [p for p in peliculas if p["genero"].lower() == genero.lower()]
    if peliculas_genero:
        print(f"\nPelículas del género '{genero}':")
        for p in peliculas_genero:
            print(f"- {p['nombre']} ({p['fecha']}) - Calificación: {p['calificacion']}")
    else:
        print(f"No se encontraron películas del género '{genero}'.")

# Función para mostrar estadísticas
def mostrar_estadisticas():
    print("\n--- Estadísticas ---")
    if not peliculas:
        print("No hay películas registradas.")
        return
    promedio = sum(p["calificacion"] for p in peliculas) / len(peliculas)
    mejor = max(peliculas, key=lambda p: p["calificacion"])
    peor = min(peliculas, key=lambda p: p["calificacion"])
    print(f"Promedio de calificaciones: {promedio:.2f}")
    print(f"Película mejor calificada: {mejor['nombre']} ({mejor['calificacion']}/10)")
    print(f"Película peor calificada: {peor['nombre']} ({peor['calificacion']}/10)")

# Función para listar todas las películas
def listar_peliculas():
    print("\n--- Listar Todas las Películas ---")
    if not peliculas:
        print("No hay películas registradas.")
        return
    peliculas_ordenadas = sorted(peliculas, key=lambda p: p["fecha"])
    for p in peliculas_ordenadas:
        print(f"- {p['nombre']} ({p['fecha']}) - Género: {p['genero']} - Calificación: {p['calificacion']}")

# Menú principal
def menu():
    while True:
        print("\n¿Qué desea hacer?")
        print("1. Registrar una película")
        print("2. Actualizar calificación")
        print("3. Buscar películas por género")
        print("4. Mostrar estadísticas")
        print("5. Listar todas las películas")
        print("6. Salir")
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_pelicula()
        elif opcion == "2":
            actualizar_calificacion()
        elif opcion == "3":
            buscar_por_genero()
        elif opcion == "4":
            mostrar_estadisticas()
        elif opcion == "5":
            listar_peliculas()
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema de gestión de películas!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
