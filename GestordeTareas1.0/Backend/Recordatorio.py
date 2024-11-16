from scr.conexion import CConexion
from datetime import datetime
from plyer import notification
import time
import threading

class Recordatorio:
    def __init__(self):
        self.conexion = CConexion()
        self.recordatorios_notificados = set()

    def agregar_recordatorio(self, id_tarea, fecha_recordatorio, fecha_vencimiento):
        if fecha_recordatorio >= fecha_vencimiento:
            print(f"Error: La fecha del recordatorio ({fecha_recordatorio}) debe ser anterior a la fecha de vencimiento ({fecha_vencimiento}).")
            return None, f"Error: La fecha del recordatorio ({fecha_recordatorio}) debe ser anterior a la fecha de vencimiento ({fecha_vencimiento})."
        if not fecha_recordatorio:
            return None,"Ingrese una fecha de recordatorio Valida"


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
                return True, "Recordatorio agregado exitosamente."
        except Exception as e:
            print(f"Error al agregar el recordatorio: {e}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.close()

class Escritorio(Recordatorio):
    def __init__(self):
        super().__init__()  # Llamamos al constructor de la clase padre (Recordatorio)

    def verificar_recordatorios(self):
        conn = None
        try:
            conn = self.conexion.ConexionBaseDeDatos()
            with conn.cursor() as cursor:
                sql = """
                SELECT R.id_recordatorio, R.fecha_recordatorio, T.titulo
                FROM Recordatorio R 
                JOIN Tarea T ON R.id_tarea = T.id_tarea
                WHERE R.fecha_recordatorio = %s;
                """
                # Comparar con la hora actual exacta
                fecha_actual = datetime.now().replace(second=0, microsecond=0)
                cursor.execute(sql, (fecha_actual,))
                recordatorios = cursor.fetchall()

                # Mostrar las notificaciones solo para tareas en el momento exacto y que no se hayan notificado antes
                for id_recordatorio, fecha_recordatorio, titulo in recordatorios:
                    if id_recordatorio not in self.recordatorios_notificados:
                        self.enviar_notificacion(
                            titulo=f"🔔 RECORDATORIO GESTOR DE TAREAS PERSONALIZADO",
                            mensaje=f"La tarea '{titulo}' está programada para ahora."
                        )
                        # Marcar el recordatorio como ya notificado
                        self.recordatorios_notificados.add(id_recordatorio)

        except Exception as e:
            print(f"Error al verificar los recordatorios: {e}")
        finally:
            if conn:
                conn.close()

    def enviar_notificacion(self, titulo, mensaje):
        max_length = 64
        titulo = (titulo[:max_length] + '...') if len(titulo) > max_length else titulo
        mensaje = (mensaje[:max_length] + '...') if len(mensaje) > max_length else mensaje

        notification.notify(
            title=titulo,
            message=mensaje,
            timeout=40  # Duración de la notificación en segundos
        )

    def iniciar_verificacion_automatica(self):

        def verificar_periodicamente():
            while True:
                self.verificar_recordatorios()
                time.sleep(30)  # Esperar 1 minuto antes de verificar nuevamente

        hilo = threading.Thread(target=verificar_periodicamente, daemon=True)
        hilo.start()

    def obtener_fecha_recordatorio_por_id_tarea(self, id_tarea):
        conn = None
        try:
            conn = self.conexion.ConexionBaseDeDatos()
            with conn.cursor() as cursor:
                sql = """
                SELECT R.fecha_recordatorio
                FROM Recordatorio R
                WHERE R.id_tarea = %s;
                """
                cursor.execute(sql, (id_tarea,))
                recordatorio = cursor.fetchone()

                if recordatorio:
                    fecha_recordatorio = recordatorio[0]
                    return fecha_recordatorio
                else:
                    print("No se encontró un recordatorio para el id_tarea especificado.")
                    return None

        except Exception as e:
            print(f"Error al obtener la fecha del recordatorio: {e}")
            return None
        finally:
            if conn:
                conn.close()