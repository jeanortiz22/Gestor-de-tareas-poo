from scr.conexion import CConexion

class Categoria:
    def __init__(self):
        self.conexion = CConexion()

    def asignar_categoria(self, id_tarea, id_usuario, categoria):
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

                actualizar_sql = """
                UPDATE Tarea
                SET estado = %s  -- Usamos el campo 'estado' como 'categoría'
                WHERE id_tarea = %s AND id_usuario = %s;
                """
                cursor.execute(actualizar_sql, (categoria, id_tarea, id_usuario))
                conn.commit()

                if cursor.rowcount > 0:
                    print("Categoría asignada exitosamente.")
                else:
                    print("No se pudo asignar la categoría.")

        except Exception as e:
            print(f"Error al asignar la categoría: {e}")
            if conn:
                conn.rollback()

        finally:
            if conn:
                conn.close()

    def hay_tareas(self, id_usuario):
        conn = self.conexion.ConexionBaseDeDatos()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT 1 FROM Tarea WHERE id_usuario = %s;"
                cursor.execute(sql, (id_usuario,))
                return cursor.fetchone() is not None

        except Exception as e:
            print(f"Error al verificar tareas: {e}")
            return False

        finally:
            conn.close()