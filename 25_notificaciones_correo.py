'''
Sistema de Gestión de Notificaciones por Correo

Crea un programa en Python que permita a una empresa gestionar el envío de 
notificaciones por correo electrónico a sus clientes. El sistema debe ofrecer las siguientes funcionalidades:

Registrar Clientes: El usuario podrá registrar clientes ingresando su nombre, dirección de correo electrónico 
y tipo de notificación preferida (promociones, recordatorios, boletines, etc.).

Ver Lista de Clientes: Mostrar una lista completa de clientes registrados con toda su información.

Enviar Notificaciones: El programa debe simular el envío de un correo a los clientes según el tipo de notificación seleccionada. 
Se imprimirá un mensaje indicando el destinatario, tipo de notificación y el estado del envío.

Eliminar Clientes: Permitir eliminar clientes de la lista en caso de que ya no deseen recibir notificaciones.

Actualizar Información del Cliente: Ofrecer la opción de modificar los datos de un cliente, 
como el correo electrónico o el tipo de notificación preferida.

Salir del Programa: Finalizar el programa.

El sistema debe validar los datos ingresados por el usuario 
(como formato correcto de correo electrónico) y manejar errores como la selección de opciones 
incorrectas o el intento de operar con un cliente inexistente.
Este programa debe ser interactivo y ejecutarse en la terminal, mostrando un menú con las opciones 
mencionadas para que el usuario pueda navegar fácilmente por sus funcionalidades.
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def menu_principal():
    print("\n=== GESTIÓN DE NOTIFICACIONES POR CORREO ===")
    print("1. Configurar datos de envío de correo")
    print("2. Enviar notificación a un destinatario")
    print("3. Ver historial de notificaciones enviadas")
    print("4. Salir")

# Variables globales
configuracion_correo = {
    "servidor": "",
    "puerto": 0,
    "correo": "",
    "contraseña": ""
}

historial_notificaciones = []

def configurar_envio():
    print("\n=== CONFIGURACIÓN DE ENVÍO ===")
    configuracion_correo["servidor"] = input("Ingrese el servidor SMTP (e.g., smtp.gmail.com): ")
    configuracion_correo["puerto"] = int(input("Ingrese el puerto SMTP (e.g., 587): "))
    configuracion_correo["correo"] = input("Ingrese su dirección de correo electrónico: ")
    configuracion_correo["contraseña"] = input("Ingrese su contraseña de correo electrónico: ")
    print("Configuración guardada exitosamente.")

def enviar_notificacion():
    print("\n=== ENVÍO DE NOTIFICACIÓN ===")
    destinatario = input("Ingrese el correo del destinatario: ")
    asunto = input("Ingrese el asunto del mensaje: ")
    cuerpo = input("Ingrese el cuerpo del mensaje: ")

    try:
        # Crear el mensaje
        mensaje = MIMEMultipart()
        mensaje["From"] = configuracion_correo["correo"]
        mensaje["To"] = destinatario
        mensaje["Subject"] = asunto
        mensaje.attach(MIMEText(cuerpo, "plain"))

        # Conectar al servidor SMTP y enviar el correo
        servidor = smtplib.SMTP(configuracion_correo["servidor"], configuracion_correo["puerto"])
        servidor.starttls()
        servidor.login(configuracion_correo["correo"], configuracion_correo["contraseña"])
        servidor.sendmail(configuracion_correo["correo"], destinatario, mensaje.as_string())
        servidor.quit()

        # Guardar en el historial
        historial_notificaciones.append({
            "destinatario": destinatario,
            "asunto": asunto,
            "cuerpo": cuerpo
        })

        print("Notificación enviada exitosamente.")
    except Exception as e:
        print(f"Error al enviar la notificación: {e}")

def ver_historial():
    print("\n=== HISTORIAL DE NOTIFICACIONES ===")
    if not historial_notificaciones:
        print("No se han enviado notificaciones aún.")
        return

    for i, notificacion in enumerate(historial_notificaciones, 1):
        print(f"\nNotificación {i}:")
        print(f"Destinatario: {notificacion['destinatario']}")
        print(f"Asunto: {notificacion['asunto']}")
        print(f"Cuerpo: {notificacion['cuerpo']}")

while True:
    menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        configurar_envio()
    elif opcion == "2":
        enviar_notificacion()
    elif opcion == "3":
        ver_historial()
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
