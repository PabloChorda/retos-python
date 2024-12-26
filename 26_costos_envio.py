'''
Simulador de Costos de Envío

Desarrolla un programa en Python que calcule los costos de envío de paquetes basándose en diferentes factores. 
El sistema deberá permitir al usuario ingresar los detalles del paquete, como peso, dimensiones y destino, y calcular el costo total según las siguientes variables:

Peso del paquete:

Hasta 1 kg: tarifa base de 5 €.
De 1 kg a 5 kg: tarifa base de 10 €.
Más de 5 kg: tarifa base de 20 €.
Dimensiones del paquete:

Si alguna dimensión excede 1 metro, se cobrará un recargo de 10 €.
Destino:

Nacional: Sin recargo.
Europa: Recargo de 15 €.
Internacional: Recargo de 30 €.
Tipo de servicio:

Estándar: Sin recargo adicional.
Exprés: Recargo del 20% sobre el costo total.
El programa debe permitir al usuario:

Calcular los costos de un solo envío.
Ver un resumen de los envíos realizados (destino, peso, dimensiones y costo total).
Salir del programa.
Incluye validación de entradas para asegurar que el peso y las 
dimensiones sean números positivos.
'''

def menu_principal():
    print("\n=== SIMULADOR DE COSTOS DE ENVÍO ===")
    print("1. Calcular costo de envío")
    print("2. Ver resumen de envíos")
    print("3. Salir")

envios = []

def calcular_costo_envio():
    print("\n=== CALCULAR COSTO DE ENVÍO ===")
    
    try:
        peso = float(input("Ingrese el peso del paquete (kg): "))
        if peso <= 0:
            print("Error: El peso debe ser un número positivo.")
            return

        largo = float(input("Ingrese el largo del paquete (m): "))
        ancho = float(input("Ingrese el ancho del paquete (m): "))
        alto = float(input("Ingrese el alto del paquete (m): "))
        
        if largo <= 0 or ancho <= 0 or alto <= 0:
            print("Error: Todas las dimensiones deben ser números positivos.")
            return

        destino = input("Ingrese el destino (nacional, europa, internacional): ").lower()
        if destino not in ["nacional", "europa", "internacional"]:
            print("Error: Destino no válido.")
            return

        servicio = input("Ingrese el tipo de servicio (estándar, exprés): ").lower()
        if servicio not in ["estándar", "exprés"]:
            print("Error: Tipo de servicio no válido.")
            return

        # Cálculo del costo base según el peso
        if peso <= 1:
            costo_base = 5
        elif peso <= 5:
            costo_base = 10
        else:
            costo_base = 20

        # Recargo por dimensiones
        recargo_dimensiones = 10 if max(largo, ancho, alto) > 1 else 0

        # Recargo por destino
        if destino == "nacional":
            recargo_destino = 0
        elif destino == "europa":
            recargo_destino = 15
        else:  # internacional
            recargo_destino = 30

        # Costo total preliminar
        costo_total = costo_base + recargo_dimensiones + recargo_destino

        # Recargo por servicio exprés
        if servicio == "exprés":
            costo_total *= 1.2

        # Registro del envío
        envio = {
            "peso": peso,
            "dimensiones": (largo, ancho, alto),
            "destino": destino,
            "servicio": servicio,
            "costo_total": round(costo_total, 2)
        }
        envios.append(envio)

        print(f"\nCosto total del envío: {round(costo_total, 2)} €")
        print("Envío registrado exitosamente.")

    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

def ver_resumen_envios():
    print("\n=== RESUMEN DE ENVÍOS ===")
    if not envios:
        print("No hay envíos registrados.")
        return

    for i, envio in enumerate(envios, start=1):
        print(f"\nEnvío {i}:")
        print(f"  Peso: {envio['peso']} kg")
        print(f"  Dimensiones: {envio['dimensiones'][0]}m x {envio['dimensiones'][1]}m x {envio['dimensiones'][2]}m")
        print(f"  Destino: {envio['destino'].capitalize()}")
        print(f"  Servicio: {envio['servicio'].capitalize()}")
        print(f"  Costo total: {envio['costo_total']} €")

while True:
    menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        calcular_costo_envio()
    elif opcion == "2":
        ver_resumen_envios()
    elif opcion == "3":
        print("Saliendo del programa. ¡Gracias por usar el simulador!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
