from scr.conexion import CConexion

class Busqueda:
    def __init__(self):
        self.conexion = CConexion()

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

                return tareas

        except Exception as e:
            print(f"Error al buscar tareas: {e}")
            return None
        finally:
            if conn:
                conn.close()
