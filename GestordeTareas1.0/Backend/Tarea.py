from scr.conexion import CConexion
from datetime import datetime
import re


class Tarea:
    def __init__(self, titulo='', descripcion='', fecha_creacion='', fecha_vencimiento='', estado=None, prioridad=None, id_usuario='', fecha_recordatorio=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado  # Inicialmente None
        self.prioridad = prioridad  # Inicialmente None
        self.id_usuario = id_usuario
        self.fecha_recordatorio = fecha_recordatorio
        self.conexion = CConexion()

    def agregar_tarea(self):
        # Validación del título
        if len(self.titulo) > 20:
            print("El título de la tarea no puede exceder los 20 caracteres")
            return None, "El título de la tarea no puede exceder los 20 caracteres"

        if len(self.titulo) == 0:
            print("El título tiene que contener al menos 1 letra")
            return None, "El título tiene que contener al menos 1 letra"

        # Validación de la fecha de vencimiento
        if not self.fecha_vencimiento:
            return None, "Ingrese una fecha de vencimiento válida"

        formato_fecha = r"^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$"
        if not re.match(formato_fecha, self.fecha_vencimiento):
            return None, "Ingrese una fecha de vencimiento válida en el formato 'dd/MM/yyyy HH:mm'"

        try:
            # Convertir la fecha de vencimiento al formato adecuado para la base de datos
            fecha_vencimiento_bd = datetime.strptime(self.fecha_vencimiento, "%d/%m/%Y %H:%M")
        except ValueError:
            return None, "Error al procesar la fecha de vencimiento. Verifique el formato."

        conn = None
        try:
            conn = self.conexion.ConexionBaseDeDatos()
            with conn.cursor() as cursor:
                insertar_sql = """
                INSERT INTO Tarea (titulo, descripcion, fecha_creacion, fecha_vencimiento, estado, prioridad, id_usuario)
                VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id_tarea;
                """
                valores = (
                    self.titulo,
                    self.descripcion,
                    datetime.now(),  # Fecha de creación actual
                    fecha_vencimiento_bd,  # Fecha de vencimiento convertida
                    self.estado,  # Esto será None hasta que se asigne una categoría
                    self.prioridad,  # Esto será None hasta que se asigne una etiqueta
                    self.id_usuario
                )
                cursor.execute(insertar_sql, valores)
                id_tarea = cursor.fetchone()[0]
                conn.commit()

                print("Tarea agregada exitosamente.")
                return True, "Tarea agregada exitosamente."

        except Exception as e:
            print(f"Error al agregar la tarea: {e}")
            if conn:
                conn.rollback()
            return None, f"Error al agregar la tarea: {e}"

        finally:
            if conn:
                conn.close()

    def editar_tarea(self, id_tarea, id_usuario, nuevo_titulo=None, nueva_descripcion=None,
                     nueva_fecha_vencimiento=None):

        if len(nuevo_titulo) > 20:
            print("El titulo de la tarea no puede exceder los 20 caracteres")
            return None, "El titulo de la tarea no puede exceder los 20 caracteres"

        if len(nuevo_titulo) == 0:
            print("El titulo tiene que contener al menos 1 letra")
            return None ,"El titulo tiene que contener al menos 1 letra"



        conn = None
        try:
            # Conectarse a la base de datos
            conn = self.conexion.ConexionBaseDeDatos()
            with conn.cursor() as cursor:
                # Verificar si la tarea pertenece al usuario especificado
                verificar_sql = """
                SELECT 1 FROM Tarea WHERE id_tarea = %s AND id_usuario = %s;
                """
                cursor.execute(verificar_sql, (id_tarea, id_usuario))
                if cursor.fetchone() is None:
                    print("No se encontró una tarea con ese ID para el usuario especificado.")
                    return

                # Crear la consulta SQL para actualizar la tarea
                actualizar_sql = """
                UPDATE Tarea
                SET titulo = COALESCE(%s, titulo),
                    descripcion = COALESCE(%s, descripcion),
                    fecha_vencimiento = COALESCE(%s, fecha_vencimiento) 
                WHERE id_tarea = %s AND id_usuario = %s;
                """

                # Definir los valores a actualizar, usando los valores existentes si son `None`
                valores = (
                    nuevo_titulo,
                    nueva_descripcion,
                    nueva_fecha_vencimiento,
                    id_tarea,
                    id_usuario
                )

                # Ejecutar la consulta
                cursor.execute(actualizar_sql, valores)

                # Confirmar los cambios
                conn.commit()

                if cursor.rowcount > 0:
                    print("Tarea actualizada exitosamente.")
                    return True,"Tarea actualizada exitosamente."
                else:
                    print("No se pudo actualizar la tarea.")

        except Exception as e:
            print(f"Error al editar la tarea: {e}")
            if conn:
                conn.rollback()

        finally:
            # Asegurarse de cerrar la conexión a la base de datos
            if conn:
                conn.close()


    def eliminar_tarea(self, id_tarea, id_usuario):
        conn = None
        try:
            conn = self.conexion.ConexionBaseDeDatos()
            with conn.cursor() as cursor:
                verificar_sql = """
                SELECT 1 FROM Tarea WHERE id_tarea = %s AND id_usuario = %s;
                """
                cursor.execute(verificar_sql, (id_tarea, id_usuario))
                if cursor.fetchone() is None:
                    print("No se encontró una tarea con ese ID para el usuario especificado.")
                    return

                eliminar_sql = """
                DELETE FROM Tarea WHERE id_tarea = %s AND id_usuario = %s;
                """
                cursor.execute(eliminar_sql, (id_tarea, id_usuario))
                conn.commit()
                if cursor.rowcount > 0:
                    print("Tarea eliminada exitosamente.")
                    return True,"Tarea eliminada exitosamente."
                else:
                    print("No se encontró una tarea con ese ID para el usuario especificado.")

        except Exception as e:
            print(f"Error al eliminar la tarea: {e}")
            if conn:
                conn.rollback()

        finally:
            if conn:
                conn.close()

    def obtener_tareas_usuario(self, id_usuario):
        # Conexión a la base de datos
        conn = self.conexion.ConexionBaseDeDatos()
        if conn is None:
            print("Error al conectar a la base de datos.")
            return None

        try:
            # Crear un cursor para ejecutar la consulta
            with conn.cursor() as cursor:
                # Consulta SQL para obtener las tareas del usuario
                sql = """
                    SELECT id_tarea, titulo, descripcion, fecha_vencimiento, estado, prioridad
                    FROM Tarea
                    WHERE id_usuario = %s
                    ORDER BY id_tarea DESC;
                """
                cursor.execute(sql, (id_usuario,))
                tareas = cursor.fetchall()

                # Verificar si hay tareas y mostrarlas
                if tareas:
                    for tarea in tareas:
                        print(f"Tarea ID: {tarea[0]}")
                        print(f"Título: {tarea[1]}")
                        print(f"Descripción: {tarea[2]}")
                        print(f"Fecha de Vencimiento: {tarea[3]}")
                        print(f"Estado: {tarea[4]}")
                        print(f"Prioridad: {tarea[5]}")
                        print("--------")
                else:
                    print("No hay tareas para mostrar.")

                return tareas
        except Exception as e:
            # Manejo de errores
            print(f"Error al obtener las tareas: {e}")
            return None
        finally:
            # Cerrar la conexión a la base de datos
            conn.close()

    def buscar_tareas(self, id_usuario, termino_busqueda):
        """
        Busca tareas por título, descripción, estado o prioridad para un usuario específico.

        """
        conn = None
        try:
            conn = self.conexion.ConexionBaseDeDatos()
            with conn.cursor() as cursor:
                # Consulta SQL para buscar tareas
                sql = """
                    SELECT id_tarea, titulo, descripcion, fecha_vencimiento, estado, prioridad
                    FROM Tarea
                    WHERE id_usuario = %s AND 
                          (titulo ILIKE %s OR 
                           descripcion ILIKE %s OR 
                           estado ILIKE %s OR 
                           prioridad ILIKE %s)
                    ORDER BY id_tarea DESC;
                """
                # Filtrar utilizando el término de búsqueda con comodines
                termino_filtro = f"%{termino_busqueda}%"
                cursor.execute(sql, (id_usuario, termino_filtro, termino_filtro, termino_filtro, termino_filtro))
                tareas = cursor.fetchall()

                # Formatear el resultado en una lista de diccionarios para facilitar su uso
                lista_tareas = []
                for tarea in tareas:
                    lista_tareas.append({
                        "id_tarea": tarea[0],
                        "titulo": tarea[1],
                        "descripcion": tarea[2],
                        "fecha_vencimiento": tarea[3].strftime("%d/%m/%Y %H:%M") if tarea[3] else None,
                        "estado": tarea[4],
                        "prioridad": tarea[5]
                    })

                return lista_tareas

        except Exception as e:
            print(f"Error al buscar tareas: {e}")
            return None
        finally:
            if conn:
                conn.close()
