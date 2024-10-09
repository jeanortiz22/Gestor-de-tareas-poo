from scr.conexion import CConexion
from Tarea import Tarea
from usuario import Usuarios
from Recordatorio import Recordatorio
from datetime import datetime


# Constantes para facilitar el uso de opciones válidas
ESTADOS_VALIDOS = ['Completa', 'Incompleta', 'Pendiente']
PRIORIDADES_VALIDAS = ['Alta', 'Media', 'Baja']


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
    exito,Id_usuario,nombre = usuario.login(correo, contrasena)
    if exito:
        menu_tareas(Id_usuario)
    else:
        print("Error de autenticación. Por favor, verifique sus credenciales.")


def registrar_usuario():
    nombre = input("Ingrese su nombre de usuario(Debe tener entre 3 y 30 caracteres y solo contener letras, números o guiones bajos): ")
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
        print("6. Buscar tarea")
        print("7. Asignar etiqueta a tarea")  # Nueva opción
        print("8. Asignar categoría a tarea")  # Nueva opción
        print("9. Cerrar sesión")

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
            buscar_tarea(Id_usuario)
        elif opcion == '7':
            asignar_etiqueta(Id_usuario)  # Llama a la función para asignar etiqueta
        elif opcion == '8':
            asignar_categoria(Id_usuario)  # Llama a la función para asignar categoría
        elif opcion == '9':
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida, intente nuevamente.")


def asignar_etiqueta(Id_usuario):
    tarea = Tarea()
    if not tarea.hay_tareas(Id_usuario):
        print("No hay tareas disponibles para asignar una etiqueta.")
        return

    numero_tarea = input("Ingrese el número de la tarea para asignar etiqueta (o escriba 'Mostrar' para ver las tareas): ")
    if numero_tarea.lower() == 'mostrar':
        mostrar_tareas(Id_usuario)
        numero_tarea = input("Ingrese el número de la tarea a la que desea asignar etiqueta: ")

    etiqueta = validar_opcion("prioridad", PRIORIDADES_VALIDAS)
    tarea.asignar_etiqueta(numero_tarea, Id_usuario, etiqueta)


def asignar_categoria(Id_usuario):
    tarea = Tarea()
    if not tarea.hay_tareas(Id_usuario):
        print("No hay tareas disponibles para asignar una categoría.")
        return

    numero_tarea = input("Ingrese el número de la tarea para asignar categoría (o escriba 'Mostrar' para ver las tareas): ")
    if numero_tarea.lower() == 'mostrar':
        mostrar_tareas(Id_usuario)
        numero_tarea = input("Ingrese el número de la tarea a la que desea asignar categoría: ")

    categoria = validar_opcion("estado", ESTADOS_VALIDOS)
    tarea.asignar_categoria(numero_tarea, Id_usuario, categoria)


def validar_opcion(tipo, opciones_validas):
    opcion = input(f"Ingrese la {tipo} ({', '.join(opciones_validas)}): ").capitalize()
    while opcion not in opciones_validas:
        print(f"Opción inválida. Ingrese una {tipo} válida.")
        opcion = input(f"Ingrese la {tipo} ({', '.join(opciones_validas)}): ").capitalize()
    return opcion


def buscar_tarea(Id_usuario):
    print("Buscar tareas...")
    titulo = input("Ingrese el título de la tarea a buscar (o deje en blanco): ")
    descripcion = input("Ingrese la descripción de la tarea a buscar (o deje en blanco): ")
    estado = input(f"Ingrese el estado de la tarea ({', '.join(ESTADOS_VALIDOS)} o deje en blanco): ").capitalize()
    prioridad = input(f"Ingrese la prioridad de la tarea ({', '.join(PRIORIDADES_VALIDAS)} o deje en blanco): ").capitalize()

    try:
        fecha_vencimiento = pedir_fecha_vencimiento() if input("¿Desea buscar por fecha de vencimiento? (S/N): ").upper() == 'S' else None
    except ValueError:
        print("Fecha de vencimiento no válida.")
        fecha_vencimiento = None

    tarea = Tarea()
    tarea.buscar_tarea(titulo=titulo, descripcion=descripcion, estado=estado, prioridad=prioridad, fecha_vencimiento=fecha_vencimiento)

def agregar_tarea(Id_usuario):
    print("Agregando tarea...")
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")

    try:
        fecha_vencimiento = pedir_fecha_vencimiento()
    except ValueError:
        print("Formato de fecha y hora de vencimiento no válido. Se omitirá la tarea.")
        return

    # Ya no pedimos estado y prioridad (etiqueta y categoría)
    tarea = Tarea(titulo, descripcion, None, fecha_vencimiento, None, None, Id_usuario, None)
    tarea.agregar_tarea()

def editar_tarea(Id_usuario):
    print("Editando tarea...")
    numero_tarea = input("Ingrese el número de la tarea: ")
    titulo_nuevo = input("Ingrese el nuevo título de la tarea: ")
    descripcion_nueva = input("Ingrese la nueva descripción de la tarea: ")

    try:
        fecha_vencimiento_nueva = pedir_fecha_vencimiento()
    except ValueError:
        print("Formato de fecha y hora no válido. Intente nuevamente.")
        return

    tarea = Tarea()
    tarea.editar_tarea(numero_tarea, Id_usuario, titulo_nuevo, descripcion_nueva, fecha_vencimiento_nueva)


def agregar_recordatorio(Id_usuario):
    print("Agregando recordatorio a tarea...")
    tarea = Tarea()

    # Mostrar las tareas disponibles si el usuario lo solicita
    opcion = input("Ingrese el número de la tarea a la que desea agregar el recordatorio (o escriba 'Mostrar' para ver las tareas): ")
    if opcion.lower() == 'mostrar':
        mostrar_tareas(Id_usuario)
        opcion = input("Ingrese el número de la tarea a la que desea agregar el recordatorio: ")

    numero_tarea = opcion

    # Obtener la fecha de vencimiento de la tarea seleccionada
    conn = tarea.conexion.ConexionBaseDeDatos()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT fecha_vencimiento FROM Tarea WHERE id_tarea = %s AND id_usuario = %s;", (numero_tarea, Id_usuario))
            resultado = cursor.fetchone()
            if not resultado:
                print("No se encontró la tarea especificada.")
                return
            fecha_vencimiento = resultado[0]
    except Exception as e:
        print(f"Error al obtener la fecha de vencimiento: {e}")
        return
    finally:
        conn.close()

    try:
        # Pedir la fecha de recordatorio
        fecha_recordatorio = pedir_fecha_recordatorio()
    except ValueError:
        print("Formato de fecha y hora del recordatorio no válido. Se omitirá el recordatorio.")
        fecha_recordatorio = None

    if fecha_recordatorio:
        recordatorio = Recordatorio()
        recordatorio.agregar_recordatorio(numero_tarea, fecha_recordatorio, fecha_vencimiento)
        recordatorio.iniciar_verificacion_automatica()


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
    return pedir_fecha("vencimiento")


def pedir_fecha_recordatorio():
    return pedir_fecha("recordatorio")


def pedir_fecha(tipo_fecha):
    try:
        anio = int(input(f"Ingrese el año de {tipo_fecha} (YYYY): "))
        mes = int(input(f"Ingrese el mes de {tipo_fecha} (MM): "))
        dia = int(input(f"Ingrese el día de {tipo_fecha} (DD): "))
        hora = int(input(f"Ingrese la hora de {tipo_fecha} (HH, formato 24 horas): "))
        minuto = int(input(f"Ingrese los minutos de {tipo_fecha} (MM): "))
        return datetime(anio, mes, dia, hora, minuto)
    except ValueError:
        raise ValueError("Fecha no válida.")


def validar_opcion(tipo, opciones_validas):
    opcion = input(f"Ingrese el {tipo} ({', '.join(opciones_validas)}): ").capitalize()
    while opcion not in opciones_validas:
        print(f"Opción inválida. Ingrese un {tipo} válido.")
        opcion = input(f"Ingrese el {tipo} ({', '.join(opciones_validas)}): ").capitalize()
    return opcion


# Llamar al menú principal
menu()
