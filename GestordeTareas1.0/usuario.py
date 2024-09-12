from scr.conexion import CConexion


class Usuarios:
    def __init__(self, nombre='', correo='', contrasena=''):
        # Atributos del usuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        # Crear una instancia de CConexion
        self.conexion = CConexion()

    def registrarusuarios(self):
        if not self.correo or not self.nombre or not self.contrasena:
            print("Tienes que ingresar todos los datos")
            return

        # Verificar que el correo contenga "@" y "."
        if "@" not in self.correo or "." not in self.correo.split("@")[-1]:
            print("Correo no válido")
            return

        # Verificar que la longitud del nombre no supere los 30 caracteres
        if len(self.nombre) > 30:
            print("El nombre de usuario no puede superar los 30 caracteres")
            return

        # Obtener la conexión a la base de datos
        conn = self.conexion.ConexionBaseDeDatos()
        if conn is None:
            print("Error al conectar a la base de datos.")
            return

        try:
            # Crear un cursor para ejecutar comandos SQL
            with conn.cursor() as cursor:
                # Verificar que el correo no esté registrado
                sql_verificar = "SELECT correo FROM usuarios WHERE correo = %s;"
                cursor.execute(sql_verificar, (self.correo,))
                resultado = cursor.fetchone()

                if resultado:
                    print("El correo ya está registrado")
                    return

                # Consulta SQL para insertar un nuevo usuario
                sql = """
                INSERT INTO usuarios (nombre_completo, correo, contraseña)
                VALUES (%s, %s, %s);
                """
                valores = (self.nombre, self.correo, self.contrasena)

                # Ejecutar la consulta SQL
                cursor.execute(sql, valores)

                # Confirmar los cambios en la base de datos
                conn.commit()

                print("Usuario registrado exitosamente.")
                return True

        except Exception as e:
            # Imprimir el error en caso de que algo salga mal
            print(f"Error al registrar el usuario: {e}")

        finally:
            # Cerrar la conexión a la base de datos
            conn.close()

    def login(self,correo,contrasena):
        # Obtener la conexión a la base de datos
        conn = self.conexion.ConexionBaseDeDatos()
        if conn is None:
            print("Error al conectar a la base de datos.")
            return

        try:
            # Crear un cursor para ejecutar comandos SQL
            with conn.cursor() as cursor:
                # Consulta SQL para obtener el usuario por correo
                sql = "SELECT id_usuario, contraseña FROM usuarios WHERE correo = %s;"
                cursor.execute(sql, (correo,))

                # Obtener el resultado de la consulta
                resultado = cursor.fetchone()

                if resultado:
                    id_usuario,stored_password = resultado

                    # Comparar la contraseña ingresada con la almacenada en la base de datos
                    if contrasena == stored_password:
                        print("Inicio de sesión exitoso.")
                        return id_usuario
                    else:
                        print("Usuario o contraseña incorrecta .")
                        return None
                else:
                    print("Usuario o contraseña incorrecta.")
                    return None

        except Exception as e:
            # Imprimir el error en caso de que algo salga mal
            print(f"Error al intentar iniciar sesión: {e}")

        finally:
            # Cerrar la conexión a la base de datos
            conn.close()



