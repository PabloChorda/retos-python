'''

Simulador de Crecimiento Poblacional
Desarrolla un programa en Python que simule el crecimiento de una población en un período de tiempo determinado. 
El programa deberá permitir al usuario ingresar los siguientes parámetros:

Población inicial: Número de habitantes al inicio de la simulación.
Tasa de natalidad: Número de nacimientos por cada 100 habitantes al año (en porcentaje).
Tasa de mortalidad: Número de muertes por cada 100 habitantes al año (en porcentaje).
Tasa de migración: Cambio neto en la población debido a migración por cada 100 habitantes al año (en porcentaje).
Duración de la simulación: Cantidad de años a simular.
El programa debe mostrar la evolución de la población año a año y el total al finalizar el período de simulación. 
Además, incluirá validaciones para que los datos ingresados sean razonables (por ejemplo, no aceptar tasas negativas o duración negativa).

'''

def simulador_poblacion():
    print("=== Simulador de Crecimiento Poblacional ===")
    
    # Solicitar datos al usuario con validaciones
    while True:
        try:
            poblacion_inicial = int(input("Ingresa la población inicial: "))
            if poblacion_inicial <= 0:
                raise ValueError("La población inicial debe ser mayor a 0.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")
    
    while True:
        try:
            tasa_natalidad = float(input("Ingresa la tasa de natalidad (%): "))
            if tasa_natalidad < 0:
                raise ValueError("La tasa de natalidad no puede ser negativa.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")
    
    while True:
        try:
            tasa_mortalidad = float(input("Ingresa la tasa de mortalidad (%): "))
            if tasa_mortalidad < 0:
                raise ValueError("La tasa de mortalidad no puede ser negativa.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")
    
    while True:
        try:
            tasa_migracion = float(input("Ingresa la tasa de migración (%): "))
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")
    
    while True:
        try:
            anios_simulacion = int(input("Ingresa la duración de la simulación (en años): "))
            if anios_simulacion <= 0:
                raise ValueError("La duración debe ser mayor a 0.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")
    
    # Mostrar parámetros ingresados
    print("\nParámetros ingresados:")
    print(f"Población inicial: {poblacion_inicial}")
    print(f"Tasa de natalidad: {tasa_natalidad}%")
    print(f"Tasa de mortalidad: {tasa_mortalidad}%")
    print(f"Tasa de migración: {tasa_migracion}%")
    print(f"Duración de la simulación: {anios_simulacion} años\n")
    
    # Inicializar variables
    poblacion_actual = poblacion_inicial
    print("Año\tPoblación")
    print("-" * 20)
    
    # Simulación año a año
    for anio in range(1, anios_simulacion + 1):
        nacimientos = poblacion_actual * (tasa_natalidad / 100)
        muertes = poblacion_actual * (tasa_mortalidad / 100)
        migracion = poblacion_actual * (tasa_migracion / 100)
        poblacion_actual += nacimientos - muertes + migracion
        print(f"{anio}\t{int(poblacion_actual)}")
    
    # Resultado final
    print("\nResultado final:")
    print(f"Población total después de {anios_simulacion} años: {int(poblacion_actual)}")


# Ejecutar el simulador
if __name__ == "__main__":
    simulador_poblacion()
