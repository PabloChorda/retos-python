'''
Crea un programa para gestionar el registro de usuarios en un evento. Podrás realizar 
operaciones como añadir usuarios, actualizar su información, eliminar usuarios y mostrar un listado de participantes registrados.

Cada usuario tiene los siguientes datos:

Nombre
Edad
Email
Tipo de entrada (general, VIP, o estudiante)
'''

# Lista de usuarios registrados
usuarios = []

# 1. Mostrar todos los usuarios registrados
def mostrar_usuarios():
    if not usuarios:
        print("\nNo hay usuarios registrados todavía.")
    else:
        print("\nUsuarios registrados:")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. Nombre: {usuario['nombre']} | Edad: {usuario['edad']} | Email: {usuario['email']} | Entrada: {usuario['entrada']}")

# 2. Registrar un nuevo usuario
def registrar_usuario(nombre, edad, email, entrada):
    nuevo_usuario = {"nombre": nombre, "edad": edad, "email": email, "entrada": entrada}
    usuarios.append(nuevo_usuario)
    print(f"\nUsuario '{nombre}' registrado con éxito.")

# 3. Actualizar la información de un usuario
def actualizar_usuario(email, nuevo_nombre=None, nueva_edad=None, nueva_entrada=None):
    for usuario in usuarios:
        if usuario["email"] == email:
            if nuevo_nombre:
                usuario["nombre"] = nuevo_nombre
            if nueva_edad:
                usuario["edad"] = nueva_edad
            if nueva_entrada:
                usuario["entrada"] = nueva_entrada
            print(f"\nUsuario con email '{email}' actualizado con éxito.")
            return
    print(f"\nNo se encontró un usuario con el email '{email}'.")

# 4. Eliminar un usuario
def eliminar_usuario(email):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario["email"] != email]
    print(f"\nUsuario con email '{email}' eliminado (si existía).")

# 5. Buscar usuario por email
def buscar_usuario(email):
    for usuario in usuarios:
        if usuario["email"] == email:
            print(f"\nUsuario encontrado: Nombre: {usuario['nombre']} | Edad: {usuario['edad']} | Email: {usuario['email']} | Entrada: {usuario['entrada']}")
            return
    print(f"\nNo se encontró un usuario con el email '{email}'.")

# 6. Contar usuarios por tipo de entrada
def contar_usuarios_por_tipo():
    tipos = {"general": 0, "VIP": 0, "estudiante": 0}
    for usuario in usuarios:
        if usuario["entrada"] in tipos:
            tipos[usuario["entrada"]] += 1
    print("\nUsuarios por tipo de entrada:")
    for tipo, cantidad in tipos.items():
        print(f"{tipo.capitalize()}: {cantidad}")

# Ejemplo de uso
registrar_usuario("Juan Pérez", 25, "juan.perez@gmail.com", "general")
registrar_usuario("Ana López", 30, "ana.lopez@gmail.com", "VIP")
registrar_usuario("Carlos Gómez", 20, "carlos.gomez@gmail.com", "estudiante")
mostrar_usuarios()
actualizar_usuario("ana.lopez@gmail.com", nueva_edad=31)
buscar_usuario("juan.perez@gmail.com")
eliminar_usuario("carlos.gomez@gmail.com")
contar_usuarios_por_tipo()
