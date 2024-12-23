'''
Simulador de Préstamos Bancarios

Crea un programa en Python que permita a los usuarios simular 
y analizar diferentes opciones de préstamos bancarios. 
El simulador debe incluir las siguientes funcionalidades:

Cálculo de préstamos con interés simple: Calcular el monto total a pagar y las cuotas mensuales de un préstamo
 basado en interés simple.
Cálculo de préstamos con interés compuesto: Calcular el monto total a pagar y las cuotas mensuales de un préstamo basado
 en interés compuesto.
Comparación de préstamos: Comparar el costo total entre un préstamo con interés simple y otro con interés compuesto, 
considerando la misma cantidad de dinero y duración.

El programa debe ser interactivo y mostrar un menú principal para seleccionar las opciones. 
Además, debe manejar errores de entrada y garantizar que los cálculos sean precisos.
'''

import math

def menu_principal():
    print("\n=== SIMULADOR DE PRÉSTAMOS BANCARIOS ===")
    print("1. Calcular préstamo con interés simple")
    print("2. Calcular préstamo con interés compuesto")
    print("3. Comparar préstamos")
    print("4. Salir")

def calcular_interes_simple():
    monto = float(input("Ingrese el monto del préstamo: "))
    tasa_anual = float(input("Ingrese la tasa de interés anual (%): ")) / 100
    años = int(input("Ingrese la cantidad de años: "))

    interes_total = monto * tasa_anual * años
    monto_total = monto + interes_total
    cuota_mensual = monto_total / (años * 12)

    print(f"\nMonto total a pagar: {monto_total:.2f} EUR")
    print(f"Cuota mensual: {cuota_mensual:.2f} EUR")

def calcular_interes_compuesto():
    monto = float(input("Ingrese el monto del préstamo: "))
    tasa_anual = float(input("Ingrese la tasa de interés anual (%): ")) / 100
    años = int(input("Ingrese la cantidad de años: "))

    monto_total = monto * math.pow((1 + tasa_anual / 12), años * 12)
    cuota_mensual = monto_total / (años * 12)

    print(f"\nMonto total a pagar: {monto_total:.2f} EUR")
    print(f"Cuota mensual: {cuota_mensual:.2f} EUR")

def comparar_prestamos():
    print("\n=== COMPARACIÓN DE PRÉSTAMOS ===")
    monto = float(input("Ingrese el monto del préstamo: "))
    tasa_simple = float(input("Ingrese la tasa de interés anual para interés simple (%): ")) / 100
    tasa_compuesto = float(input("Ingrese la tasa de interés anual para interés compuesto (%): ")) / 100
    años = int(input("Ingrese la cantidad de años: "))

    interes_simple = monto * tasa_simple * años
    monto_simple = monto + interes_simple

    monto_compuesto = monto * math.pow((1 + tasa_compuesto / 12), años * 12)

    print(f"\nPréstamo con interés simple: {monto_simple:.2f} EUR")
    print(f"Préstamo con interés compuesto: {monto_compuesto:.2f} EUR")

    if monto_simple < monto_compuesto:
        print("El préstamo con interés simple es más económico.")
    else:
        print("El préstamo con interés compuesto es más económico.")

while True:
    menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        calcular_interes_simple()
    elif opcion == "2":
        calcular_interes_compuesto()
    elif opcion == "3":
        comparar_prestamos()
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
