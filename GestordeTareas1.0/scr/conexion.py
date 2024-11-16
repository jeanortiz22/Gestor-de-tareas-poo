import psycopg2

class CConexion:
    def ConexionBaseDeDatos(self):
        try:
            connection = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='andrea915',
                database='GestorTareas'
            )
            return connection
        except Exception as ex:
            print(f"Error de conexión: {ex}")
            return None  # Devolver None en caso de error



