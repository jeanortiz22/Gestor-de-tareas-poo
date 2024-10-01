from scr.conexion import CConexion
from datetime import datetime, timedelta

class Recordatorio:
    def __init__(self):
        # Recibe una conexión a la base de datos
        self.conexion = CConexion()

    def agregar_recordatorio(self, id_tarea, fecha_recordatorio):
        conn = None
        try:
            conn = self.conexion.ConexionBaseDeDatos()
            with conn.cursor() as cursor:
                insertar_sql = """
                INSERT INTO Recordatorio (fecha_recordatorio, id_tarea)
                VALUES (%s, %s);
                """
                valores = (fecha_recordatorio, id_tarea)
                cursor.execute(insertar_sql, valores)
                conn.commit()
                print("Recordatorio agregado exitosamente.")

        except Exception as e:
            print(f"Error al agregar el recordatorio: {e}")
            if conn:
                conn.rollback()

        finally:
            if conn:
                conn.close()

    def verificar_recordatorios(self, id_usuario):
        conn = None
        try:
            conn = self.conexion.ConexionBaseDeDatos()
            with conn.cursor() as cursor:
                sql = """
                SELECT R.fecha_recordatorio, T.titulo 
                FROM Recordatorio R 
                JOIN Tarea T ON R.id_tarea = T.id_tarea 
                WHERE T.id_usuario = %s AND R.fecha_recordatorio <= %s;
                """
                cursor.execute(sql, (id_usuario, datetime.now() + timedelta(minutes=5)))

                recordatorios = cursor.fetchall()
                for fecha_recordatorio, titulo in recordatorios:
                    print(f"¡Recordatorio! La tarea '{titulo}' está programada para recordarse ahora o pronto.")

        except Exception as e:
            print(f"Error al verificar los recordatorios: {e}")

        finally:
            if conn:
                conn.close()

def intervalo():
    pass
