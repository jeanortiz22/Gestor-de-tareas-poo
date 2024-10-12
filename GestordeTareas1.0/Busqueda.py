from scr.conexion import CConexion

class Busqueda:
    def __init__(self):
        self.conexion = CConexion()

    def buscar_tarea(self, titulo=None, descripcion=None, estado=None, prioridad=None, fecha_vencimiento=None):
        conn = None
        try:
            conn = self.conexion.ConexionBaseDeDatos()
            with conn.cursor() as cursor:
                # Condiciones de búsqueda
                condiciones = []
                valores = []

                if titulo:
                    condiciones.append("titulo LIKE %s")
                    valores.append(f"%{titulo}%")

                if descripcion:
                    condiciones.append("descripcion LIKE %s")
                    valores.append(f"%{descripcion}%")

                if estado:
                    condiciones.append("estado = %s")
                    valores.append(estado)

                if prioridad:
                    condiciones.append("prioridad = %s")
                    valores.append(prioridad)

                if fecha_vencimiento:
                    condiciones.append("fecha_vencimiento = %s")
                    valores.append(fecha_vencimiento)

                # Construir la consulta SQL con las condiciones
                sql = "SELECT * FROM Tarea"
                if condiciones:
                    sql += " WHERE " + " AND ".join(condiciones)

                cursor.execute(sql, valores)
                tareas = cursor.fetchall()

                # Mostrar resultados solo con la información de las tareas
                if tareas:
                    for tarea in tareas:
                        print("Información de la tarea:")
                        print(f"- ID Tarea: {tarea[0]}")  # Suponiendo que el ID de la tarea es el primer elemento
                        print(f"- Título: {tarea[1]}")
                        print(f"- Descripción: {tarea[2]}")
                        print(f"- Fecha de creación: {tarea[3]}")
                        print(f"- Fecha de vencimiento: {tarea[4]}")
                        print(f"- Estado: {tarea[5]}")
                        print(f"- Prioridad: {tarea[6]}")
                        print("--------------------------")
                else:
                    print("No se encontraron tareas que coincidan con los criterios de búsqueda.")

        except Exception as e:
            print(f"Error al buscar tarea: {e}")

        finally:
            if conn:
                conn.close()
