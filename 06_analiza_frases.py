'''
EJERCICIO:
Crea un programa que lea una frase ingresada por el usuario y determine:

La palabra más larga de la frase.
La cantidad de palabras que contienen más de 5 letras.
Si todas las palabras de la frase son únicas (es decir, 
si no hay palabras repetidas).
'''

def analizar_frase(frase):
    palabras = frase.split()
    palabra_mas_larga = max(palabras, key=len)
    palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
    todas_unicas = len(palabras) == len(set(palabras))

    print(f"La palabra más larga es: {palabra_mas_larga}")
    print(f"Hay {len(palabras_largas)} palabras con más de 5 letras.")
    print("Todas las palabras son únicas." if todas_unicas else "Hay palabras repetidas.")

# Solicitar entrada al usuario
frase_usuario = input("Ingresa una frase: ")
analizar_frase(frase_usuario)
