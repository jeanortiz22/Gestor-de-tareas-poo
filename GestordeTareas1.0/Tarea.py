from scr.conexion import CConexion
from datetime import datetime



class Tarea:
    def __init__(self,titulo='', descripcion='', fecha_creacion='', fecha_vencimiento='', estado='', prioridad='', id_usuario=''):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.prioridad = prioridad
        self.id_usuario = id_usuario

        # Recibe una conexión a la base de datos
        self.conexion = CConexion()

    def agregar_tarea(self):
        conn = None
        try:
            # Conectarse a la base de datos
            conn = self.conexion.ConexionBaseDeDatos()
            with conn.cursor() as cursor:
                # Crear la consulta SQL para insertar una nueva tarea
                insertar_sql = """
                INSERT INTO Tarea (titulo, descripcion, fecha_creacion, fecha_vencimiento, estado, prioridad, id_usuario)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
                """
                # Definir los valores de la tarea
                valores = (
                    self.titulo,
                    self.descripcion,
                    datetime.now(),  # Fecha de creación actual
                    self.fecha_vencimiento,
                    self.estado,
                    self.prioridad,
                    self.id_usuario
                )
                # Ejecutar la consulta
                cursor.execute(insertar_sql, valores)
                # Confirmar los cambios
                conn.commit()
                print("Tarea agregada exitosamente.")

        except Exception as e:
            print(f"Error al agregar la tarea: {e}")
            if conn:
                conn.rollback()

        finally:
            # Asegurarse de cerrar la conexión a la base de datos
            if conn:
                conn.close()

    def editar_tarea(self, id_tarea, id_usuario, nuevo_titulo=None, nueva_descripcion=None,
                     nueva_fecha_vencimiento=None, nuevo_estado=None, nueva_prioridad=None):
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
                    fecha_vencimiento = COALESCE(%s, fecha_vencimiento),
                    estado = COALESCE(%s, estado),
                    prioridad = COALESCE(%s, prioridad)
                WHERE id_tarea = %s AND id_usuario = %s;
                """

                # Definir los valores a actualizar, usando los valores existentes si son `None`
                valores = (
                    nuevo_titulo,
                    nueva_descripcion,
                    nueva_fecha_vencimiento,
                    nuevo_estado,
                    nueva_prioridad,
                    id_tarea,
                    id_usuario
                )

                # Ejecutar la consulta
                cursor.execute(actualizar_sql, valores)

                # Confirmar los cambios
                conn.commit()

                if cursor.rowcount > 0:
                    print("Tarea actualizada exitosamente.")
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

                # Crear la consulta SQL para eliminar una tarea
                eliminar_sql = """
                DELETE FROM Tarea WHERE id_tarea = %s AND id_usuario = %s;
                """
                # Ejecutar la consulta
                cursor.execute(eliminar_sql, (id_tarea, id_usuario))
                # Confirmar los cambios
                conn.commit()
                if cursor.rowcount > 0:
                    print("Tarea eliminada exitosamente.")
                else:
                    print("No se encontró una tarea con ese ID para el usuario especificado.")

        except Exception as e:
            print(f"Error al eliminar la tarea: {e}")
            if conn:
                conn.rollback()

        finally:
            # Asegurarse de cerrar la conexión a la base de datos
            if conn:
                conn.close()

    def obtener_tareas_usuario(self, id_usuario):
        # Obtener la conexión a la base de datos
        conn = self.conexion.ConexionBaseDeDatos()
        if conn is None:
            print("Error al conectar a la base de datos.")
            return None

        try:
            # Crear un cursor para ejecutar comandos SQL
            with conn.cursor() as cursor:
                # Consulta SQL para obtener todas las tareas del usuario específico
                sql = "SELECT id_tarea, titulo, descripcion, fecha_vencimiento, estado, prioridad FROM Tarea WHERE id_usuario = %s;"
                cursor.execute(sql, (id_usuario,))

                # Obtener todas las filas de resultados de la consulta
                tareas = cursor.fetchall()

                # Imprimir las tareas obtenidas
                for tarea in tareas:
                    print(tarea)

                return tareas

        except Exception as e:
            print(f"Error al obtener las tareas: {e}")
            return None

        finally:
            conn.close()


