from scr.conexion import CConexion
from Tarea import Tarea
from usuario import Usuarios
from datetime import datetime



# Menú principal
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("Iniciando sesión...")
            correo = input("Digite su Correo: ")
            contrasena = input("Digite su contraseña: ")
            usuario = Usuarios()
            Id_usuario = usuario.login(correo, contrasena)
            if Id_usuario:
                menu_tareas(Id_usuario)

        elif opcion == '2':
            print("Registrando usuario...")
            nombre = input("Ingrese su nombre completo: ")
            correo = input("Ingrese su correo electrónico: ")
            contrasena = input("Ingrese una contraseña: ")
            confirmar_contrasena = input("Confirme su contraseña: ")

            if contrasena == confirmar_contrasena:
                usuario = Usuarios(nombre, correo, contrasena, confirmar_contrasena)
                usuario.registrarusuarios()


        elif opcion == '3':
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intente nuevamente.")


# Función para mostrar el menú de tareas
def menu_tareas(Id_usuario):
    while True:
        print("\n--- Menú de Tareas ---")
        print("1. Agregar tarea")
        print("2. Editar tarea")
        print("3. Eliminar tarea")
        print("4. Mostrar tareas")
        print("5. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("Agregando tarea...")
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha_vencimiento_str = input("Ingrese la fecha de vencimiento (formato: YYYY-MM-DD HH:MM): ")
            estado = input("Ingrese el estado (Completa, Incompleta, Pendiente): ")
            prioridad = input("Ingrese el nivel de importancia del proyecto (Alta, Media, Baja): ")
            try:
                fecha_vencimiento = datetime.strptime(fecha_vencimiento_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Formato de fecha y hora no válido. Intente nuevamente.")
                continue

            tarea = Tarea(titulo, descripcion, None, fecha_vencimiento, estado, prioridad, Id_usuario)
            tarea.agregar_tarea()

        elif opcion == '2':
            print("Editando tarea...")
            numero_tarea = input("Ingrese el numero de la tarea: ")
            titulo_nuevo = input("Ingrese el título de la tarea: ")
            descripcion_nuevo = input("Ingrese la descripción de la tarea: ")
            fecha_vencimiento_str_nuevo = input("Ingrese la fecha de vencimiento (formato: YYYY-MM-DD HH:MM): ")
            estado_nuevo = input("Ingrese el estado (Completa, Incompleta, Pendiente): ")
            prioridad_nuevo = input("Ingrese el nivel de importancia del proyecto (Alta, Media, Baja): ")
            try:
                fecha_vencimiento_nuevo = datetime.strptime(fecha_vencimiento_str_nuevo, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Formato de fecha y hora no válido. Intente nuevamente.")
                continue

            # Llamar a la función de editar tarea
            tarea = Tarea()
            tarea.editar_tarea(numero_tarea,Id_usuario,titulo_nuevo,descripcion_nuevo,fecha_vencimiento_nuevo,estado_nuevo,prioridad_nuevo)

        elif opcion == '3':
            print("Eliminar tarea...")
            tarea = Tarea()
            numero_tarea = input("Ingrese el numero de la tarea que quieres eliminar (SI NO TE LOS SABES ESCRIBE Mostrar: ")
            if numero_tarea == "Mostrar":
                print("Voy a mostrarte todas las tareas que tienes ")
                tarea.obtener_tareas_usuario(Id_usuario)
                numero_tarea2= input("Ingrese el numero que quiere eliminar: ")
                if numero_tarea2:
                    tarea.eliminar_tarea(numero_tarea2, Id_usuario)

            else:
                tarea.eliminar_tarea(numero_tarea,Id_usuario)

            # Llamar a la función de eliminar tarea

        elif opcion == '4':
            print("Mostrando tareas...")
            tarea = Tarea()
            tarea.obtener_tareas_usuario(Id_usuario)
            # Llamar a la función de mostrar tareas
            pass

        elif opcion == '5':
            print("Cerrando sesión...")
            break

        else:
            print("Opción no válida, intente nuevamente.")

# Llamar al menú principal
menu()