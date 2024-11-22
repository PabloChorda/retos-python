
'''
Aquí tienes un ejercicio más desafiante, que requiere lógica y manejo de estructuras de datos:

EJERCICIO:
Crea un programa que simule un sistema de votación. El programa debe:

Permitir que los usuarios ingresen el nombre de los candidatos (mínimo 2 candidatos).
Realizar una votación simulada con n votos (donde n es ingresado por el usuario). 
Cada voto se asignará aleatoriamente a uno de los candidatos.
Mostrar al final:
El número total de votos que recibió cada candidato.
El candidato ganador.
Si hubo empate, muestra los candidatos empatados.

'''

import random

def iniciar_votacion():
    print("=== SISTEMA DE VOTACIÓN ===")
    
    # Solicitar nombres de los candidatos
    candidatos = []
    while len(candidatos) < 2:
        candidato = input("Introduce el nombre de un candidato (mínimo 2): ").strip()
        if candidato and candidato not in candidatos:
            candidatos.append(candidato)
        else:
            print("El nombre es inválido o ya está en la lista.")
    
    # Solicitar número de votos
    while True:
        try:
            n_votos = int(input("Introduce el número de votos a simular: "))
            if n_votos > 0:
                break
            else:
                print("El número debe ser mayor a 0.")
        except ValueError:
            print("Introduce un número válido.")
    
    # Simular votación
    votos = {candidato: 0 for candidato in candidatos}
    for _ in range(n_votos):
        voto = random.choice(candidatos)
        votos[voto] += 1
    
    # Mostrar resultados
    print("\n=== RESULTADOS ===")
    for candidato, total in votos.items():
        print(f"{candidato}: {total} votos")
    
    # Determinar ganador
    max_votos = max(votos.values())
    ganadores = [candidato for candidato, total in votos.items() if total == max_votos]
    
    if len(ganadores) > 1:
        print("\nEmpate entre los candidatos: " + ", ".join(ganadores))
    else:
        print(f"\nEl ganador es: {ganadores[0]} con {max_votos} votos.")

# Ejecutar el programa
if __name__ == "__main__":
    iniciar_votacion()
