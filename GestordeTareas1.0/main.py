from scr.conexion import CConexion
from Tarea import Tarea
from usuario import Usuarios
from Recordatorio import Recordatorio
from datetime import datetime


def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            iniciar_sesion()
        elif opcion == '2':
            registrar_usuario()
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente nuevamente.")


def iniciar_sesion():
    correo = input("Digite su Correo: ")
    contrasena = input("Digite su contraseña: ")
    usuario = Usuarios()
    Id_usuario = usuario.login(correo, contrasena)
    if Id_usuario:
        menu_tareas(Id_usuario)


def registrar_usuario():
    nombre = input("Ingrese su nombre completo: ")
    correo = input("Ingrese su correo electrónico: ")
    contrasena = input("Ingrese una contraseña: ")
    confirmar_contrasena = input("Confirme su contraseña: ")

    if contrasena == confirmar_contrasena:
        usuario = Usuarios(nombre, correo, contrasena, confirmar_contrasena)
        usuario.registrarusuarios()
        print("Usuario registrado con éxito.")
    else:
        print("Las contraseñas no coinciden. Intente nuevamente.")


def menu_tareas(Id_usuario):
    while True:
        print("\n--- Menú de Tareas ---")
        print("1. Agregar tarea")
        print("2. Editar tarea")
        print("3. Agregar recordatorio para tarea")
        print("4. Eliminar tarea")
        print("5. Mostrar tareas")
        print("6. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_tarea(Id_usuario)
        elif opcion == '2':
            editar_tarea(Id_usuario)
        elif opcion == '3':
            agregar_recordatorio(Id_usuario)
        elif opcion == '4':
            eliminar_tarea(Id_usuario)
        elif opcion == '5':
            mostrar_tareas(Id_usuario)
        elif opcion == '6':
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida, intente nuevamente.")


def agregar_tarea(Id_usuario):
    print("Agregando tarea...")
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")

    try:
        fecha_vencimiento = pedir_fecha_vencimiento()
    except ValueError:
        print("Formato de fecha y hora de vencimiento no válido. Se omitirá la tarea.")
        return

    estado = input("Ingrese el estado (Completa, Incompleta, Pendiente): ")
    estadoM= estado.capitalize()
    prioridad = input("Ingrese el nivel de importancia del proyecto (Alta, Media, Baja): ")
    prioridadM =prioridad.capitalize()

    tarea = Tarea(titulo, descripcion, None, fecha_vencimiento, estadoM, prioridadM, Id_usuario, None)
    tarea.agregar_tarea()


def editar_tarea(Id_usuario):
    print("Editando tarea...")
    numero_tarea = input("Ingrese el número de la tarea: ")
    titulo_nuevo = input("Ingrese el nuevo título de la tarea: ")
    descripcion_nueva = input("Ingrese la nueva descripción de la tarea: ")

    while True:
        try:
            anio = int(input("Ingrese el año de vencimiento (YYYY): "))
            mes = int(input("Ingrese el mes de vencimiento (MM): "))
            dia = int(input("Ingrese el día de vencimiento (DD): "))
            hora = int(input("Ingrese la hora de vencimiento (HH, formato 24 horas): "))
            minuto = int(input("Ingrese los minutos (MM): "))

            # Crear la fecha a partir de los valores ingresados
            fecha_vencimiento_nueva = datetime(anio, mes, dia, hora, minuto)
            break
        except ValueError:
            print("Formato de fecha y hora no válido. Intente nuevamente.")

    # Llamar a la función de editar tarea
    tarea = Tarea()
    tarea.editar_tarea(numero_tarea, Id_usuario, titulo_nuevo, descripcion_nueva, fecha_vencimiento_nueva)



def agregar_recordatorio(Id_usuario):
    print("Agregando recordatorio a tarea...")
    numero_tarea = input("Ingrese el número de la tarea a la que desea agregar el recordatorio (o escriba 'Mostrar' para ver las tareas): ")

    if numero_tarea.lower() == 'mostrar':
        mostrar_tareas(Id_usuario)
        numero_tarea = input("Ingrese el número de la tarea a la que desea agregar el recordatorio: ")

    try:
        fecha_recordatorio = pedir_fecha_recordatorio()
    except ValueError:
        print("Formato de fecha y hora del recordatorio no válido. Se omitirá el recordatorio.")
        fecha_recordatorio = None

    recordatorio = Recordatorio()
    recordatorio.agregar_recordatorio(numero_tarea, fecha_recordatorio)
    print("Recordatorio agregado con éxito.")


def eliminar_tarea(Id_usuario):
    print("Eliminando tarea...")
    tarea = Tarea()
    numero_tarea = input("Ingrese el número de la tarea que quiere eliminar (o escriba 'Mostrar' para ver las tareas): ")

    if numero_tarea.lower() == 'mostrar':
        mostrar_tareas(Id_usuario)
        numero_tarea = input("Ingrese el número de la tarea que desea eliminar: ")

    if numero_tarea:
        tarea.eliminar_tarea(numero_tarea, Id_usuario)


def mostrar_tareas(Id_usuario):
    print("Mostrando tareas...")
    tarea = Tarea()
    tarea.obtener_tareas_usuario(Id_usuario)


def pedir_fecha_vencimiento():
    anio = int(input("Ingrese el año de vencimiento (YYYY): "))
    mes = int(input("Ingrese el mes de vencimiento (MM): "))
    dia = int(input("Ingrese el día de vencimiento (DD): "))
    hora = int(input("Ingrese la hora de vencimiento (HH, formato 24 horas): "))
    minuto = int(input("Ingrese los minutos (MM): "))
    return datetime(anio, mes, dia, hora, minuto)


def pedir_fecha_recordatorio():
    anio = int(input("Ingrese el año del recordatorio (YYYY): "))
    mes = int(input("Ingrese el mes del recordatorio (MM): "))
    dia = int(input("Ingrese el día del recordatorio (DD): "))
    hora = int(input("Ingrese la hora del recordatorio (HH, formato 24 horas): "))
    minuto = int(input("Ingrese los minutos del recordatorio (MM): "))
    return datetime(anio, mes, dia, hora, minuto)


# Llamar al menú principal
menu()
