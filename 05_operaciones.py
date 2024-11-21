''' EJERCICIO:
Crea un programa que explore diferentes operaciones que se pueden 
realizar con listas en tu lenguaje de programación. Algunas operaciones 
posibles son:

Indexación, slicing, adición, eliminación, búsqueda, ordenación, inversión, conteo de elementos, comprobación de unicidad, concatenación y copia.
Trabaja con listas anidadas e intenta modificar elementos dentro de estas.

'''

# Crear listas
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

# Concatenación
lista_concatenada = lista1 + lista2
print("Concatenación:", lista_concatenada)

# Indexación
print("Primer elemento de lista1:", lista1[0])

# Slicing
print("Últimos dos elementos de lista2:", lista2[-2:])

# Adición y eliminación
lista1.append(5)
print("Lista1 después de agregar 5:", lista1)
lista1.remove(3)
print("Lista1 después de eliminar 3:", lista1)

# Búsqueda y conteo
print("¿5 está en lista1?", 5 in lista1)
print("Cantidad de veces que aparece 4 en lista2:", lista2.count(4))

# Ordenar e invertir
lista2.sort()
print("Lista2 ordenada:", lista2)
lista2.reverse()
print("Lista2 invertida:", lista2)

# Listas anidadas
lista_anidada = [lista1, lista2]
print("Elemento de lista anidada:", lista_anidada[0][2])

# Copia de lista
lista_copia = lista1[:]
lista_copia.append(6)
print("Lista copia:", lista_copia)
print("Lista original:", lista1)
